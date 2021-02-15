import sys

a = [x for x in range(100000)]
print(a)
print(sys.getsizeof(a))