# prints out a multiplication table

import argparse

DEFAULT_ROW_LOWER = 0
DEFAULT_ROW_UPPER = 9
DEFAULT_COLUMN_LOWER = 0
DEFAULT_COLUMN_UPPER = 9

HELP_ROW_LOWER = 'row lower-bound value: default ' + str(DEFAULT_ROW_LOWER)
HELP_ROW_UPPER = 'row upper-bound value: default ' + str(DEFAULT_ROW_UPPER)
HELP_COLUMN_LOWER = 'column lower-bound value: default ' + str(DEFAULT_COLUMN_LOWER)
HELP_COLUMN_UPPER = 'column upper-bound value: default ' + str(DEFAULT_COLUMN_UPPER)

parser = argparse.ArgumentParser(description='multiplication table')

parser.add_argument('--row_lower', help=HELP_ROW_LOWER)
parser.add_argument('--row_upper', help=HELP_ROW_UPPER)
parser.add_argument('--column_lower', help=HELP_COLUMN_LOWER)
parser.add_argument('--column_upper', help=HELP_COLUMN_UPPER)

args = parser.parse_args()

row_lower = int(args.row_lower) if args.row_lower else DEFAULT_ROW_LOWER
row_upper = int(args.row_upper) if args.row_upper else DEFAULT_ROW_UPPER
column_lower = int(args.column_lower) if args.column_lower else DEFAULT_COLUMN_LOWER
column_upper = int(args.column_upper) if args.column_upper else DEFAULT_COLUMN_UPPER

width = len(str(row_upper*column_upper)) + 2

for i in range(row_lower, row_upper+1):
    for j in range(column_lower, column_upper+1):
        print(str(i*j).rjust(width), end='')
    print()
