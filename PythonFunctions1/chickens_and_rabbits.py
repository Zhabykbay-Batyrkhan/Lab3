def solve(numheads, numlegs):
    y = (numlegs - 2*numheads)/2
    x = numheads - y
    return int(x), int(y)

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
x, y = result
print(f"Chickens: {x}, Rabbits: {y}")