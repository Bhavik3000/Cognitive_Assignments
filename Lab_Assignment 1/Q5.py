# 5.1 Find largest and smallest in a list:
numbers = [32, 11, 44, 15, 5]
print(max(numbers), min(numbers))


# 5.2 Retrieve value from a dictionary:
d = {"a": 1, "b": 2, "c": 3}
print(d["b"])

# 5.3 Sort a list:
numbers = [34, 12, 48, 15, 85]
print(sorted(numbers))  # In  Ascending order
print(sorted(numbers, reverse=True))  # In Descending order


# 5.4 Merge dictionaries:
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d1.update(d2)
print(d1)
