from collections import Counter
from random import choice

import numpy as np
import pycuber as pc

action_map = {'F': 0, 'B': 1, 'U': 2, 'D': 3, 'L': 4, 'R': 5,
              "F'": 6, "B'": 7, "U'": 8, "D'": 9, "L'": 10, "R'": 11}
color_short_map = {'green': 'g', 'blue': 'b', 'yellow': 'y', 'red': 'r', 'orange': 'o', 'white': 'w'}


def flatten(cube):
    # this method returns a list of the color of every square in a cube
    sides = [cube.F, cube.B, cube.U, cube.D, cube.L, cube.R]
    flat_cube = []
    for s in sides:
        for i in range(3):
            for j in range(3):
                flat_cube.append(s[i][j].colour)
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
        distance_list.append(steps - i)
        cube(s)
        i += 1
    return actions_list, states_cube_list, distance_list


def generate_sequence(steps=3):
    # this method generates samples of a cube that is randomly scrambled for a number of steps, default 3 steps
    # returns a list of the state, flattened state, action, and distance from solved for the cube at each step
    cube = pc.Cube()
    actions = []
    for i in range(steps):
        actions.append(choice(list(action_map.keys())))
    formula = pc.Formula(actions)
    cube(formula)
    formula.reverse()

    states_cube_list = []
    distance_list = []
    i = 0
    for s in formula:
        states_cube_list.append(cube.copy())
        distance_list.append(steps - i)
        cube(s)
        i += 1
    return states_cube_list, distance_list


def flatten_string(cube):
    # this method returns a list of the color of every square in a cube
    sides = [cube.F, cube.B, cube.U, cube.D, cube.L, cube.R]
    flat_cube = ""
    for s in sides:
        for i in range(3):
            for j in range(3):
                flat_cube = flat_cube + color_short_map[s[i][j].colour]
    return flat_cube
