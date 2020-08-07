from iteration import training
from solving import scramble, solve
from cube_utilities import cube_completeness
import pycuber as pc


cube_reward = training(10)
scrambled_cube, scramble_steps = scramble()
print("scrambled cube")
print(scrambled_cube)
print("formula used to scramble cube:")
print(scramble_steps)
solved_cube, total_steps, actions = solve(scrambled_cube, cube_reward)
print("after solving")
print(solved_cube)
print("number of steps taken " + str(total_steps))
print("actions taken to solve cube: ")
print(pc.Formula(actions))
print("Completeness of cube: " + str(cube_completeness(solved_cube)))
