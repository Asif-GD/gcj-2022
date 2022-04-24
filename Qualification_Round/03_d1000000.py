# pseudocode
# step 1: if it's just one die, return 1
# step 2: else-if the number of dice < least-sided die amongst the N dice; then return N
# step 3: else, the dice are to be looped to check for the longest straight

# number_of_dice = 0
# list_of_dice = []

# number_of_dice = 4
# list_of_dice = [6, 10, 12, 8]

# number_of_dice = 6
# list_of_dice = [5, 4, 5, 4, 4, 4]

# number_of_dice = 10
# list_of_dice = [10, 10, 7, 6, 7, 4, 4, 5, 7, 4]

# number_of_dice = 1
# list_of_dice = [10]

def find_longest_straight(number_of_dice, list_of_dice):
    if number_of_dice == 1:
        print('1')
    elif number_of_dice <= min(list_of_dice):
        print(number_of_dice)
    else:
        temp_list_of_dice.sort()
        sequence = 1
        counter = 0
        while counter < number_of_dice:
            # print(temp_list_of_dice[counter], sequence)
            if temp_list_of_dice[counter] < sequence:
                # print("if loop")
                temp_list_of_dice.pop(0)
                number_of_dice -= 1
                sequence = 0
                counter = -1
            sequence += 1
            counter += 1
        print(sequence - 1)


number_of_test_cases = int(input())
number_of_dice = 0
list_of_dice = []

for i in range(1, number_of_test_cases + 1):
    number_of_dice = int(input())
    # print(number_of_dice)
    list_of_dice = list([int(s) for s in input().split(" ")])
    # print(list_of_dice)
    temp_list_of_dice = list_of_dice[:]  # didn't want to lose the original input
    # print(temp_list_of_dice)
    print("Case #{}: ".format(i), end='')
    find_longest_straight(number_of_dice, list_of_dice)
