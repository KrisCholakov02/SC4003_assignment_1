from config import *
from utils import *
import pandas as pd
import random
from algorithms.algorithm_utils import *


# Function to initialize the policy iteration maze environment
def init_pi_env():
    # Create a GRID_SIZE_H x GRID_SIZE_W grid matrix filled with zeros
    pi_env = [[0 for _ in range(GRID_SIZE_W)] for _ in range(GRID_SIZE_H)]
    # Create a GRID_SIZE_H x GRID_SIZE_W grid matrix filled with random actions (Initialize the policy randomly)
    pi_policy = [[random.choice(list(ACTIONS.keys())) for _ in range(GRID_SIZE_W)] for _ in range(GRID_SIZE_H)]
    # Return the environment and the policy matrices
    return pi_env, pi_policy


# Function for the Bellman equation used for policy iteration
# Bellman equation: U_(i+1)(s) = R(s) + γ * Σ_(s') P(s' | s, π(s)) * U_i(s')
def bellman_equation_pi(vi_env, s, action):
    # Check if the current state is a reward, hole, wall or empty field and assign the corresponding reward
    if s in REWARDS:  # If the current state is a reward
        reward = REWARDS[s]
    elif s in HOLES:  # If the current state is a hole
        reward = HOLES[s]
    elif s in WALLS:  # If the current state is a wall
        reward = 0
    else:  # If the current state is an empty field
        reward = EMPTY_REWARD

    # Calculate the expected utility of taking action 'action' in state 's'
    utility = expected_utility(vi_env, s, action)

    # Return the Bellman equation result
    return reward + (DISCOUNT_FACTOR * utility)


# Function to perform policy evaluation
def policy_evaluation(pi_env, pi_policy, iteration):
    # Iterate until the error is smaller than the SMALL_ENOUGH threshold
    while True:
        # Create a new environment copy to store the updated utilities
        new_pi_env = copy_env(pi_env)
        # Initialize the error to 0
        error = 0
        # Loop through all the states in the environment
        for y in range(GRID_SIZE_H):
            for x in range(GRID_SIZE_W):
                # Calculate the Bellman equation result for the current state and action
                new_pi_env[y][x] = bellman_equation_pi(pi_env, (x, y), pi_policy[y][x])
                # Update the error with the difference between the new and old utility
                error = max(error, abs(new_pi_env[y][x] - pi_env[y][x]))

        # Update the environment with the new utilities
        pi_env = new_pi_env
        # Break the loop if the error is smaller than the SMALL_ENOUGH threshold
        if error < SMALL_ENOUGH:
            break

    # Return the updated environment
    return pi_env


# Function to perform policy iteration
def policy_iteration(pi_env, pi_policy):
    # Initialize the iteration counter to 0
    iteration_cnt = 0
    while True:
        # Increment the iteration counter for each iteration
        iteration_cnt += 1
        # Perform policy evaluation
        new_pi_env = policy_evaluation(pi_env, pi_policy, iteration_cnt)
        # Initialize the policy_stable flag to True (used to check if the policy has converged)
        policy_stable = True
        # Loop through all the states in the environment
        for y in range(GRID_SIZE_H):
            for x in range(GRID_SIZE_W):
                # Store the old action
                old_action = pi_policy[y][x]
                # Defining the maximum utility --> max_(a ∈ A(s)) ∑_(s′) P(s′ | s, a) * U_i(s′)
                max_utility = float('-inf')
                # Defining the best action --> argmax_(a ∈ A(s)) ∑_(s′) P(s′ | s, a) * U_i(s′)
                best_action = None
                # Loop through all possible actions
                for action in ACTIONS:
                    # Calculate the Bellman equation result for the current state and action
                    utility = bellman_equation_pi(new_pi_env, (x, y), action)
                    # If the utility is greater than the maximum utility, update the maximum utility and the best action
                    if utility > max_utility:
                        max_utility = utility
                        best_action = action
                # Update the environment with the Bellman equation result
                pi_env[y][x] = max_utility
                # Update the policy with the best action
                pi_policy[y][x] = best_action

                # If the old action is different from the best action, set the policy_stable flag to False
                if old_action != best_action:
                    policy_stable = False

        # Break the loop if the policy has converged
        if policy_stable:
            break

    # Return the updated environment, policy and the iteration counter
    return pi_policy