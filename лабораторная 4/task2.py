def get_count_char(list_a):
    textt = list_a.lower()
    clean_list=filter(str.isalpha, textt)
    text_dict = {}
    COUNT = 0
    for letter in  clean_list:
        text_dict[letter] = text_dict.get(letter, COUNT) + 1
    return text_dict

def share_of_text(list_a):
    textt = list_a.lower()
    clean_list=filter(str.isalpha, textt)
    text_dict = {}
    COUNT = 0
    number_ = len(textt)
    for letter in  clean_list:
        text_dict[letter] = text_dict.get(letter, COUNT) + 1 / number_ * 100
    return text_dict


main_str ="""Данное предложение будет разбиваться на отдельные слова.В качестве разделителя для встроенного метода split будет выбран символ пробела.
На выходе мы получим список отдельных слов.Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!"""

print(get_count_char(main_str))
print(share_of_text(main_str))