import numpy as np

class Item:
    def __init__(self, name, price, weight, quantity=1):
        self.name = name
        self.price = price
        self.weight = weight
        self.quantity = quantity

def knapsack_dynamic(items, max_weight):
    n = len(items)
    # Tworzymy macierz DP o wymiarach (n+1) x (max_weight+1)
    dp = np.zeros((n + 1, max_weight + 1))
    
    # Wypełnianie macierzy DP
    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if items[i-1].weight <= w:
                dp[i, w] = max(dp[i-1, w], dp[i-1, w-items[i-1].weight] + items[i-1].price)
            else:
                dp[i, w] = dp[i-1, w]
    
    # Odtwarzanie rozwiązania
    w = max_weight
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i, w] != dp[i-1, w]:
            selected_items.append(items[i-1])
            w -= items[i-1].weight
    
    selected_items.reverse()  # Aby zachować kolejność dodawania przedmiotów
    return dp[n, max_weight], selected_items

def knapsack_greedy(items, max_weight):
    # Sortowanie przedmiotów według stosunku cena/waga w kolejności malejącej
    items.sort(key=lambda item: item.price / item.weight, reverse=True)
    
    total_value = 0
    total_weight = 0
    selected_items = {}
    
    for item in items:
        while item.quantity > 0 and total_weight + item.weight <= max_weight:
            if item.name in selected_items:
                selected_items[item.name].quantity += 1
            else:
                selected_items[item.name] = Item(item.name, item.price, item.weight, 1)
                
            total_weight += item.weight
            total_value += item.price
            item.quantity -= 1
    
    return total_value, list(selected_items.values())

# n = 8
items = [
    Item("P1", 10, 8, 7),
    Item("P2", 9, 8, 5),
    Item("P3", 5, 9, 4),
    Item("P4", 8, 10, 6),
    Item("P5", 10, 7, 4),
    Item("P6", 12, 10, 3),
]

max_value, selected_items = knapsack_dynamic(items, 30)

print(f"Algorytm dynamiczny:")
print(f"Maksymalna wartość: {max_value}")
print("Wybrane przedmioty:")
for item in selected_items:
    print(f"{item.name}: cena={item.price}, waga={item.weight}")

print(f"\nAlgorytm zachłanny:")
max_value, selected_items = knapsack_greedy(items, 100)
print(f"Maksymalna wartość: {max_value}")
print("Wybrane przedmioty:")

for item in selected_items:
    print(f"{item.name} ({item.quantity} szt.): cena={item.price}, waga={item.weight}")
