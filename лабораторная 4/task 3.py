def delete(list_, index=None):
    # TODO реализовать функцию удаления элемента из списка по индексу
    if index == None:
        list_ = list_[index:-1]
    elif index == -1:
        list_ = list_[0:-1]
    else:
        list_ = list_[0:index] + list_[index + 1:]
    return list_

print(delete([0, 0, 1, 2], index=1)) # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1)) # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4])) # [0, 1, 2, 3]