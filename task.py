import openpyxl
import datetime

full_name = "Ivanov Ivan Ivanovych"
lastname_lat = "Ivanov"
now = datetime.datetime.now() # поточні дата та час
file_name = lastname_lat+ "-" +now.strftime("%Y%m%d-%H%M%S")+".xlsx" # створення назви файлу

wb = openpyxl.Workbook() # створення обєкту Workbook
sheet = wb.active # запис у змінну sheet листа

'''
    У першому рядку у першій комірці - ПІБ студента
'''
cell = sheet['A1']  # перший рядок перша комірка
cell.value = full_name # запис ПІБ у комірку

'''
    У другому рядку у першій комірці - поточні дата і час у форматі ДД:ММ:РРРР ГГ:ХХ:СС
'''
date = now.strftime("%Y.%m.%d %H:%M:%S")
cell = sheet['A2'] # перший рядок перша комірка
cell.value = date # запис дати у комірку
cell.number_format = 'DD:MM:YYYY HH:MM:SS' # налаштування формату дати

'''
    Введення цілих чисел a та b для наступних записів,
    за умови що b>a
'''
while True:
    a = int(input("Введіть значення а: "))
    b = int(input("Введіть значення b: "))
    if b>a:
        break
    print("Значення 'b' повинно бути більше за значення 'а'")

'''
    Далі рядки повинні мати прогресію 
    перша комірка - число, друга комірка - число в квадраті, третя - в кубі
    числа в межах [a,b] включно
'''
for num in range(a, b+1):
    sheet.append([num, num**2, num**3])

wb.save(file_name)



