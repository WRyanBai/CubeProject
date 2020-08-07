import math
import pycuber as pc
import random as r
from tqdm import tqdm
from cube_utilities import action_map, flatten_string, cube_completeness


def generate_sequence(prob = 100, reward = {}):
    # prob is the probability that we will solve the cube by reversing the actions which scrambled it
    # prob is 100 by default
    scrambled_cube = pc.Cube()
    actions = []
    states_cube_list = []
    value_list = []
    # The following lines scrambles the cubes using 3 actions
    for i in range(3):
        actions.append(r.choice(list(action_map.keys())))
    formula = pc.Formula(actions)
    scrambled_cube(formula)
    # The following loop tries to solve the scrambled cube 10 times
    for i in range(10):
        # cube is a copy of the scrambled_cube
        # the scrambled state is being kept in scrambled_cube while cube is being solved
        cube = scrambled_cube.copy()
        total_steps = 0
        random_number = r.randint(0, 100)
        if random_number <= prob:
            # The following code solves the cube by reversing the actions that it was scrambled with
            formula.reverse()
            for k, move in enumerate(formula):
                states_cube_list.append(cube.copy())
                cube(move)
                total_steps += 1
        else:
            while total_steps < 6 and cube_completeness(cube) < 1:
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
                states_cube_list.append(cube.copy())
                cube(r.choice(best_move))
                total_steps += 1
        final_reward = 100 * (cube_completeness(cube) == 1) - 5 * total_steps
        for step, state in enumerate(states_cube_list):
            value = final_reward * math.pow(0.9, step + 1)
            value_list.append(value)
    return states_cube_list, value_list


def training (iterations = 100):
    reward = {}
    cube_count = {}
    cubes = []
    values = []
    prob = 100
    for j in tqdm(range(iterations)):
        _cubes, _values = generate_sequence(prob, reward)
        cubes.extend(_cubes)
        values.extend(_values)
        prob = int(prob * 0.9)
    for j in range(len(cubes)):
        if flatten_string(cubes[j - 1]) in cube_count:
            cube_count[flatten_string(cubes[j - 1])] += 1
            q = reward[flatten_string(cubes[j - 1])]
            n = cube_count[flatten_string(cubes[j - 1])]
            reward[flatten_string(cubes[j - 1])] = (q * (n - 1) + values[j - 1]) / n
        else:
            cube_count[flatten_string(cubes[j - 1])] = 1
            reward[flatten_string(cubes[j - 1])] = values[j - 1]
    reward[flatten_string(pc.Cube())] = 100
    return reward
