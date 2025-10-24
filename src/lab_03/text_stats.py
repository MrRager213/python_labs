import sys
from ..lib.text import normalize
from src.lib.table import print_summary


def main():

     """
     echo "Привет, мир! Привет!!!" | python -m src.lab_03.text_stats
     """

     print("text", sys.stdin.read(), sys.stdin.readline(), sys.stdin.readlines())

     IS_TABLE = True
     print_summary(text=sys.stdin.read(), is_table=IS_TABLE)


if __name__ == "__main__":
    main()