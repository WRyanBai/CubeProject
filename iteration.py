import keras.backend as K
import numpy as np
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras.layers import Dense, Input, LeakyReLU
from keras.models import Model
from keras.optimizers import Adam
from tqdm import tqdm
from cube_utilities import action_map, generate_sequence, flatten_string

for i in range(1):
    cubes = []
    distance_to_solved = []
    cube_reward = {}
    for j in tqdm(range(10)):
        _cubes, _distance_to_solved = generate_sequence(3)
        cubes.extend(_cubes)
        distance_to_solved.extend(_distance_to_solved)

    # cube_distance = zip(cubes,distance_to_solved)
    state_reward = []

    for c in tqdm(distance_to_solved):
        rewards = (100 - distance_to_solved[0]) * (1 - (0.1 * int(c)))
        state_reward.append(rewards)  # 每一state的reward

    for i in range(len(cubes)):
        # if the state is already in cube_reward, its value in cube_reward will be the greater value
        if flatten_string(cubes[i - 1]) in cube_reward:
            if state_reward[i - 1] > cube_reward[flatten_string(cubes[i - 1])]:
                cube_reward[flatten_string(cubes[i - 1])] = state_reward[i - 1]
        else:
            cube_reward[flatten_string(cubes[i - 1])] = state_reward[i - 1]
