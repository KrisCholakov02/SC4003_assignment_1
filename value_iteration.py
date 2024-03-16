from config import *
from utils import *
import pandas as pd


# Function to initialize the value iteration maze environment
def init_vi_grid():
    vi_env = [[0 for _ in range(GRID_SIZE_W)] for _ in range(GRID_SIZE_H)]
    return vi_env


# Function to calculate the utility of the next state based on the current state and action
def next_state_utility(vi_env, s, a):
    # Check if the current state is a wall
    if s in walls:
        return vi_env[s[1]][s[0]]

    # Calculate the next state based on the action
    new_x, new_y = s
    new_x += actions[a][0]
    new_y += actions[a][1]

    # Check if the next state is a wall or out of bounds
    if (new_x, new_y) in walls or new_x < 0 or new_x >= GRID_SIZE_W or new_y < 0 or new_y >= GRID_SIZE_H:
        return vi_env[s[1]][s[0]]
    else:
        return vi_env[new_y][new_x]


# Function to calculate the expected utility of taking action 'a' in state 's'
def expected_utility(vi_env, s, a, U):
    x, y = s
    exp_utility = 0
    for action, prob in transition_model(a).items():
        exp_utility += prob * next_state_utility(vi_env, s, action)
    return exp_utility


# Function for the Bellman equation
def bellman_equation(vi_env, s):
    reward = 0
    if s in rewards:
        reward = rewards[s]
    elif s in holes:
        reward = holes[s]
    elif s in walls:
        reward = 0
    else:
        reward = EMPTY_REWARD

    max_utility = float('-inf')
    best_action = None
    for action in actions:
        utility = expected_utility(vi_env, s, action, vi_env)
        if utility > max_utility:
            max_utility = utility
            best_action = action

    return (reward + DISCOUNT_FACTOR * max_utility), best_action


# Function to perform value iteration and save the results to a CSV file using pandas
def value_iteration(vi_env):
    iteration_cnt = 0
    while True:
        iteration_cnt += 1
        new_vi_env = copy_env(vi_env)
        error = 0
        for y in range(GRID_SIZE_H):
            for x in range(GRID_SIZE_W):
                max_utility, best_action = bellman_equation(vi_env, (x, y))
                new_vi_env[y][x] = max_utility
                error = max(error, abs(max_utility - vi_env[y][x]))

        vi_env = new_vi_env
        if error < SMALL_ENOUGH * (1 - DISCOUNT_FACTOR) / DISCOUNT_FACTOR:
            break

    return vi_env, iteration_cnt


# Function to generate the optimal policy based on the value iteration results
def generate_policy(vi_env):
    policy = [[None for _ in range(GRID_SIZE_W)] for _ in range(GRID_SIZE_H)]
    for y in range(GRID_SIZE_H):
        for x in range(GRID_SIZE_W):
            max_utility = float('-inf')
            best_action = None
            for action in actions:
                utility = expected_utility(vi_env, (x, y), action, vi_env)
                if utility > max_utility:
                    max_utility = utility
                    best_action = action
            policy[y][x] = best_action
    return policy
