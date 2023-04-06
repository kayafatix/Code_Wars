"""
If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
"""

number = int(input())
my_list = [i for i in range(1, number) if i % 3 == 0 or i % 5 == 0]


def solution(number):
    result = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)
    print(sum(result))


solution(100)
print(sum(my_list))