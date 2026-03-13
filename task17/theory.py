with open('путь до файла') as file:
    #Считывает весь файл, возвращает str
    data = file.read()
    #Считывает 1 строку до символа \n #Возвращает str
    data = file.readline()
    #Считывает все строки, возвращает list[str]
    data = file.readlines()


