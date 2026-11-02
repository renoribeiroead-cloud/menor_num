#-*- coding: latin1 -*-

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

menor_num = num1 #assume o menor

if num2 < num1: #teste valor2
    menor_num = num2
if num3 < num1: #teste valor3
    menor_num = num3

print(f"o menor numero é: ", menor_num)
