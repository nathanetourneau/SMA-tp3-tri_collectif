# SMA-tp3-tri_collectif

This repository contains the work of a school project for Claude Bernard University dealing with multi-agent systems. 


## Scenario

### Version 1
On a N*M grid, there are objects, n_a objets of class A, and n_b objects of class B. There are also n_agents agents, and the goal for the agent is to sort the objects. The agents are subject to the following rules : 
- they are able to move only randomly in the eight directions (N, S, E, W, NW, NE, SE, SO).
- on a grid, there can only be one object and/or one agent at the same time.
- agents have a memory of the past m cells they visited, they pick or drop objects only using the memory of the past m cells, they do not have access to their environment.

This work is based on the paper : Deneubourg, Jean-Louis et al *“The dynamics of collective sorting robot-like ants and ant-like robots.”* (1991).

### Version 2
On a N*M grid, there are objects, n_a objets of class A, and n_b objects of class B, n_c objects of class C. There are also n_agents agents, and the goal for the agent is to sort the objects. The agents are subject to the following rules : 
- they are able to move only randomly in the eight directions (N, S, E, W, NW, NE, SE, SO).
- on a grid, there can only be one object and/or one agent at the same time.
- agents have a memory of the past m cells they visited, they pick or drop objects only using the memory of the past m cells, they do not have access to their environment.
- to carry an object of type C, two agents are needed. When an agent meets an object of type C, it sends pheromone to call for help. The amount of pheromone on a cell decrease over time and distance from the emitter.

## Run

To run the work, one has to type `cd V1` or `cd V2` if one wants to run version 1 or version 2. Once done, one can use the handy streamlit app in `app.py` by running `streamlit run app.py` or just run `python main.py` for a less fancy but nevertheless working visualisation of the objects spread across the rounds.
