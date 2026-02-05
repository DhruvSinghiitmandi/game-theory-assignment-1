import numpy as np
from utils import get_utility_dict, plot_save


def simulate_game(p, utility_scores, iterations=1000):
    """
    Simulate the Prisoner's Dilemma for a fixed p.
    Returns empirical expected utilities for both players.
    """
    u1_total, u2_total = 0.0, 0.0

    for _ in range(iterations):
        a1 = np.random.choice(["c", "nc"], p=[p, 1 - p])
        a2 = np.random.choice(["c", "nc"], p=[p, 1 - p])

        payoff = utility_scores[a1][a2]
        u1_total += payoff[0]
        u2_total += payoff[1]

    return u1_total / iterations, u2_total / iterations

import numpy as np
from collections import Counter
from utils import get_utility_dict, plot_save


def utility_frequency_plot(p, utility_scores, iterations=5000):
    utilities = []

    for _ in range(iterations):
        a1 = np.random.choice(["c", "nc"], p=[p, 1 - p])
        a2 = np.random.choice(["c", "nc"], p=[p, 1 - p])
        utilities.append(utility_scores[a1][a2][0])  # Player 1

    counts = Counter(utilities)

    # Sort by utility value
    utility_vals = sorted(counts.keys())
    frequencies = [counts[u] for u in utility_vals]

    plot_save(
        frequencies,
        utility_vals,
        f"Utility Frequency (Player 1), p={p}",
        "Utility Value",
        "Count",
        f"scenario1_utility_frequency_p_{p}.png",
        scatter=False,
    )

    return counts


def main():
    utility_scores, _ = get_utility_dict()

    # ---------- STEP 1: Single p analysis ----------
    p = 0.3
    iterations = 500
    utilities_over_time = []

    for _ in range(iterations):
        a1 = np.random.choice(["c", "nc"], p=[p, 1 - p])
        a2 = np.random.choice(["c", "nc"], p=[p, 1 - p])
        utilities_over_time.append(utility_scores[a1][a2][0])

    plot_save(
        utilities_over_time,
        np.arange(iterations),
        f"Utility per Game (Player 1), p={p}",
        "Iteration",
        "Utility",
        "scenario1_single_p_simulation.png",
        scatter=False,
    )

    # ---------- STEP 2: Construct F(p) ----------
    prob_values = np.linspace(0, 1, 100)
    player1_expected = []
    player2_expected = []
    avg_expected_utility = []

    for p in prob_values:
        u1, u2 = simulate_game(p, utility_scores, iterations=100)
        player1_expected.append(u1)
        player2_expected.append(u2)
        avg_expected_utility.append((u1 + u2) / 2)

    # ---------- STEP 3: Plots ----------
    plot_save(
        player1_expected,
        prob_values,
        "Expected Utility vs p (Player 1)",
        "p (Prob. of Confess)",
        "Expected Utility",
        "scenario1_player1_expected.png",
        scatter=False,
    )

    plot_save(
        player2_expected,
        prob_values,
        "Expected Utility vs p (Player 2)",
        "p (Prob. of Confess)",
        "Expected Utility",
        "scenario1_player2_expected.png",
        scatter=False,
    )

    plot_save(
        avg_expected_utility,
        prob_values,
        "Average Expected Utility vs p ((U1 + U2)/2)",
        "p (Prob. of Confess)",
        "Average Expected Utility",
        "scenario1_avg_expected.png",
        scatter=False,
    
    )
    p = 0.1
    utility_frequency_plot(p, utility_scores, iterations=5000)

    p = 0.3
    utility_frequency_plot(p, utility_scores, iterations=5000)

    p = 0.5
    utility_frequency_plot(p, utility_scores, iterations=5000)

    p = 0.7
    utility_frequency_plot(p, utility_scores, iterations=5000)

    p = 0.9
    utility_frequency_plot(p, utility_scores, iterations=5000)

if __name__ == "__main__":
    main()
