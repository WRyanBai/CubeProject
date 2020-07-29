from collections import Counter
from random import choice

import numpy as np
import pycuber as pc

action_map = {'F': 0, 'B': 1, 'U': 2, 'D': 3, 'L': 4, 'R': 5,
              "F'": 6, "B'": 7, "U'": 8, "D'": 9, "L'": 10, "R'": 11}
color_list_map = {'green': [1, 0, 0, 0, 0, 0], 'blue': [0, 1, 0, 0, 0, 0], 'yellow': [0, 0, 1, 0, 0, 0],
                  'red': [0, 0, 0, 1, 0, 0], 'orange': [0, 0, 0, 0, 1, 0], 'white': [0, 0, 0, 0, 0, 1]}


def flatten(cube):
    # this method returns a list of the color of every square in a cube
    sides = [cube.F, cube.B, cube.U, cube.D, cube.L, cube.R]
    flat_cube = []
    for s in sides:
        for i in range(3):
            for j in range(3):
                flat_cube.append(s[i][j].colour)
    return flat_cube


def flatten_1d(cube):
    # this method returns a list of the color of every square in a cube, but the color is a list(see color_list_map)
    sides = [cube.F, cube.B, cube.U, cube.D, cube.L, cube.R]
    flat_cube = []
    for s in sides:
        for i in range(3):
            for j in range(3):
                flat_cube.extend(color_list_map[s[i][j].colour])
    return flat_cube


def side_completeness(side):
    # this method determines how complete a side is. A 1 would mean that it is complete
    count = Counter()
    count.update(side)
    completeness = []
    for c in count.values():
        completeness.append(c / 9)
    return max(completeness)


def cube_completeness(cube):
    # this method determines how complete a cube is. A 1 would mean that it is complete
    flat_cube = flatten(cube)
    completeness = []
    for i in range(0, 36, 9):
        completeness.append(side_completeness((flat_cube[i:i + 9])))
    return np.mean(completeness)


def generate_sample(steps=3):
    # this method generates samples of a cube that is randomly scrambled for a number of steps, default 3 steps
    # returns a list of the state, flattened state, action, and distance from solved for the cube at each step
    cube = pc.Cube()
    actions = []
    for i in range(steps):
        actions.append(choice(list(action_map.keys())))
    formula = pc.Formula(actions)
    cube(formula)
    formula.reverse()

    actions_list = []
    states_cube_list = []
    states_1d_list = []
    distance_list = []
    i = 0
    for s in formula:
        actions_list.append(s)
        states_cube_list.append(cube.copy())
        states_1d_list.append(flatten_1d(cube))
        distance_list.append(steps - i)
        cube(s)
        i += 1
    return actions_list, states_cube_list, states_1d_list, distance_list