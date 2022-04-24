# solution

def create_minus_plus_string_pairs(columns):
    minus_plus_string_pairs = '-+' * columns
    return minus_plus_string_pairs


def create_period_pipe_string_pairs(columns):
    period_pipe_string_pairs = '.|' * columns
    return period_pipe_string_pairs


def print_ascii(rows, columns):
    for line in range(1, actual_rows + 1):
        if line == 1:
            print_string = '..+' + create_minus_plus_string_pairs(columns)
            print(print_string[0:actual_columns])  # because there will be excess characters
        elif line == 2:
            print_string = '..|' + create_period_pipe_string_pairs(columns)
            print(print_string[0:actual_columns])  # because there will be excess characters
        elif line % 2 != 0:
            print_string = '+' + create_minus_plus_string_pairs(columns)
            print(print_string)
        else:
            print_string = '|' + create_period_pipe_string_pairs(columns)
            print(print_string)


number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    rows, columns = [int(s) for s in input().split(" ")]

    # considering the matrix
    actual_rows = 2 * rows + 1
    actual_columns = 2 * columns + 1

    print("Case #{}:".format(i))
    print_ascii(rows, columns)
