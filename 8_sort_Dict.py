# Program to Sort Dictionary by ket and value

dict = {'shau': 20,'vasudha': 04,'vilas':14,'vaidehi': 30,'mayo': 17}

print("Sorted by key:")
print(sorted(dict.items(), key=lambda kv: (kv[0], kv[1])))

print("\nSorted by value:")
print(sorted(dict.items(), key=lambda kv: (kv[1], kv[0])))
