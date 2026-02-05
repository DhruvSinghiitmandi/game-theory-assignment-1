from collections import defaultdict

def get_utility_dict():
    utility = defaultdict(dict)
    utility["c"]["c"] = (-5, -5)
    utility["c"]["nc"] = (-1, -10)
    utility["nc"]["c"] = (-10, -1)
    utility["nc"]["nc"] = (-2, -2)
    return utility


def backward_induction(utility):
    # Stage 1: Player 2 best responses
    p2_best_response = {}

    # If Player 1 does not confess
    if utility["nc"]["c"][1] > utility["nc"]["nc"][1]:
        p2_best_response["nc"] = "c"
    else:
        p2_best_response["nc"] = "nc"

    # If Player 1 confesses
    if utility["c"]["c"][1] > utility["c"]["nc"][1]:
        p2_best_response["c"] = "c"
    else:
        p2_best_response["c"] = "nc"

    # Stage 2: Player 1 anticipates Player 2
    payoff_if_c = utility["c"][p2_best_response["c"]][0]
    payoff_if_nc = utility["nc"][p2_best_response["nc"]][0]

    p1_action = "c" if payoff_if_c > payoff_if_nc else "nc"
    p2_action = p2_best_response[p1_action]

    return p1_action, p2_action, utility[p1_action][p2_action]


def simulate_game(utility, n_runs=50):
    u1_hist, u2_hist = [], []

    for _ in range(n_runs):
        _, _, (u1, u2) = backward_induction(utility)
        u1_hist.append(u1)
        u2_hist.append(u2)

    return u1_hist, u2_hist


import matplotlib.pyplot as plt

def plot_utilities(u1_hist, u2_hist):
    plt.figure()
    plt.plot(u1_hist, label="Player 1 Utility")
    plt.plot(u2_hist, label="Player 2 Utility")
    plt.xlabel("Run")
    plt.ylabel("Utility")
    plt.title("Multistage Prisoner's Dilemma ")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    utility = get_utility_dict()

    p1, p2, payoff = backward_induction(utility)
    print("SPNE:", (p1, p2))
    print("Payoffs:", payoff)

    u1_hist, u2_hist = simulate_game(utility, n_runs=50)
    plot_utilities(u1_hist, u2_hist)
