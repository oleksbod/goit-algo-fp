import random

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    results = {}
    for _ in range(num_rolls):
        roll1 = roll_dice()
        roll2 = roll_dice()
        total = roll1 + roll2
        results[total] = results.get(total, 0) + 1
    return results

def calculate_probabilities(results, num_rolls):
    probabilities = {}
    for i in range(2, 13):
        probabilities[i] = results.get(i, 0) / num_rolls * 100
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for total, prob in probabilities.items():
        print(f"{total}\t{prob:.2f}% ({prob/100:.2f})")

def main():
    print("1000 кидків кубиків")
    num_rolls = 1000  # Кількість кидків кубиків
    results = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(results, num_rolls)
    print_probabilities(probabilities)

    print("10000 кидків кубиків")
    num_rolls = 10000  # Кількість кидків кубиків
    results = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(results, num_rolls)
    print_probabilities(probabilities)

    print("1000000 кидків кубиків")
    num_rolls = 1000000  # Кількість кидків кубиків
    results = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(results, num_rolls)
    print_probabilities(probabilities)

if __name__ == "__main__":
    main()