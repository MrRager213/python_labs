import sys
from src.lib.table import print_summary


def main():
     IS_TABLE = True
     print_summary(text=sys.stdin.read(), is_table=IS_TABLE)


if __name__ == "__main__":
    main()