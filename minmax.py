import minmax

#print to screen and ask for list of numbers
array = []

while True:

    arrayInput = input("Please enter a list of numbers: ")
    if arrayInput == "":
      break

    array.append(arrayInput)
    

print(array)



#create a formula to get the max difference (highest number - lowest number)


#create a formula to get the min (smallest number)
smallestNum = str(min(array))
print("The smallest number is " + smallestNum)

#create a formula to get the max (largest number)
largestNum = str(max(array))
print("The largest number is " + largestNum)