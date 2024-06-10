
import openpyxl
import pyautogui
import utilstb
import time

workbook = openpyxl.load_workbook(r'')
sheet = workbook.active


cod = sheet['C']
produto = sheet['B']    
valor = sheet['D']
cod1 = 0
produto1 = 0
valor1 = 0

utilstb.open_file_explorer()

for i in range(1, 1582):
    cod1 = cod[i]
    produto1 = produto[i]
    valor1 = valor[i]
    utilstb.create_file(produto1)
    time.sleep(12)
    utilstb.edit_and_save_file(produto1, valor1, cod1)

