from config import *
from utils import *
import pandas as pd
from algorithms.algorithm_utils import *
from grid import *


# Function to initialize the value iteration maze environment
def init_vi_env():
    # Create a GRID_SIZE_H x GRID_SIZE_W grid matrix filled with zeros
    vi_env = [[0 for _ in range(GRID_SIZE_W)] for _ in range(GRID_SIZE_H)]
    return vi_env


# Function for the Bellman equation used for value iteration
# Bellman equation: U_(i+1)(s) = R(s) + γ * max_(a ∈ A(s)) ∑_(s′) P(s′ | s, a) * U_i(s′)
def bellman_equation_vi(vi_env, s):
    # Check if the current state is a reward, hole, wall or empty field and assign the corresponding reward
    if s in REWARDS:  # If the current state is a reward
        reward = REWARDS[s]
    elif s in HOLES:  # If the current state is a hole
        reward = HOLES[s]
    elif s in WALLS:  #
        reward = 0
    else:  # If the current state is an empty field
        reward = EMPTY_REWARD

    # Defining the maximum utility --> max_(a ∈ A(s)) ∑_(s′) P(s′ | s, a) * U_i(s′)
    max_utility = float('-inf')
    # Defining the best action --> argmax_(a ∈ A(s)) ∑_(s′) P(s′ | s, a) * U_i(s′)
    best_action = None
    # Loop through all possible actions
    for action in ACTIONS:
        # Calculate the expected utility of taking action the current action in the current state
        utility = expected_utility(vi_env, s, action)
        # If the utility is greater than the maximum utility, update the maximum utility and the best action
        if utility > max_utility:
            max_utility = utility
            best_action = action

    # Return the Bellman equation result and the best action
    return (reward + DISCOUNT_FACTOR * max_utility), best_action


# Function to perform value iteration
def value_iteration(vi_env):
    # Initialize the iteration counter to 0
    iteration_cnt = 0
    while True:
        # Increment the iteration counter for each iteration
        iteration_cnt += 1
        # Create a new environment copy to store the updated utilities
        new_vi_env = copy_env(vi_env)
        # Initialize the error to 0
        error = 0
        # Loop through all the states in the environment
        for y in range(GRID_SIZE_H):
            for x in range(GRID_SIZE_W):
                # Calculate the Bellman equation result and the best action for the current state
                max_utility, best_action = bellman_equation_vi(vi_env, (x, y))
                # Update the new environment with the Bellman equation result
                new_vi_env[y][x] = max_utility
                # Update the error if the difference between the new and old utility is greater than the current error
                error = max(error, abs(max_utility - vi_env[y][x]))

        # Update the environment with the new environment
        vi_env = new_vi_env
        # If the error is smaller than the threshold, break the loop
        if error < SMALL_ENOUGH * (1 - DISCOUNT_FACTOR) / DISCOUNT_FACTOR:
            break

    # Return the updated environment and the iteration counter
    return vi_env, iteration_cnt


# Function to generate the optimal policy based on the value iteration results
def generate_policy(vi_env):
    # Create a GRID_SIZE_H x GRID_SIZE_W grid matrix to store the optimal policies for each state
    policy = [[None for _ in range(GRID_SIZE_W)] for _ in range(GRID_SIZE_H)]
    # Loop through all the states in the environment
    for y in range(GRID_SIZE_H):
        for x in range(GRID_SIZE_W):
            # Initialize the maximum utility to negative infinity and the best action to None
            max_utility = float('-inf')
            best_action = None
            # Loop through all the possible actions
            for action in ACTIONS:
                # Calculate the expected utility of taking the current action in the current state
                utility = expected_utility(vi_env, (x, y), action)
                # If the utility is greater than the maximum utility, update the maximum utility and the best action
                if utility > max_utility:
                    max_utility = utility
                    best_action = action
            # Update the policy with the best action for the current state
            policy[y][x] = best_action
    # Return the optimal policy
    return policy