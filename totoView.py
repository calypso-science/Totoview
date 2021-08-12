#!/usr/bin/python3
from __future__ import absolute_import
import sys


def main(filenames=[],reader=None,dataframes=None):
    import totoview
    totoview.show(filenames=filenames,dataframe=dataframes,reader=reader)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog='totoView.py', usage='%(prog)s file1.txt [options]')
    ## main arguments
    parser.add_argument('files', type=str,nargs='+',default=None,help='name of the files to read')
    ## options
    parser.add_argument('--reader','-r',type=str,default=None,help='name of the reader to use')

    args = parser.parse_args()
    main(filenames=args.files,reader=args.reader)