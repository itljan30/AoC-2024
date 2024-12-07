# we load all the data from the input file but instead put it into a hashmap as a string key
# and just increase the value by one for each one we find

list1 = []
list2 = {}

with open("input.txt", "r") as input:
    for line in input:
        input1, input2 = line.split('   ')
        list1.append(int(input1))
        list2.setdefault(int(input2), 0)
        list2[int(input2)] += 1

similarity = 0
for key in list1:
    list2.setdefault(key, 0)
    similarity += list2[key] * key

print(similarity)
