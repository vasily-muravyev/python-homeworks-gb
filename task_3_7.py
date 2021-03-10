# Задание 7

# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(word):
    return word.capitalize()

def capitalize_all_words(sentence):
    return ' '.join(map(int_func, sentence.split()))

sentence = 'this is sentence to transform'
print(f'sentence: {sentence} -> {capitalize_all_words(sentence)}')