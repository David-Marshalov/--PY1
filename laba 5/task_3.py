from random import randint
def get_unique_list_numbers(start=-10, finish=10, size=15) -> list[int]:
    # если size задать больше количества целых числес между start и stop то получится бесконечный цикл
    list_ = []

    size_ = 0
    size_range = range(start,finish + 1 )
    while len(list_) != size:
        x = random.randint(start, finish )
        if size > len(size_range): #сравниваю чтобы цикл не был бесконечным, к примеру, если убрать эту проверку и вместо size=15 подставить size= 22
            break
        elif x not in list_:
            list_.append(x)
    return list_


    # TODO написать функцию для получения списка уникальных целых

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))i), "oct": oct(i), "hex": hex(i)} for i in range(16)])