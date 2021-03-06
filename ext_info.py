"""
#!/user/bin/python3

a command line program that shows information about different file types
in a specified folder.
"""

# import sys
import argparse
from pathlib import Path
from collections import defaultdict


def create_folder_data():
    ''' default values for ifiles data dict
    '''
    return {
        'num of files': 0,
        'total size': 0,
    }


def gather_info_from_folder(path):
    ''' look for files in path supplied and build dict where extensions are keys
        and values are number of files and total sizes of files with extension
        the dict is returned
    '''
    folder = Path(path)
    files_data_by_ext = defaultdict(create_folder_data)
    for p in folder.iterdir():
        if not p.is_dir():
            # use a dot for empty suffix
            if p.suffix == '':
                suffix = '.'
            else:
                suffix = p.suffix
            files_data_by_ext[suffix]['num of files'] += 1
            files_data_by_ext[suffix]['total size'] += p.stat().st_size
    return files_data_by_ext


def display_files_data_sorted_by_ext(files_data_by_ext):
    ''' display data  from dict received
    '''
    keys = list(files_data_by_ext.keys())
    keys.sort()
    for k in keys:
        print(k,
              files_data_by_ext[k]['num of files'],
              files_data_by_ext[k]['total size'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''displays number of files and total size of files
                    per extension in the specified path.''')
    parser.add_argument('path', metavar='path',
                        help='name of folder to scan')

    args = parser.parse_args()
    files_data_by_ext = gather_info_from_folder(args.path)
    display_files_data_sorted_by_ext(files_data_by_ext)
