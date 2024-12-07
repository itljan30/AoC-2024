# so we have 2 lists, we need to sort both of them and go index by index and
# subtract number from list 1 - number from list 2 and take abs value
# then we iterate over this new list and just add it all up
# we don't actually need to make a third list, just keep a running total for all subtractions

list1 = []
list2 = []

with open('input.txt', 'r') as input:
    for line in input:
        input1, input2 = line.split('   ')
        list1.append(int(input1))
        list2.append(int(input2))

list1 = sorted(list1)
list2 = sorted(list2)

running_total = 0

for i in range(len(list1)):
    running_total += abs(list1[i] - list2[i])

print(running_total)
