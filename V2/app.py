#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main module coding the loop of the multi-agent system. The scenario here is a
grid of dimensions NxM, with a number na of objects of class A, nb of objects
of class B, n_agents agents, and the purpose of the agents is to walk randomly,
and sort the objects with few rules described in Deneubourg, Jean-Louis et al.
“The dynamics of collective sorting robot-like ants and ant-like robots.”

The main script is embedded in a Streamlit app, with a visualisation made with
the Altair plotting library.

@authors: Nathan Etourneau, Paul Flagel
"""

import random

import streamlit as st

from environment import Environment
from visualization import update_altair_plot

# Sidebar

st.sidebar.header("General settings")

N = st.sidebar.number_input(
    label="Number of rows ?", min_value=1, max_value=99999, value=50)
M = st.sidebar.number_input(
    label="Number of columns ?", min_value=1, max_value=99999, value=50)
NA = st.sidebar.number_input(
    label="Number of objects of class A ?", min_value=1, max_value=99999, value=100)
NB = st.sidebar.number_input(
    label="Number of objects of class B ?", min_value=1, max_value=99999, value=100)
NC = st.sidebar.number_input(
    label="Number of objects of class C ?", min_value=1, max_value=99999, value=100)
N_AGENTS = st.sidebar.number_input(
    label="Number of agents ?", min_value=1, max_value=99999, value=20)
KPLUS = st.sidebar.slider(label="Value for K+ ?",
                          min_value=0., max_value=1., value=0.1)
KMINUS = st.sidebar.slider(label="Value for K- ?",
                           min_value=0., max_value=1., value=0.3)
MEMORY_BUFFER_SIZE = st.sidebar.number_input(
    label="Size of memory buffer ?", min_value=1, max_value=99999, value=20)
N_ROUNDS = st.sidebar.number_input(
    label="Number of rounds ?", min_value=1, max_value=1000000000, value=1000000)

RATIO = st.sidebar.slider(label="Value of the temporal decay factor of the pheromones ?",
                          min_value=0., max_value=1., value=0.75)
SIGNAL_RANGE = st.sidebar.number_input(label="Spatial range of the pheromones ?",
                                       min_value=1, value=4)

MAX_PATIENCE = st.sidebar.number_input(label="Patience for objects of type C ?",
                                       min_value=1, max_value=100, value=15)


start = st.sidebar.button("Run")
_ = st.sidebar.button("Stop")

# Layout

st.title("Practical work 3 : Multi-agents implementation")
st.markdown(
    """Authors : @paulflagel, @nathanetourneau.

A school project focused on the implementation of this research paper : Deneubourg, Jean-Louis, Simon Goss, Nigel R. Franks, Ana B. Sendova-Franks, Claire Detrain and Louis Chretien. “The dynamics of collective sorting robot-like ants and ant-like robots.” (1991).

Master 2 IA - Université Lyon 1 - 2021-2022"""
)


status = st.empty()
round_progress_bar = st.progress(0)
st.header('Graph of the objects')
plot_placeholder = st.empty()


def main(n_rounds, N, M, na, nb, nc, n_agents, kplus, kminus, memory_buffer_size, ratio, signal_range, max_patience):
    env = Environment(N, M, na, nb, nc, n_agents, kplus, kminus,
                      memory_buffer_size, ratio, signal_range, max_patience)

    # Loop
    keys = list(env.agents.keys())

    for round in range(1, n_rounds + 1):
        status.text(f'Round n°{round}/{N_ROUNDS}')
        round_progress_bar.progress(round/N_ROUNDS)

        # Shuffle the agents to mimic the fact that the movement is erratic
        random.shuffle(keys)

        for key in keys:
            agent = env.agents[key].agent
            empty_cells = agent.perception(env)
            agent.action(env, empty_cells)

        env.update_pheromones()

        if round % 50 == 0 or round == 1:
            fig = update_altair_plot(env)
            plot_placeholder.altair_chart(fig, use_container_width=True)


if start:
    main(N_ROUNDS, N, M, NA, NB, NC, N_AGENTS, KPLUS,
         KMINUS, MEMORY_BUFFER_SIZE, RATIO, SIGNAL_RANGE, MAX_PATIENCE)
