# all the estimation points
lis = [1.1, 1.3, 1.5, 1.7, 1.9]

# list to contain all the estimation results
lis2 = []

# Compute all the f(x) of estimation points.
for i in lis:
    stage_result = 1 / i    # function f(x)
    lis2.append(stage_result)

# area of each individual rectangle.
print(lis2)

# add up all the values of rectangles.
result = 0
for i in lis2:
    result += i

# product of delta-x and summation of all the f(x) estimations
print(0.2 * result)

