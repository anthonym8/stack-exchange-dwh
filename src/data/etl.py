"""End-to-end ETL pipeline."""


from extract import extract
from transform import transform_dataset
from load import load_dataset


def run_pipeline(dataset):
    """Executes the entire ETL pipeline."""
    
    print('Extracting data: {}'.format(dataset.upper()))
    extract(dataset)
    
    print('Transforming data: {}'.format(dataset.upper()))
    transform_dataset(dataset)
    
    print('Loading data to database: {}'.format(dataset.upper()))
    load_dataset(dataset)


if __name__ == '__main__':
    
    import os
    
    # Ensure that script is executed in the correct directory
    cwd = os.getcwd()
    assert cwd.split('/')[-1] == 'stack-exchange-dwh', 'Script was executed in the wrong directory: {}.'.format(cwd)
    
    run_pipeline(input())