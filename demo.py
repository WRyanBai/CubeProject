from iteration import training
from solving import scramble, solve
from cube_utilities import cube_completeness
import pycuber as pc


cube_reward = training(10)
scrambled_cube = scramble()
print("scrambled cube")
solved_cube, total_steps, actions = solve(scrambled_cube, cube_reward)
print(scrambled_cube)
print("after solving")
print(solved_cube)
print("number of steps taken " + str(total_steps))
print("actions taken to solve cube: ")
print(pc.Formula(actions))
print("Completeness of cube: " + str(cube_completeness(solved_cube)))
