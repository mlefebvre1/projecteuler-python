#!/usr/bin/env python3

import project_euler
from project_euler.utils.timeit import timeit

import argparse
import sys


@timeit
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--problem", type=int, help="Specify which problem number you want to run"
    )
    args = parser.parse_args()
    if args.problem is not None:
        problem = f"problem{args.problem if args.problem > 9 else f'0{args.problem}'}"
        eval(f"project_euler.problems.{problem}.{problem}()")
    else:
        for problem in project_euler.problems.__all__:
            eval(f"project_euler.problems.{problem}.{problem}()")
    return 0


"""
for i in range(1, 10):
    if i < 10:
        problem_str = f"problem0{i}.problem0{i}()"
    else:
        problem_str = f"problem{i}.problem{i}()"
    eval(problem_str)
"""
if __name__ == "__main__":
    sys.exit(main())
