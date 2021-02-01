"""Downloads the Stack Exchange data dump from the Internet Archive"""

if __name__ == '__main__':

    import os
    
    dataset = 'datascience.meta.stackexchange.com'
    
    # Download file
    os.chdir('data/raw')
    url = 'https://archive.org/download/stackexchange/{}.7z'.format(dataset)
    command = 'wget -O {}.7z {}'.format(dataset, url)
    os.system(command)
    
    # Decompress file
    command = '7z x {0}.7z -o../interim/{0}/ -aoa'.format(dataset)
    os.system(command)