import keras.backend as K
import numpy as np
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras.layers import Dense, Input, LeakyReLU
from keras.models import Model
from keras.optimizers import Adam
from tqdm import tqdm
from utils import action_map_small, gen_sequence, get_all_possible_actions_cube_small, chunker, \
    flatten_1d_b

for i in range (1):
    cubes = []
    distance_to_solved = []
    cube_reward = {}
    for j in tqdm(range(10)):    
        _cubes, _distance_to_solved = gen_sequence(3)
        cubes.extend(_cubes)
        distance_to_solved.extend(_distance_to_solved)

    #cube_distance = zip(cubes,distance_to_solved)   
    state_reward = []   

    for c in tqdm(distance_to_solved):
        rewards = (100 - distance_to_solve[0])*(1-(0.1*int(c)))
        state_reward.append(rewards)   #每一state的reward

    for i in range(len(cubes)):
        cube_reward[cubes[i-1]] = state_reward[i-1]
                                                
