#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    
    number_args = len(sys.argv) - 1
    if number_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operation = sys.argv[2]
    if operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, mul, sub, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operation == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))

    elif operation == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))

    elif operation == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))

    else:
        print("{} - {} = {}".format(a, b, sub(a, b)))
