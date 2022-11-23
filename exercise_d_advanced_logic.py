# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
print("Q.1 : ")
list_of_even = []
for num in numbers:
    if num%2 == 0:
        list_of_even.append(num)
print(list_of_even)

# 2. Print the difference between the largest and smallest value:
print("Q.2 : ")
sorted_numbers = sorted(numbers)
print(sorted_numbers[-1] - sorted_numbers[0])

# 3. Print True if the list contains a 2 next to a 2 somewhere.
print("Q.3 : ")
last_number = "Initialised to str so cannot match"
for num in numbers:
    # print(f"debug: checking num: {num} against {last_number}")
    if num == last_number:
        print(True)
        break
    else:
        last_number = num

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
print("Q.4 : ")
# numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]
total = 0
count_allowed = True
for num in numbers:
    # print(f"debug: num = {num}")
    if num == 6:
        count_allowed = False
    elif num == 7:
        count_allowed = True
    elif count_allowed:
        total += num
    #     print(f"debug: ount_allowed: total = {total}")
    # else:
    #     print(f"debug: count not allowed: total = {total}")
print(total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
print("Q.5 : ")

total = 0
i = 0
index_cursed = "Any index assigned to this will not be counted"
for num in numbers:
    if num == 13:
        index_cursed = i + 1
        i += 1
    elif i == index_cursed:
        print(f"num: {num} comes after a 13 so is not counted")
        i +=1
    else:
        total += num
        i += 1
print(total)







