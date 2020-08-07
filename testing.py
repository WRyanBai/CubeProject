from tqdm import tqdm
from cube_utilities import cube_completeness
from iteration import training, cube_reward
from demo import scramble, solve


def percent_solved(iterations):
    training(iterations)
    solved_times = 0
    for i in tqdm(range(100)):
        scrambled_cube = scramble()
        solved_cube = solve(scrambled_cube)
        if cube_completeness(solved_cube[0]) == 1:
            solved_times += 1
    print("after " + str(iterations) + " training iterations")
    print(str(solved_times) + " cubes were solved out of 100")


percent_solved(10)
percent_solved(50)
percent_solved(100)
