# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

even_list = []
for x in numbers:
    if x % 2 == 0:
        even_list.append(x)

print(even_list)


# 2. Print the difference between the largest and smallest value:

print(max(numbers)-min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.

i = 0
while i < len(numbers):
    if numbers[i] == 2 and numbers[i] == numbers[i+1]:
        print(numbers[i] == numbers[i+1])
        break
    else:
        i += 1

# 4. Print the sum of the numbers,
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total = 0
switch_on = True
for num in numbers:
    while switch_on:
        if num != 6:
            total += num
            break
        else:
            switch_on = False
    while not switch_on:
        if num != 7:
            break
        else:
            switch_on = True
print(total)

# 5. HARD! Print the sum of the numbers.
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.

total = 0
luck = True
numbers[numbers.index(13)+1] = 0
for num_bad in numbers:
    if num_bad != 13:
        total += num_bad
    else:
        pass

print(total)
