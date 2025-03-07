def tri_recursion(k):
  if k > 0:
    result = k + tri_recursion(k - 1)
    print(result)  
    return result
  else:
    return 0  # Base case when k is 0

print("Recursion Example Results:")
data=tri_recursion(6)
print(data)