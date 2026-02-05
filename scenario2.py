from collections import defaultdict

def get_utility_dict():
    # Payoffs are (player1, player2)
    utility_scores = defaultdict(dict)
    utility_scores["c"]["c"] = (-5, -5)
    utility_scores["c"]["nc"] = (-1, -10)
    utility_scores["nc"]["c"] = (-10, -1)
    utility_scores["nc"]["nc"] = (-2, -2)
    return utility_scores


def get_dominant_strategy(utility_scores, player=1):
    """
    player = 1 or 2
    returns dominant strategy if it exists
    """
    idx = 0 if player == 1 else 1
    strategies = ["c", "nc"]

    for s in strategies:
        for opp in strategies:
            other = "nc" if s == "c" else "c"

            if player == 1:
                if utility_scores[s][opp][idx] < utility_scores[other][opp][idx]:
                    break
            else:
                if utility_scores[opp][s][idx] < utility_scores[opp][other][idx]:
                    break
        else:
            return s  # strictly dominant

    return None


def find_nash_equilibrium(utility_scores):
    d1 = get_dominant_strategy(utility_scores, player=1)
    d2 = get_dominant_strategy(utility_scores, player=2)

    if d1 is not None and d2 is not None:
        return (d1, d2), utility_scores[d1][d2]
    return None, None


def simulate_game(utility_scores, n_runs=50):
    strategy_p1 = get_dominant_strategy(utility_scores, player=1)
    strategy_p2 = get_dominant_strategy(utility_scores, player=2)

    u1_hist, u2_hist = [], []

    for _ in range(n_runs):
        u1, u2 = utility_scores[strategy_p1][strategy_p2]
        u1_hist.append(u1)
        u2_hist.append(u2)

    return u1_hist, u2_hist


import matplotlib.pyplot as plt

def plot_utilities(u1_hist, u2_hist):
    plt.figure()
    plt.plot(u1_hist, label="Player 1 Utility")
    plt.plot(u2_hist, label="Player 2 Utility")
    plt.xlabel("Game Run")
    plt.ylabel("Utility")
    plt.title("Utilities over Multiple Runs (Nash Equilibrium)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    utility_scores = get_utility_dict()

    # Nash equilibrium
    ne, utilities = find_nash_equilibrium(utility_scores)
    print("Nash Equilibrium:", ne)
    print("Utilities at NE:", utilities)

    # Simulation
    u1_hist, u2_hist = simulate_game(utility_scores, n_runs=50)

    # Plot
    plot_utilities(u1_hist, u2_hist)
