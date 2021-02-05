"""End-to-end ETL pipeline."""


from src.data.extract import extract
from src.data.transform import transform_dataset
from src.data.load import load_dataset, write_sql_statements


def run_default_pipeline(dataset):
    """Executes the entire ETL pipeline."""
    
    print('Extracting data: {}'.format(dataset.upper()))
    extract(dataset)
    
    print('Transforming data: {}'.format(dataset.upper()))
    transform_dataset(dataset)
    
    print('Loading data to database: {}'.format(dataset.upper()))
    load_dataset(dataset)
    
    
def run_docker_pipeline(dataset):
    """Executes the entire ETL pipeline for building the docker image"""
    
    print('Extracting data: {}'.format(dataset.upper()))
    extract(dataset)
    
    print('Transforming data: {}'.format(dataset.upper()))
    transform_dataset(dataset)
    
    print('Loading data to database: {}'.format(dataset.upper()))
    write_sql_statements(dataset)

    
if __name__ == '__main__':
    
    import os
    import argparse
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(prog='etl')
    parser.add_argument('--dataset', action='store', required=True, help='The dataset to ETL')
    parser.add_argument('--pipeline', action='store', required=True, help='The ETL pipeline to execute, e.g. default, docker')
    args = parser.parse_args()

    
    # Ensure that script is executed in the correct directory
    cwd = os.getcwd()
    assert cwd.split('/')[-1] == 'stack-exchange-dwh', 'Script was executed in the wrong directory: {}.'.format(cwd)
    
    
    # Check if the pipeline argument is valid
    assert args.pipeline in ['default','docker'], 'Invalid pipeline argument specified: {}'.format(args.pipeline)
    
    
    # Run pipeline
    if args.pipeline == 'default':
        run_default_pipeline(dataset=args.dataset)
        
    elif args.pipeline == 'docker':
        run_docker_pipeline(dataset=args.dataset)
        