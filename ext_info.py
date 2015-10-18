"""
#!/user/bin/python3

a command line program that shows information about different file types
in a specified folder.
"""

# import sys
import argparse
from pathlib import Path


def gather_info_from_folder(path):
    folder = Path(path)
    for p in folder.iterdir():
        if not p.is_dir():
            print(p, p.is_dir(), p.is_file(), p.stat().st_size, p.suffix)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''displays number of files and total size of files
                    per extension in the specified path.''')
    parser.add_argument('path', metavar='path',
                        help='name of folder to scan')

    args = parser.parse_args()
    print("args.path:", args.path)
    print()
    gather_info_from_folder(args.path)
