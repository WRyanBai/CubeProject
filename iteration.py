import pycuber as pc
import random as r
from tqdm import tqdm
from cube_utilities import action_map, flatten_string


def generate_sequence(prob = 100):
    # prob is the probability that we will solve the cube by reversing the actions which scrambled it
    # prob is 100 by default
    scrambled_cube = pc.Cube()
    actions = []
    states_cube_list = []
    distance_list = []
    state_reward=[]
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
        random_number = r.randint(0, 100)
        if random_number <= prob:
            # The following code solves the cube by reversing the actions that it was scrambled with
            formula.reverse()
            for k, s in enumerate(formula):
                # k is the current number of actions taken to solve the cube
                # e.g after performing one action on cube, k is 0. after two actions it is 1
                states_cube_list.append(cube.copy())
                distance_list.append(3 - k)
                ##reward=##write reward formula here
                ##state_reward.append(reward)
                cube(s)
            return states_cube_list, distance_list,state_reward
        else:
            update_cube=cube.copy() #update_cube is the updates every step and keeps track of the best moves
            for i in range(3):
                best_move="U"
                max_score=0
                for move in possible_actions:
                    init_cube=update_cube.copy()
                    init_cube(move)
                    if(flatten_string(init_cube) in cube_reward):
                        if(cube_reward([flatten_string(init_cube)])>max_score):
                            best_move=move
                states_cube_list.append(update_cube.copy())
                distance_list.append(3-move)
                update_cube(best_move)
            return states_cube_list,distance_list,state_reward


for i in range(1):
    cubes = []
    distance_to_solved = []
    cube_reward = {}
    for j in tqdm(range(10)):
        _cubes, _distance_to_solved,_state_reward = generate_sequence()
        cubes.extend(_cubes)
        distance_to_solved.extend(_distance_to_solved)
    state_reward = []
    state_reward.append(_state_reward)
    ##
    ##for c in tqdm(distance_to_solved):
    ##   rewards = (100 - distance_to_solved[0]) * (1 - (0.1 * int(c)))
    ##    state_reward.append(rewards)  # 每一state的reward

    for j in range(len(cubes)):
        # if the state is already in cube_reward, its value in cube_reward will be the greater value
        if flatten_string(cubes[j - 1]) in cube_reward:
            if state_reward[j - 1] > cube_reward[flatten_string(cubes[j - 1])]:
                cube_reward[flatten_string(cubes[j - 1])] = state_reward[j - 1]
        else:
            cube_reward[flatten_string(cubes[j - 1])] = state_reward[j - 1]
