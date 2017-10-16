import os


def count(list_a):

    n = len(list_a)//2
    left_array = list_a[:n]
    right_array = list_a[n:]

    if len(list_a) > 1:

        left_array, x = count(left_array)
        right_array, y = count(right_array)

        # merging of sorted sub-arrays
        merged_out, z = merge_count(left_array, right_array)
        return merged_out, x+y+z

    else:

        return list_a, 0


def merge_count(left_array, right_array):

    i = 0
    j = 0
    number_of_inversions = 0
    output_array = []

    # counting
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            # populate output_array
            output_array += [left_array[i]]
            i += 1
        else:
            # populate output_array with next value from right_array
            output_array += [right_array[j]]
            j += 1
            # l > r -> r will be next in line if we assume left_array is sorted (due to recursive sorting on left_array)
            # -> remaining number of values in left_array (len(left_array)-i) are under inversion with r
            number_of_inversions += len(left_array) - i

    # at the end of counting while loop - output_array will not be fully populated
    # e.g.  if l = [7] and r = [6]
    #       --> while loop == FALSE and output_array = 6
    #       --> iterate over un-iterated l indexes --> range(i, len(l))
    # just add lists since we can do that..
    output_array += left_array[i:]
    output_array += right_array[j:]

    return output_array, number_of_inversions


def load_txt_file():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path,'IntegerArray.txt'), 'r') as f:
        integer_list = [int(x) for x in f]

    return integer_list


def main():

    # load txt file into list
    integer_list = load_txt_file()

    # computer number of inversions in integer_list
    output, number_of_inversions = count(integer_list)
    print(number_of_inversions)


if __name__ == '__main__':
    main()
