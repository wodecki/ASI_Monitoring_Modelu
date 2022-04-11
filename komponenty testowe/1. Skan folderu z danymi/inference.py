import argparse
import os
import sys

def go(args):
    print("... Initiating inference ...")
    print("... processing ...", args.dataset)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Initiate inference pipeline.')
    parser.add_argument('--dataset', type=str, default='./data/batch 1.csv', help='Path to dataset.')
    args = parser.parse_args()
    go(args)

# to call from CLI type e.g.: $ python inference.py --dataset "./data/batch 1.csv" 