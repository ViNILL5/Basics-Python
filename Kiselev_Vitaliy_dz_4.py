import sys
from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


result = []
start = perf_counter()

for i in range(len(src)-1):
  if src[i] < src[i+1]:
    result.append(src[i+1])
    
print(type(result))
print(result, sys.getsizeof(result), perf_counter() - start)


print('*' * 20)

result = (j for i, j in zip(src, src[1:]) if j > i)

print(type(result))
print([*result], sys.getsizeof(result), perf_counter() - start)