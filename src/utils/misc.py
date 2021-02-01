"""Misc helper functions"""

# Author: Rey Anthony Masilang <rey.masilang@gmail.app>


import os


def prepare_directory(filename):
    """Creates a directory if it doesn't exist yet."""
    directory = '/'.join(filename.split('/')[:-1])
    if not os.path.exists(directory):
        os.makedirs(directory)


def cleanup_local(files=[]):
    """Deletes files in local machine.
    
    Parameters
    ----------
    files : list
        A list of interim local files to remove from the local filesystem.
        
    Returns
    -------
    None
    
    """
    
    # Delete local files
    for filename in files:
        try:
            os.remove(filename)
            print('Deleted local file: {}'.format(filename))
        except:
            print('File {} does not exist. Skipping'.format(filename))
