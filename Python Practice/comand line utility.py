import argparse
import sys

def calc(args):
    if args.o == "add":
        return args.x + args.y
    elif args.o == "minus":
        return args.x - args.y
    elif args.o == "multiply":
        return args.x * args.y
    elif args.o == "divide":
        return args.x / args.y
    else:
        return"somethig went wrond"



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--x",type=float,default = 1.0,
                        help = "enter firstnumber. for more info contact @akshay_dhumda_07 on instagram")

    parser.add_argument("--y",type=float,default = 3.0,
                        help="enter firstnumber. for more info contact @akshay_dhumda_07 on instagram")


    parser.add_argument("--o",type=str,default = "add",
                        help="enter firstnumber. for more info contact @akshay_dhumda_07 on instagram")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))