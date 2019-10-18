t = [[1,2,3], [3, 2], [4,5,6], [321, 0]]

def nested_sum(t):
    total = 0
    for i in t:
        if isinstance(i, list):  # checks if `i` is a list and if it is sums all elements in the list
            total += nested_sum(i)
        else:
            total += i
    return total

print(nested_sum(t))

    






