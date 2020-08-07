import pycuber as pc
import random as r
from cube_utilities import action_map, flatten_string, cube_completeness


def scramble():
    cube = pc.Cube()
    actions = []
    for i in range(3):
        actions.append(r.choice(list(action_map.keys())))
    formula = pc.Formula(actions)
    cube(formula)
    return cube, formula


def solve(cube, reward):
    steps = 0
    actions = []
    while steps < 6 and cube_completeness(cube) < 1:
        best_move = list(action_map.keys())
        max_value = 0
        for move in action_map.keys():
            init_cube = cube.copy()
            init_cube(move)
            if flatten_string(init_cube) in reward:
                if reward[flatten_string(init_cube)] > max_value:
                    best_move = [move]
                    max_value = reward[flatten_string(init_cube)]
                elif reward[flatten_string(init_cube)] > max_value:
                    best_move.append(move)
        act = r.choice(best_move)
        cube(act)
        actions.append(act)
        steps += 1
    return cube, steps, actions
