def get_count_char(text):
    text = text.lower()
    list_words = text.split("!")
    with_separate =" ".join(list_words)
    clean_list=filter(str.isalpha, with_separate)
    my_dict = {}
    COUNT = 0
    for letter in  clean_list:
        my_dict[letter] = my_dict.get(letter, COUNT ) + 1
    return my_dict



main_str ="""Данное предложение будет разбиваться на отдельные слова.В качестве разделителя для встроенного метода split будет выбран символ пробела.
На выходе мы получим список отдельных слов.Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!"""







print(get_count_char(main_str))