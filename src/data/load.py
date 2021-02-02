"""Load CSVs to PostgreSQL tables"""

def generate_sql_stmt(dataset, table_name, column_def):
    """Generates SQL commands to load CSV to Postgres.
    
    Parameters
    ----------
    dataset : str
        The name of the StackExchange dataset. This will be used as schema name.
    
    table_name : str
        The name of the dataset table to load to Postgres.
        
    column_def : dict
        A dictionary of column names and data types of the table to be created.
        
    Returns
    -------
    sql : str
        The complete SQL statement
    
    """
    
    import json
    import os
    from src.utils.misc import camel_to_snake_case
    

    dataset_metadata = json.load(open('data/metadata/{}.json'.format(dataset), 'r'))
    table_metadata = dataset_metadata[table_name]
    data_columns = table_metadata['columns']
    
    # Adjust column def based on fields present in actual data
    column_def_adj = {x:column_def[x] for x in data_columns if x in column_def.keys()}
    
    # Check if all data columns have corresponding column type in schema definition
    assert len([x for x in data_columns if x not in column_def.keys()])==0, 'Error. Extra columns are present in data which are missing in schema definition.'
    
    filepath = table_metadata['csv']
    schema_name = camel_to_snake_case(dataset.replace('.','_'))
    
    # DROP table statement
    drop_stmt = 'DROP TABLE IF EXISTS {}.{};'.format(schema_name, table_name)
    
    # CREATE statement
    lines = []
    lines.append('CREATE TABLE {}.{} (\n'.format(schema_name, table_name))
    lines += ['    {}\t{},\n'.format(k.ljust(20,' '),v) for k,v in column_def_adj.items()]
    lines.append('    PRIMARY KEY (id)\n')
    lines.append(');')
    create_stmt = ''.join(lines)
    
    # COPY statement
    lines = []
    lines.append('COPY {}.{}({})'.format(schema_name, table_name, ', '.join(column_def_adj.keys())))
    lines.append("FROM '{}'".format(filepath))
    lines.append("WITH (")
    lines.append("  FORMAT CSV,")
    lines.append("  DELIMITER ',',")
    lines.append("  NULL '',")
    lines.append("  HEADER,")
    lines.append("  FORCE_NULL({})".format(', '.join([x for x in column_def_adj if x != 'id'])))
    lines.append(");")
    copy_stmt = '\n'.join(lines)
    
    commit_stmt = 'COMMIT;'
    
    sql = '\n\n'.join([drop_stmt, create_stmt, copy_stmt, commit_stmt])
    
    return sql


def load_data(dataset, table_name):
    """Loads CSV data to a Postgres table.
    
    Parameters
    ----------
    dataset : str
        The name of the StackExchange dataset. This will be used as schema name.
    
    table_name : str
        The name of the dataset table to load to Postgres.

    Returns
    -------
    None
    
    """
    
    import os
    import json
    from sqlalchemy import create_engine
    from src.utils.misc import camel_to_snake_case
    
    root = os.getcwd()
    
    # Parse schema info
    schema_def = json.load(open('{}/data/metadata/postgres_schema.json'.format(root),'r'))
    column_def = schema_def[table_name]
    sql_stmt = generate_sql_stmt(dataset, table_name, column_def)
    
    # Execute SQL commands
    DATABASE_URI = 'postgres+psycopg2://postgres:password@localhost:5432/stackexchange'
    engine = create_engine(DATABASE_URI)
    
    with engine.connect() as conn:
        conn.execute(sql_stmt)
        
    print('Loaded data to: {}.{}'.format(camel_to_snake_case(dataset.replace('.','_')), table_name))
    
    
def load_dataset(dataset):
    """Loads all tables for a specific dataset.
    
    Parameters
    ----------
    dataset : str
        The name of the StackExchange dataset. This will be used as schema name.
        
    Returns
    -------
    None
    
    """
    
    import os
    import json
    
    
    # Parse schema info
    root = os.getcwd()
    metadata = json.load(open('{}/data/metadata/postgres_schema.json'.format(root),'r'))
    table_list = list(metadata.keys())
    
    # Load each table data
    for table_name in table_list:
        load_data(dataset, table_name)
        
    print('\n\nFinished loading all tables for dataset: {}'.format(dataset))


if __name__ == '__main__':
    
    dataset = input() 
    load_dataset(dataset)
   