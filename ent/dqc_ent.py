import argparse
import pandas as pd

from dqc import dqc_rules

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file_path" , type=str, help="define file path")
parser.add_argument("-r", "--checking_rule" , type=str, help="define checking rules")
args_parser = parser.parse_args()



if __name__ == "__main__":
    pdf = pd.read_csv(args_parser.file_path)
    dqc_func =  getattr(dqc_rules, "check_dq_"  + args_parser.checking_rule)
    print(dqc_func(pdf))