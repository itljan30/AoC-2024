# 0-3 literal
# 4 5 6 reg a b c

# codes
# 0 (adv) = div takes reg a / 2 ^ combo operand to reg a
# 1 (bxl) = bitwise xor of reg b and instructions literal operator to reg b
# 2 (bst) = combo operand % 8 to reg b
# 3 (jnz) = nothing if reg a = 0 else jumps to literal
# 4 (bxc) = bitwise xor of reg b and reg c (ignore operand) to b
# 5 (out) = combo operand % 8 to reg b
# 6 (bdv) = div takes reg a / 2 ** combo operand to reg b
# 7 (cdv) = div takes reg a / 2 ** combo operand to reg c


a = 0
b = 0
c = 0
counter = 0
output: list[int] = []


def adv(CO: int):
    global a, b, c
    if CO <= 3:
        a = a // 2 ** CO
    elif CO == 4:
        a = a // 2 ** a
    elif CO == 5:
        a = a // 2 ** b
    elif CO == 6:
        a = a // 2 ** c


def bdv(CO: int):
    global a, b, c
    if CO <= 3:
        b = a // 2 ** CO
    elif CO == 4:
        b = a // 2 ** a
    elif CO == 5:
        b = a // 2 ** b
    elif CO == 6:
        b = a // 2 ** c


def cdv(CO: int):
    global a, b, c
    if CO <= 3:
        c = a // 2 ** CO
    elif CO == 4:
        c = a // 2 ** a
    elif CO == 5:
        c = a // 2 ** b
    elif CO == 6:
        c = a // 2 ** c


def bxl(literal: int):
    global b
    b ^= literal


def bxc(CO: int):
    global b, c
    b ^= c


def bst(CO: int):
    global a, b, c
    if CO <= 3:
        b = CO % 8
    if CO == 4:
        b = a % 8
    if CO == 5:
        b = b % 8
    if CO == 6:
        b = c % 8


def jnz(literal: int):
    global a, counter
    if a != 0:
        counter = literal


def out(CO: int):
    global a, b, c
    if CO <= 3:
        output.append(CO % 8)
    elif CO == 4:
        output.append(a % 8)
    elif CO == 5:
        output.append(b % 8)
    elif CO == 6:
        output.append(c % 8)


def run(program):
    global counter
    while counter < len(program):
        arg1 = int(program[counter])
        arg2 = int(program[counter + 1])

        counter += 2

        if arg1 == 0:
            adv(arg2)
        elif arg1 == 1:
            bxl(arg2)
        elif arg1 == 2:
            bst(arg2)
        elif arg1 == 3:
            jnz(arg2)
        elif arg1 == 4:
            bxc(arg2)
        elif arg1 == 5:
            out(arg2)
        elif arg1 == 6:
            bdv(arg2)
        elif arg1 == 7:
            cdv(arg2)


def main():
    global a, b, c, counter

    program: list[str] = []
    with open("input.txt", "r") as file:
        for line in file:
            if line.startswith("Register A: "):
                _, number = line.split(": ")
                a = int(number)
            elif line.startswith("Register B: "):
                _, number = line.split(": ")
                b = int(number)
            elif line.startswith("Register C: "):
                _, number = line.split(": ")
                c = int(number)
            elif line.startswith("Program: "):
                _, instructions = line.split(": ")
                program = instructions.strip().split(",")

    run(program)

    for num in output:
        print(num, end=',')

    print()


if __name__ == "__main__":
    main()
