# Peg Solitaire

CS 449 semester project. Building Peg Solitaire (BrainVita) over five sprints.

## Project Description

This repository contains my implementation of Peg Solitaire (BrainVita), a single-player board game built as the semester-long project for CS 449. The game starts with every position on the board filled by a peg except one. A move consists of jumping a peg orthogonally or diagonally over an adjacent peg into an empty hole two positions away, removing the peg that was jumped. The objective is to clear the board down to as few pegs as possible, ideally just one.

The project is developed across five sprints. It's expected to eventually support a manual mode, where a human plays until no legal moves remain and is given a rating based on how many pegs are left, and an autoplay mode, where the computer plays the game out using randomized (not hardcoded) valid moves. It also needs to support multiple board shapes.

Beyond making the game playable, this project is also meant to be a practical exercise in software engineering: applying object-oriented design (class hierarchies, inheritance, polymorphism, dynamic binding), keeping game logic separate from the user interface, writing unit tests alongside the game logic as it's built, and tracking the whole process through Git/GitHub.

## Sprint 0 Decisions

| Topic | Decision |
|---|---|
| Language | Python 3.10+ |
| GUI library | PyQt6 |
| IDE | VS Code |
| Unit test framework | pytest |
| Programming style guide | Google Python Style Guide |
| Project hosting | GitHub |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"