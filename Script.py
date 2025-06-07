"""
Marco Bejarano Oseguera
06/06/2025

This application is a probability distribution calculator for a die.
When it starts, it asked the user for three inputs: the number of side,
the number of the dice to roll and how many times it needs to roll this
die.
"""

import random

def roll_dice_once(num_dice, num_sides):
    total_sum = 0
    for single_roll in range(num_dice):
        roll_result = random.randint(1, num_sides)
        total_sum += roll_result
    return total_sum

def simulate_multiple_rolls(num_dice, num_sides, num_trials):
    all_sums = []
    for trial in range(num_trials):
        sum_result = roll_dice_once(num_dice, num_sides)
        all_sums.append(sum_result)
    return all_sums

def calculate_probabilities(sum_list):
    probability_dict = {}
    total_rolls = len(sum_list)
    for outcome in sum_list:
        if outcome in probability_dict:
            probability_dict[outcome] += 1
        else:
            probability_dict[outcome] = 1
    for key in probability_dict:
        probability_dict[key] = probability_dict[key] / total_rolls
    return probability_dict

def main():
    print("Dice Probability Distribution Calculator")
    num_sides = int(input("Enter the number of sides of each die (N): "))
    num_dice = int(input("Enter the number of the dice to roll (M): "))
    num_trials = int(input("Enter the number of times to roll the dice (K): "))

    results = simulate_multiple_rolls(num_dice, num_sides, num_trials)
    probabilities = calculate_probabilities(results)

    print("\nSum\tProbability")
    for possible_sum in sorted(probabilities):
        print(f"{possible_sum}\t{probabilities[possible_sum]:.4f}")

def run_tests():
    print("\nRunning Test Cases...\n")

    # Normal Test Case 1: 2 six-sided dice, 1000 trials
    test1 = simulate_multiple_rolls(2, 6, 1000)
    prob1 = calculate_probabilities(test1)
    print("Test 1: 2 dice, 6 sides, 1000 trials")
    print("Possible sums:", sorted(prob1.keys()))
    print("Total probabilities sum to:", sum(prob1.values()))
    print()

    # Normal Test Case 2: 3 four-sided dice, 500 trials
    test2 = simulate_multiple_rolls(3, 4, 500)
    prob2 = calculate_probabilities(test2)
    print("Test 2: 3 dice, 4 sides, 500 trials")
    print("Possible sums:", sorted(prob2.keys()))
    print("Total probabilities sum to:", sum(prob2.values()))
    print()

    # Normal Test Case 3: 1 ten-sided die, 100 trials
    test3 = simulate_multiple_rolls(1, 10, 100)
    prob3 = calculate_probabilities(test3)
    print("Test 3: 1 die, 10 sides, 100 trials")
    print("Possible sums:", sorted(prob3.keys()))
    print("Total probabilities sum to:", sum(prob3.values()))
    print()

    # Edge Case 1: 1 die, 1 side, 10 trials (should always be 1)
    test4 = simulate_multiple_rolls(1, 1, 10)
    prob4 = calculate_probabilities(test4)
    print("Edge Test 1: 1 die, 1 side, 10 trials")
    print("Probabilities:", prob4)
    print()

    # Edge Case 2: 0 dice, 6 sides, 10 trials (sum should always be 0)
    test5 = simulate_multiple_rolls(0, 6, 10)
    prob5 = calculate_probabilities(test5)
    print("Edge Test 2: 0 dice, 6 sides, 10 trials")
    print("Probabilities:", prob5)
    print()

    # Edge Case 3: 2 dice, 6 sides, 0 trials (no rolls)
    test6 = simulate_multiple_rolls(2, 6, 0)
    prob6 = calculate_probabilities(test6)
    print("Edge Test 3: 2 dice, 6 sides, 0 trials")
    print("Probabilities:", prob6)
    print()


if __name__ == "__main__":
    main()
    #run_tests()
