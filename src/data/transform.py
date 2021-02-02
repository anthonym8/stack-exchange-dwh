"""Parses XML files and saves as CSV files"""


def parse_raw_xml(input_file, output_file):
    """Parses a StackExchange XML data dump file and saves as CSV.
    
    Parameters
    ----------
    input_file : str
        The path to the raw XML file to transform.
        
    output_file : str
        The path to the transformed CSV file
        
    Returns
    -------
    columns : list
        A list of column names of the parsed data.
    
    """

    import xml.etree.ElementTree as ET
    import pandas as pd
    from csv import QUOTE_NONNUMERIC
    from src.utils.misc import prepare_directory
    
    print('Parsing:\n    Source:  {}'.format(input_file))
    
    # Parse XML, convert to DataFrame
    xml = ET.parse(input_file)
    rows = [x.attrib for x in xml.getroot().getchildren()]
    df = pd.DataFrame(rows)

    # Save to file
    prepare_directory(output_file)
    df.to_csv(output_file, index=False, quoting=QUOTE_NONNUMERIC)
    
    print('    Sink:    {}\n'.format(output_file))
    
    return df.columns.tolist()


def transform_dataset(dataset):
    """Parses all XML files related to a dataset and saves to CSV files.
    
    Parameters
    ----------
    dataset : str
        The name of the StackExchange site whose data you want to transform.
        
    Returns
    -------
    None
    
    """

    import os
    import json
    from src.utils.misc import camel_to_snake_case, prepare_directory
    
    root = os.getcwd()
        
    xml_folder = '{}/data/interim/{}'.format(root, dataset)
    xml_files = [x for x in os.listdir(xml_folder) if x.endswith('.xml')]
    metadata = {camel_to_snake_case(x.replace('.xml','')):{'source':x} for x in xml_files}
    
    for t in metadata.keys():
        
        input_file = '{}/data/interim/{}/{}'.format(root, dataset, metadata[t]['source'])
        output_file = '{}/data/processed/{}/{}.csv'.format(root, dataset, t)
        
        columns = parse_raw_xml(input_file, output_file)
        metadata[t]['raw'] = input_file
        metadata[t]['csv'] = output_file
        metadata[t]['columns'] = list(map(camel_to_snake_case, columns))
        
    # Save metadata
    metadata_file = '{}/data/metadata/{}.json'.format(root, dataset)
    prepare_directory(metadata_file)
    json.dump(metadata, open(metadata_file, 'w'))
        

if __name__ == '__main__':
    
    dataset = input()
    transform_dataset(dataset)