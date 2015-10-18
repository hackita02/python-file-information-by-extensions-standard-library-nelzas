"""
#!/user/bin/python3

a command line program that shows information about different file types
in a specified folder.
"""

# import sys
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''displays number of files and total size of files
                    per extension in the specified path.''')
    parser.add_argument('path', metavar='path',
                        help='name of folder to scan')

    args = parser.parse_args()
    print(args.path)
