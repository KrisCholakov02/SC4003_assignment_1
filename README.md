# SC4003 Intelligent Agents

## Assignment 1: Single Agent Decision Making

### Description
This project is part of the SC4003 Intelligent Agents course at Nanyang Technological University. The assignment focuses on single-agent decision-making, analyzing agent behavior and decision processes within a simulated maze environment. The key objectives are:

- Implementing **Value Iteration** and **Policy Iteration** to find optimal policies.
- Exploring how different maze configurations affect convergence and decision-making.
- Developing a **game-like environment** to visualize and interact with the maze, enhancing interpretability and usability.

### Solution Overview
The solution includes:

- **Markov Decision Process (MDP) Framework:** The environment is modeled as an MDP with states, actions, transition probabilities, and rewards.
- **Algorithms:** Value Iteration and Policy Iteration are implemented to compute optimal policies.
- **Multiple Maze Configurations:**
  - **Base Maze** (as per assignment requirements)
  - **Increased-Size Maze** (10x10 grid for higher complexity)
  - **Labyrinth Maze** (pathways and penalties to challenge the agent)
  - **Blockages Maze** (gated sections requiring strategic movement)
  - **Dynamic Environment** (changing reward positions over time)
- **Interactive Visualization:** A mini-game using **PyGame** to visualize the maze and agent actions.

### Novelty: Interactive Game Environment
A key contribution of this project is the development of a **mini-game environment** using PyGame. This allows users to:

- Visualize maze structures dynamically.
- Observe agent movement and decision-making.
- Test different policies interactively.
- Gain insights into agent behavior beyond static console outputs.

### Project Structure
```
assignment1/
│── algorithms/
│   ├── value_iteration.py     # Implementation of Value Iteration
│   ├── policy_iteration.py    # Implementation of Policy Iteration
│   ├── algorithm_utils.py     # Utility functions for MDP handling
│── maze_configs/
│   ├── base.py                # Base Maze configuration
│   ├── blockages.py           # Blockages Maze configuration
│   ├── increased_size.py      # Increased-Size Maze configuration
│   ├── labyrinth.py           # Labyrinth Maze configuration
│── assets/                    # Visual assets for the interactive environment
│── results/                   # CSV files containing computed utilities
│── plots/                     # Generated plots for analysis
│── main.py                    # Runs the interactive PyGame environment
│── main.ipynb                 # Jupyter notebook for running experiments
│── config.py                  # Configuration constants
│── requirements.txt           # Dependencies
│── README.md                  # Project documentation
```

### Installation & Execution
#### Prerequisites
Ensure you have **Python 3.8+** and **Conda** installed.

#### Setup Environment
```bash
cd assignment1
conda create --name <env> --file requirements.txt
conda activate <env>
```

#### Running the Interactive Environment (Mini-Game)
```bash
python main.py
```

#### Running the Jupyter Notebook for Experiments
```bash
jupyter notebook main.ipynb
```

### Results & Insights
- **Value Iteration vs. Policy Iteration:**
  - Both methods produce the same optimal policy.
  - **Policy Iteration converges faster** (fewer iterations).
- **Effect of Maze Complexity:**
  - Larger mazes and obstacles **increase convergence time**.
  - Blocked paths require better strategy planning.
- **Dynamic Environments:**
  - Introducing changing rewards makes learning more difficult.

### Conclusion
This project successfully implements decision-making agents using MDPs. The addition of an **interactive visualization environment** provides an intuitive way to understand agent policies and maze-solving strategies. The results highlight the efficiency of different reinforcement learning approaches and the impact of environmental complexity.

### Author
**Kristiyan Kamenov Cholakov**
