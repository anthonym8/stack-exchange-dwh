"""Downloads the Stack Exchange data dump from the Internet Archive"""


def extract(dataset):
    """Downloads files from archive.org, decompresses file from 7z archive.
    
    Parameters
    ----------
    dataset : str
        The name of the StackExchange site whose data you want to extract.
        
    Returns
    -------
    None
    
    """
    
    import os
        
    raw_file = '{}.stackexchange.com.7z'.format(dataset)
    source_url = 'https://archive.org/download/stackexchange/{}'.format(raw_file)
    
    # Download file
    command = 'wget -O data/raw/{} {}'.format(raw_file, source_url)
    retval = os.system(command)
    assert retval==0, 'Failed to download files. Check logs.'
    
    # Decompress file
    command = '7z x data/raw/{} -odata/interim/{}/ -aoa'.format(raw_file, dataset)
    retval = os.system(command)
    assert retval==0, 'Failed to unzip files. Check logs.'
    

if __name__ == '__main__':
    
    dataset = input()
    extract(dataset)