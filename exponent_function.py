# Author:Anthony Quinn
# Date: 26-8-19
# Description: Program demonstrating the Exponent Function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
        return result


print(raise_to_power(5, 3))
