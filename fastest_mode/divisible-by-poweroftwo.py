

def divisible(n):
  j=0
  s = bin(n)[2:]
  for i in s[::-1]:
    if i=='1':
      break
    j+=1
  ans = 2**j
  return ans
        
number = int(input())
print(divisible(number))
