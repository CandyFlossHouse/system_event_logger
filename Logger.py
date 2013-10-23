# coding=utf-8
'''
Created on 2013-10-22

@author: maisonwan
'''
from Arguments import LoadArgument
import sys

if __name__ == '__main__':
    load = LoadArgument()
    try:
        args = load.parse_argv(sys.argv)
    except:
        sys.exit(-1)
    finally:
        load.__del__()