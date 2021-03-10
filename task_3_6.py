# Задание 6

# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(word):
    return word.capitalize()


def another_int_func(word):
    return word[0].upper() + word[1:]


print(int_func('text'))
print(another_int_func('vasily'))