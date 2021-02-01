"""Parses XML files and saves as CSV files"""

if __name__ == '__main__':
    
    import xml.etree.ElementTree as ET
    import pandas as pd
    from csv import QUOTE_NONNUMERIC
    from src.utils.misc import prepare_directory
    
    dataset = 'datascience.meta.stackexchange.com'
    
    tables = [
        'Badges',
        'Comments',
        'PostHistory',
        'PostLinks',
        'Posts',
        'Tags',
        'Users',
        'Votes'
    ]
    
    for t in tables:
        input_file = 'data/interim/{}/{}.xml'.format(dataset, t)
        output_file = 'data/processed/{}/{}.csv'.format(dataset, t)

        xml = ET.parse(input_file)
        rows = [x.attrib for x in xml.getroot().getchildren()]
        df = pd.DataFrame(rows)

        # Save to file
        prepare_directory(output_file)
        df.to_csv(output_file, index=False, quoting=QUOTE_NONNUMERIC)
