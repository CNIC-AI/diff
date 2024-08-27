import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Process two folder paths.")

    parser.add_argument("dir_1", type=str)
    parser.add_argument("dir_2", type=str)

    args = parser.parse_args()
    # TODO:

    return args
