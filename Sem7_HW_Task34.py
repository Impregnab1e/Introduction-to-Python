# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам

def vinnypuh(list_1):
    letters = ['а', 'о', 'у', 'и', 'ы', 'е', 'ё', 'э', 'ы', 'ю', 'я']
    new_list = list_1.split()
    def result(x): return sum(1 for i in x if i in letters)
    l = result(new_list[0])
    if all([result(i) == l for i in new_list]):
        return 'Парам пам-пам'
    return 'Пам парам'

text = str(input('Введите стихотворение: '))
decide = vinnypuh(text)
print(decide)