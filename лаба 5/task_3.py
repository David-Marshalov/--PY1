import random
def get_unique_list_numbers(start=-10, finish=10, size=15) -> list[int]:
    list_ = []
    size_ = 0
    size_range = range(start,finish + 1 )
    while len(list_) != size:
        x = random.randint(start, finish )
        if size > len(size_range):
            break
        elif x not in list_:
            list_.append(x)
    return list_


    # TODO написать функцию для получения списка уникальных целых

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))