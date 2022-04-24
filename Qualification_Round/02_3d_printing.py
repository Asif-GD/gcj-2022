# list of colors
# cyan = [300000,300000,300000]
# magenta = [200000,200000,500000]
# yellow = [300000,500000,300000]
# black = [500000,300000,200000]

# cyan = [1000000,0,999999]
# magenta = [1000000,1000000,999999]
# yellow = [0,1000000,999999]
# black = [0,1000000,999999]

# cyan = [768763,699508,949704]
# magenta = [148041,515362,625054]
# yellow = [178147,534729,946212]
# black = [984173,714381,951187]

# max_of_all_min_colors = max(min_of_colors.values())
# print(max_of_all_min_colors)
# print(min_of_colors[max_of_all_min_colors])
# a,b,c,d = min_of_colors.values()
# print(f"{a} {b} {c} {d}")

# pseudocode
# step 1: sort the color into their individual color lists
# step 2: compare and retrieve the least units of the color across the lists
# step 3: if the total minimum of colors across the printers is below 10^6; it is impossible to print
# step 4: else-if it's equal to 10^6 units; print in that color and end.
# step 5: else we calculate the excess color units and reduce the difference accordingly

def printing_in_color(cyan, magenta, yellow, black):
    # minimum of all colors
    min_cyan = min(cyan)
    min_magenta = min(magenta)
    min_yellow = min(yellow)
    min_black = min(black)

    # for convenience of looping over
    min_of_colors = [min_cyan, min_magenta, min_yellow, min_black]

    total_min_from_all_colors = min_cyan + min_magenta + min_yellow + min_black

    if total_min_from_all_colors < 1000000:
        print("IMPOSSIBLE")

    elif total_min_from_all_colors == 1000000:
        print(f"{min_cyan} {min_magenta} {min_yellow} {min_black}")

    else:
        excess_color_units = abs(total_min_from_all_colors - 1000000)
        counter = 0
        for color in min_of_colors:
            if color >= excess_color_units:
                color -= excess_color_units
                min_of_colors[counter] = color
                break

            else:
                excess_color_units -= color
                min_of_colors[counter] = 0
            counter += 1
        cyan, magenta, yellow, black = min_of_colors
        print(f"{cyan} {magenta} {yellow} {black}")


number_of_test_cases = int(input())
cyan = []
magenta = []
yellow = []
black = []

for i in range(1, number_of_test_cases + 1):
    for j in range(3):
        color_1, color_2, color_3, color_4 = [int(s) for s in input().split(" ")]
        cyan.append(color_1)
        magenta.append(color_2)
        yellow.append(color_3)
        black.append(color_4)
    print("Case #{}: ".format(i), end='')
    printing_in_color(cyan, magenta, yellow, black)
    cyan.clear()
    magenta.clear()
    yellow.clear()
    black.clear()