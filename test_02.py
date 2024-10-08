# Write a fucntion to find all the subsets of a list
# NOTE: The number of subsets in a list of N length is 2^N

# This base case is not an 'if' statement, but rather a 'for' loop
# that serves as the goal you're moving towards.


def calculate_subset(l, result_list, subset, index):
    # add the current subset to the result list
    result_list.append(subset[:])

    # Generate elements by recursively including and excluding elements
    for i in range(index, len(l)):
        # include the element in the subset
        subset.append(l[i])

        calculate_subset(l, result_list, subset, i + 1)

        # exclude the element in the subset
        subset.pop()


def find_subsets(l: list[int]):

    subset: list[int] = []
    result_list: list[list[int]] = []
    index = 0
    calculate_subset(l, result_list, subset, index)
    return result_list


def main() -> None:
    my_list = [1, 2, 3]
    res = find_subsets(my_list)
    print(res)


if __name__ == '__main__':
    main()
