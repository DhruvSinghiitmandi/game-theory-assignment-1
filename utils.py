import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict


def get_utility_dict():
    # Payoffs are (player1, player2)
    # Both confess -> (-5, -5)
    # Player1 confesses, Player2 stays silent -> (-1, -10)
    # Player1 stays silent, Player2 confesses -> (-10, -1)
    # Both stay silent -> (-2, -2)
    utility_values = [(-5, -5), (-1, -10), (-10, -1), (-2, -2)]
    utility_scores = defaultdict(dict)
    utility_scores["c"]["c"] = (-5, -5)
    utility_scores["c"]["nc"] = (-1, -10)
    utility_scores["nc"]["c"] = (-10, -1)
    utility_scores["nc"]["nc"] = (-2, -2)
    return utility_scores, utility_values


def get_utility(action, prob, utility_values):
    if action == "c":
        return utility_values[0] * prob * prob + utility_values[1] * prob * (1 - prob)
    else:
        return utility_values[2] * prob * (1 - prob) + utility_values[3] * (1 - prob) * (1 - prob)


def plot_save(y_values, x_values, title, xlabel, ylabel, filename, scatter=True):
    plt.figure()
    if scatter:
        plt.scatter(x_values, y_values)
    else:
        plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
