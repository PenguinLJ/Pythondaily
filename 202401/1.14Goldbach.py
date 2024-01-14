"""
哥德巴赫猜想是世界近代三大数学难题之一“
任一大于2的整数都可写成3个质数之和”
此猜想至今也没有完全证明，但是却可以用程序去验证它。
当前哥德巴赫猜想已经演变为欧拉的版本：
“任一大于2的偶数都可以写成两个素数之和”
素数：一个大于1的自然数，除了1和它自身外，不能被其他自然数整除。
题目简化为：判断一个大于5的偶数是否能写成两个素数之和？
"""

# number = int(input("Please a Even number that greater than 5.\n"))
#
#
# def isPrimenumber(number):  # 该函数用于判断数字是否为素数
#     if number == 2:
#         return True
#     for i in range(2, number):
#         if number % i == 0:  # 除了1和自己，如果能被其他数整除，就不是素数
#             return False
#
#     return True
#
#
# def find_element_Primenumber(number):  # 用于找到一个数字的子素数
#     child = []
#     for i in range(2, number):
#         if isPrimenumber(i):
#             child.append(i)
#
#     return child
#
#
# def is_added_by_two_oddnumber(number):
#     first, second = 0, 0
#     if number < 5:
#         print("The number is lower than 5.")
#         return
#     elif number % 2 != 0:
#         print("Please input a Even number, not a Odd number.")
#         return
#     else:
#         child = find_element_Primenumber(number // 2)
#         for i in child:
#             if (number - i) in child:
#                 first = i
#                 second = number - i
#                 print(f"The first number is {first}, the second is {second}.")
#             else:
#                 print("Oops, cannot find the two number.")
#
#
# is_added_by_two_oddnumber(number)


import math


def is_even(number):
    """判断是否为偶数"""
    return number % 2 == 0


def is_prime(number):
    """判断是否为素数"""
    if number < 2:
        return False
    sqrt_num = int(math.sqrt(number))
    for i in range(2, sqrt_num + 1):
        if number % i == 0:
            return False
    return True


def can_split(number):
    """判断该数字能否拆分为两个素数"""
    equo_list = []
    for i in range(1, number // 2 + 1):
        j = number - i
        if is_prime(i) and is_prime(j):
            equo_list.append(f"{number}={i}+{j}")
    if not equo_list:
        equo_list.append(f"{number} cannot split two numbers.")

    return equo_list


if __name__ == "__main__":
    num = input("please input a Even number greater than 5\n")
    if num.isdigit():
        num = int(num)
        if num > 5 and is_even(num):
            result = can_split(num)
            for i in result:
                print(i)
        else:
            print("Oops,the number must be Even and greater than 5")
    else:
        print("Please input number")
