def ex1():
    text = input("enter text: ")

    l = text.split(' ')
    d = {}

    for word in l:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1

    print(d)


def ex2():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    unionS = set1.union(set2)

    print(unionS)


def ex3():
    my_list = [1, 2, 2, 3, 4, 4, 5]
    new_list = list(set(my_list))

def ex4():
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    my_dict['e'] = 5
    my_dict['d'] = 10