'''Vanalyzer

Usage:
    vanalyze.py --i <input> [--c <config>] [--o <output>]

Options:
    -h --help    Show this screen
    --version    Show version.
    --i <input>  Provide input file
    --c <config> Provide config file
    --o <output> Provide output file [default: va.out]
    

Created on 28 paü 2017
@author: Marcin Stec
'''
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Vanalyzer 0.1')
    print(arguments)