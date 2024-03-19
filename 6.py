def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0
    for item, properties in sorted_items:
        if total_cost + properties['cost'] <= budget:
            selected_items.append(item)
            total_cost += properties['cost']
            total_calories += properties['calories']
    return selected_items, total_calories


def dynamic_programming(items, budget):
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    for i, (item, properties) in enumerate(items.items(), 1):
        for j in range(1, budget + 1):
            if properties['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], properties['calories'] + dp[i - 1][j - properties['cost']])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    i, j = len(items), budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[selected_items[-1]]['cost']
        i -= 1

    selected_items.reverse()
    total_calories = dp[len(items)][budget]
    return selected_items, total_calories


# Приклад використання:
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 110

greedy_selected_items, greedy_total_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", greedy_selected_items)
print("Total calories:", greedy_total_calories)

dp_selected_items, dp_total_calories = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Selected items:", dp_selected_items)
print("Total calories:", dp_total_calories)