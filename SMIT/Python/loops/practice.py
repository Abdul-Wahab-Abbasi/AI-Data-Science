while True:
    startingNum = int(input("Enter the starting number: "))
    endingNum = int(input("Enter the ending number: "))
    numList = []
    sumOfNums = 0
    if startingNum <= endingNum:
        choice = input("Enter Odd or Even: ").lower()
        if (choice == 'even' or choice == 'odd'):
            while startingNum <= endingNum:
                if choice == 'even':
                    if startingNum % 2 == 0:
                        numList.append(startingNum)
                        sumOfNums += startingNum
                elif choice == 'odd':
                    if startingNum % 2 != 0:
                        numList.append(startingNum)
                        sumOfNums += startingNum
                startingNum += 1
                
            break
        else:
            print("Choice must be 'Even' or 'Odd' ")
    else:
        print("Starting number should be less than or equal to ending number. Please try again.")

print(f"List of {choice} numbers: {numList}")
print(f"Count of {choice} numbers: {len(numList)}")
print(f"Sum of {choice} numbers: {sumOfNums}")
print(f"Average of {choice} numbers: {sumOfNums / len(numList)}")