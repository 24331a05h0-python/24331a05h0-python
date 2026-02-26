lst = [5, 8, 20, 3, 30, 14]
lst2 = [x for x in lst if x > 10]
print("Elements greater than 10:", lst2)

dct = {"book": 40, "notebook": 25, "marker": 15, "bag": 60}
dct.update({k: v + 5 for k, v in dct.items()})
print("Dictionary after updating:", dct)
