from iteration import generate_sequence
test_cube = pc.Cube()
actions = []
for i in range(3):
    actions.append(r.choice(list(action_map.keys())))
formula = pc.Formula(actions)
test_cube(formula)
total_steps = 0
print(test_cube)
print("after solving")
while total_steps < 6 and cube_completeness(test_cube) < 1:
    best_move = "U"
    max_value = 0
    for move in action_map.keys():
        init_cube = test_cube.copy()
        init_cube(move)
        if flatten_string(init_cube) in cube_reward and cube_reward[flatten_string(init_cube)] > max_value:
            best_move = move
            max_value = cube_reward[flatten_string(init_cube)]
    test_cube(best_move)
    total_steps += 1
print(test_cube)
print(total_steps)
print(cube_completeness(test_cube))
