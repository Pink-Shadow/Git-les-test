#This file is here to let you practice with merge errors.

def print_in_between(num, range):
    print(f"nu bij: {num} *= {range}")

def calc_factorial(num):
    res = 1
    for number in range(2, num+1):
        print_in_between(res, number)
        res *= number
    return res

def useless_function(acht):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    acht *= 1532
    acht //= 81
    acht += 38
    return letters[acht%letters.__len__()]


if __name__ == "__main__":
    print(f"\nresult: {calc_factorial(10)}\n")
    print(useless_function(11))
