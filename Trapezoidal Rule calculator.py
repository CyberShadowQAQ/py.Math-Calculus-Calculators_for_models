# a = float(input('a goes here:'))
# b = float(input('b goes here:'))
# n = float(input('number of sub-intervals:'))
#
# width = float((b - a) / n)
#
# left_endpoint = a
# estimation_points = [a]
#
# while left_endpoint < b:
#     left_endpoint += width
#     estimation_points.append(left_endpoint)
#
# del estimation_points[-1]
#
# end_points = [estimation_points[0], estimation_points[-1]]
#
# del estimation_points[-1]
# del estimation_points[0]
#
# outcome1 = 0
# outcome2 = 0
#
# for i in estimation_points:
#     outcome1 += 2 / i
#
# for j in end_points:
#     outcome2 += 1 / j
#
# summation_part = float(outcome1) + float(outcome2)
# final_answer = 0.5 * width * summation_part
#
# print(estimation_points)
#
# # Questions left to be completed:
# # 1. This only works for function f(x) = 1/x, more coding needs to be done for other functions.
#
# # 2. If you print out estimation points they are not finite decimals
# # with our test input been a = 1, b = 2, n = 5. Should be [1.2, 1.4, 1.6, 1.8] instead of
# # [1.2, 1.4, 1.5999999999999999, 1.7999999999999998] weird roundings done by python
#
# # 3. (width test input a = 1, b = 2, n = )If we calculate the errors with n -> ∞ the
# # results by theory should -> ln(2) and error -> 0 but by test it's not the case the error fluctuate.


# def operation(x):
#     user_func = input('Enter your formula')
#     Shunting yard to reformat the user function.
#     ...


def midpoint_riemann(a, b, n):
    lst_1 = []
    lst_2 = [a, b]
    outcome1 = 0
    outcome2 = 0
    width = (b - a) / n

    while a < b:
        a += width
        lst_1.append(a)

    del lst_1[-1]
    del lst_1[-1]
    print(lst_1)
    print(lst_2)

    for i in lst_1:
        outcome1 += 2 * (1 / i)

    for j in lst_2:
        outcome2 += 1 / j

    result = 0.5 * width * (outcome2 + outcome1)
    return result


print(midpoint_riemann(1, 2, 100000))
