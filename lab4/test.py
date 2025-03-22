def a(n):
    yield n + 1
    yield n + 9

gerenaton = a(5)
print(next(gerenaton))
print(next(gerenaton))