def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
result=tri_recursion(-1)
print(result)