friends = ["Karen","Tom","John","Mike","oscar","Ben","Chris"] #note in list functions are written seperately not with print statement
print(friends[4])#prints oscar
print(friends[-2])#prints ben
friends[2]= "Luke" #replaces 2nd index element with luke
print(friends[2]) #prints the second element
print(friends[1:]) #prints from index value 1 to end of the list
print(friends[3:6]) #prints elemnts from 3rd index to 5th index

numbers = [4, 5, 8, 2, 9, 7, 1]
print(len(friends))
friends.extend(numbers) #combines two list
print(friends)

friends.append("Paul") #adds paul as the last element
print(friends)

friends.insert(1, "George") #insert george in 1st index value
print(friends)

friends.remove("oscar")
print(friends)

friends.pop() #remove last elemnt of list
print(friends)

print(friends.index("Luke"))
print(friends.count("George"))

friends = ["Karen","Tom","John","Mike","oscar","Ben","Chris"]
friends.sort()
print(friends)
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
print(numbers)

friends.clear() #empty the list
print(friends)

