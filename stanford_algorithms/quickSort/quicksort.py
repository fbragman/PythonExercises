import os


def load_txt_file():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, 'QuickSort.txt'), 'r') as f:
        integer_list = [int(x) for x in f]

    return integer_list


def sort_it(list_a, start_idx, end_idx, counter):

    if start_idx < end_idx:

        final_pivot_idx = partition(list_a, start_idx, end_idx, counter)
        # recursive partition on left side of final_pivot_idx of list_a
        sort_it(list_a, start_idx, final_pivot_idx, counter)
        # recursive partition on right side of final_pivot_idx of list_a
        sort_it(list_a, final_pivot_idx + 1, end_idx, counter)


def partition(A, l, r, counter):

    p = A[l]
    i = l + 1

    # calculate length of array - [l,...,r]
    comparisons = r-l-1

    for j in range(l+1, r):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[l], A[i-1] = A[i-1], A[l]

    counter += [comparisons]

    return i-1


def main():

    # load txt file into list
    integer_list = load_txt_file()

    # computer number of inversions in integer_list
    counter = []
    sort_it(integer_list, 0, len(integer_list), counter)
    num_counts = sum(counter[:])

    if sorted(integer_list) == integer_list:
        print(num_counts)


if __name__ == '__main__':
    main()