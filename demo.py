import pycuber as pc
import random as r
from cube_utilities import action_map, flatten_string, cube_completeness
from iteration import cube_reward, training

def scramble():
    cube = pc.Cube()
    actions = []
    for i in range(3):
        actions.append(r.choice(list(action_map.keys())))
    formula = pc.Formula(actions)
    cube(formula)
    return cube


def solve(cube):
    steps = 0
    while steps < 6 and cube_completeness(cube) < 1:
        best_move = list(action_map.keys())
        max_value = 0
        for move in action_map.keys():
            init_cube = cube.copy()
            init_cube(move)
            if flatten_string(init_cube) in cube_reward:
                if cube_reward[flatten_string(init_cube)] > max_value:
                    best_move = [move]
                    max_value = cube_reward[flatten_string(init_cube)]
                elif cube_reward[flatten_string(init_cube)] > max_value:
                    best_move.append(move)
        cube(r.choice(best_move))
        steps += 1
    return cube, steps


'''training(10)
scrambled_cube = scramble()
print(scrambled_cube)
print("after solving")
solved_cube, total_steps = solve(scrambled_cube)
print(solved_cube)
print(total_steps)
print(cube_completeness(solved_cube))'''
