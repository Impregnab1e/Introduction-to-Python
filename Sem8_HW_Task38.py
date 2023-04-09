def writing_person():
    lastname = input("фамилия: ")
    name = input("имя: ")
    surname = input("отчество: ")
    tel = input("телефон: ")
    data = open('E:\Учеба\Учусь\Python\phonebook.txt', "a", encoding="utf-8")
    data.writelines(
        f"фамилия:{lastname} имя:{name} отчество:{surname} телефон:{tel}\n")
    data.close()


def search():
    lookfor = input("кого ищем? ")
    with open('E:\Учеба\Учусь\Python\phonebook.txt', "r", encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)


def print_phonebook():
    with open('E:\Учеба\Учусь\Python\phonebook.txt', "r", encoding="utf-8") as data:
        for line in data:
            print(line)


def delete_info():
    name_del = input("Введите имя контакта, который хотите удалить: ")
    with open('E:\Учеба\Учусь\Python\phonebook.txt', "r", encoding="utf-8") as data:
        lines = data.readlines()
    with open('E:\Учеба\Учусь\Python\phonebook.txt', "w", encoding="utf-8") as data1:
        for line in lines:
            if name_del not in line:
                data1.write(line)
            else:
                print(line)
                ask = input("Желаете удалить эту строку? (y / n) ")
                while ask not in ("y", "n"):
                    print("Ввод не корректный")
                    ask = input("Желаете удалить эту строку? (y / n) ")
                if ask == "n":
                    data1.write(line)


def replace_info():
    line_change = input('Введите информацию, которую необходимо заменить: ')
    with open('E:\Учеба\Учусь\Python\phonebook.txt', "r", encoding="utf-8") as data:
        lines = data.readlines()
        with open('E:\Учеба\Учусь\Python\phonebook.txt', "w", encoding="utf-8") as data1:
            for line in lines:
                if line_change not in line:
                    data1.write(line)
                else:
                    ask = input('Что хотите поменять (1,2,3,4')
                    while ask not in ("1", "2", "3", "4"):
                        print('ввод некорректный ')
                        ask = input('Что хотите поменять (1,2,3,4)  : ')
                    new_data = input('Введите новые данные : ')
                    line_list = line.split()
                    line_list[int(ask)-1] = new_data
                    data1.write('\t'.join(line_list) + '\n')


def load():
    new_phonebook = input("введите ссылку: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open('E:\Учеба\Учусь\Python\phonebook.txt', "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
            data_1.write("\n")


print("""1 - добавление,
2 - поиск,
3 - вывод на экран,
4 - удаление пользователя,
5 - изменение данных """)
ask = int(input())
if ask == 1:
    writing_person()
elif ask == 2:
    search()
elif ask == 3:
    print_phonebook()
elif ask == 4:
    delete_info()
elif ask == 5:
    replace_info()
else:
    print("нет такой комманды")
