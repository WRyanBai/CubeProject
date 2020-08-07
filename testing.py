from tqdm import tqdm
from cube_utilities import cube_completeness
from iteration import training
from solving import scramble, solve


def percent_solved(iterations):
    cube_reward = training(iterations)
    solved_times = 0
    for i in tqdm(range(100)):
        scrambled_cube = scramble()[0]
        solved_cube = solve(scrambled_cube, cube_reward)[0]
        if cube_completeness(solved_cube) == 1:
            solved_times += 1
    print("after " + str(iterations) + " training iterations")
    print(str(solved_times) + " cubes were solved out of 100")


percent_solved(10)
percent_solved(30)
percent_solved(50)
percent_solved(100)
percent_solved(200)
