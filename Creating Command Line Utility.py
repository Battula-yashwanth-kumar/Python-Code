# # pythonUtlility.py
# A command line utility is a way of giving operating system instruction using line of text.
# command line programs operate via the command line or powershell.It will interact with a command -line script
# python comes with several differernt libraries that allows us to write a command line interface for our scripts, but the standards way for creating a CLI  in python is by using argparse Module
# import the python argparse Module
# create the parser
# add optional and positional arguments to the parser
# execute .parse_args()
# python provides the sys module that gives us independence from the host machine operating system and allows us to operate  an on underlying interpreter irrespective of its being linux or windows platform

import argparse
import sys

def calc(args):
    if args.o=='add':
        return args.x+args.y;
    elif args.o=='mul':
        return args.x*args.y;
    elif args.o=='div':
        return args.x/args.y
    elif args.o=='sub':
        return args.x-args.y
    else:
        return "Something went wrong"
    
    if __name__=='__main__':
        parser=argparse.ArgumentParser()
        parser.add_argument('--x',type==float,default=1.0,help="Enter first number")
        parser.add_argument('--y',type=float,default=3.0,help="Enter second number")
        parser.add_argument('--o',type==str,default='add',help="This a utility of calculation")
        args=parser.parse_args()
        sys.stdout.write(str(calc(args)))


        #to run

        # cd .\pythontyts\
        # python .\pythonUtility.py --x 7 --y 8 --o div
        # >>> 0.875
