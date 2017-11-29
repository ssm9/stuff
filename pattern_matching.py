#!/usr/bin/env python


def main():
    # 111 1111 111 11111 111
    # a   b    a   c     a
    # a   b    a   b     a
    string = "111111111111111111"
    pattern = "abcabc"

    positional_arrays = []
    strings = []

    pos_arr_pattern = positional_array(list(pattern))

    for s in split(string, len(pattern) - 1):
        strings.append(s)
        pos_arr = positional_array(s)
        positional_arrays.append(pos_arr)
        print("%s : %s" % (s, pos_arr == pos_arr_pattern))

    print(positional_arrays.__contains__(positional_array(list(pattern))))


def positional_array(in_list):
    a = {}
    b = []
    i = 0
    for element in in_list:
        k = a.get(element, i)
        a[element] = k
        i += 1
        b.append(k)
    return b


def split(string, num_spaces):
    if num_spaces == 0:
        yield [string]
        return
    else:
        for i in range(1, len(string)):
            for tail in split(string[i:], num_spaces - 1):
                yield [string[:i]] + tail


if __name__ == '__main__':
    main()
