from project_euler.problems import *

for i in range(1, 10):
    if i < 10:
        problem_str = f"problem0{i}.problem0{i}()"
    else:
        problem_str = f"problem{i}.problem{i}()"
    eval(problem_str)
