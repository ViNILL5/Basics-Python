def odd_nums(n):
  for num in range(1, n + 1, 2):
    print(num)  
    yield num
  
 
odd_to_n = odd_nums(30)

while True:
  (next(odd_to_n))