def recusion(k):
    if k > 0:
        result = k + recusion(k - 1)
        print(result)
        return result
    else:
        return 0

# Call the function
result = recusion(12)
# print(result)


