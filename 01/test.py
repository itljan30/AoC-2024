list1 = []
list2 = []

with open("input.txt", "r") as file:
    for line in file:
        numbers = line.split("   ")

        list1.append(numbers[0])
        list2.append(numbers[1])
