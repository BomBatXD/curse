def ex1(dict, key):
    try:
        print(dict[key])
    except:
        print('key error')


def ex2(set1, set2):
    return set1.union(set2)


def ex3(list_tup):
    dict = {}
    for tup in list_tup:
        for char in tup:
            if char in dict.keys():
                dict[char] += 1
            else:
                dict[char] = 1
    return dict