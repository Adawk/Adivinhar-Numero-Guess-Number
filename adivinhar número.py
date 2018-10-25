import time

lista1 = [1, 3, 5, 7, 9, 11,
         13, 15, 17, 19, 21, 23,
         25, 27, 29, 31, 33, 35,
         37, 39, 41, 43, 45, 47,
         49, 51, 53, 55, 57, 59]

lista2 = [2, 3, 6, 7, 10, 11,
         14, 15, 18, 19, 22, 23,
         26, 27, 30, 31, 34, 35,
         38, 39, 42, 43, 46, 47,
         50, 51, 54, 55, 58, 59]

lista3 = [4, 5, 6, 7, 12, 13,
         13, 14, 15, 20, 21, 22,
         23, 28, 29, 30, 31, 36,
         37, 38, 39, 44, 45, 46,
         47, 52, 53, 54, 55, 60]

lista4 = [8, 9, 10, 11, 12, 13, 
         13, 14, 15, 24, 25, 26,
         27, 28, 29, 30, 31, 40,
         41, 41, 43, 44, 45, 46,
         47, 56, 57, 58, 59, 60]

lista5 = [16, 17, 18, 19, 20, 21,
         22, 23, 24, 25, 26, 27,
         28, 29, 30, 31, 31, 48,
         49, 50, 51, 52, 53, 54,
         55, 56, 57, 58, 59, 60]

lista6 = [32, 33, 34, 35, 36, 37,
         38, 39, 40, 41, 42, 43,
         44, 45, 46, 46, 47, 48,
         49, 50, 51, 52, 53, 54,
         55, 56, 57, 58, 59, 60]

print ()

print ()
print("ESCOLHA UM NÚMERO DE 1 À 60")
print("E ME DIGA QUAL DESSES QUADROS CONTÉM O NÚMERO ESCOLHIDO")
print()
print("Observação: o número escolhido pode estar em um  quadro ou mais")

print ("_" *84)
print()
print("Quadro 1")
print()
print(lista1[0], lista1[1], lista1[2], lista1[3], lista1[4], lista1[5])

print(lista1[6], lista1[7], lista1[8], lista1[9], lista1[10], lista1[11])

print(lista1[12], lista1[13], lista1[14], lista1[15], lista1[16], lista1[17])

print(lista1[18], lista1[19], lista1[20], lista1[21], lista1[22], lista1[23])

print(lista1[24], lista1[25], lista1[26], lista1[27], lista1[28], lista1[29])

print("_" *84)
print()
print("Quadro 2")
print()
print(lista2[0], lista2[1], lista2[2], lista2[3], lista2[4], lista2[5])

print(lista2[6], lista2[7], lista2[8], lista2[9], lista2[10], lista2[11])

print(lista2[12], lista2[13], lista2[14], lista2[15], lista2[16], lista2[17])

print(lista2[18], lista2[19], lista2[20], lista2[21], lista2[22], lista2[23])

print(lista2[24], lista2[25], lista2[26], lista2[27], lista2[28], lista2[29])

print("_" *84)
print()
print("Quadro 3")
print()
print(lista3[0], lista3[1], lista3[2], lista3[3], lista3[4], lista3[5])

print(lista3[6], lista3[7], lista3[8], lista3[9], lista3[10], lista3[11])

print(lista3[12], lista3[13], lista3[14], lista3[15], lista3[16], lista3[17])

print(lista3[18], lista3[19], lista3[20], lista3[21], lista3[22], lista3[23])

print(lista3[24], lista3[25], lista3[26], lista3[27], lista3[28], lista3[29])

print("_" *84)
print()
print("Quadro 4")
print()
print(lista4[0], lista4[1], lista4[2], lista4[3], lista4[4], lista4[5])

print(lista4[6], lista4[7], lista4[8], lista4[9], lista4[10], lista4[11])

print(lista4[12], lista4[13], lista4[14], lista4[15], lista4[16], lista4[17])

print(lista4[18], lista4[19], lista4[20], lista4[21], lista4[22], lista4[23])

print(lista4[24], lista4[25], lista4[26], lista4[27], lista4[28], lista4[29])

print("_" *84)
print()
print("Quadro 5")
print()
print(lista5[0], lista5[1], lista5[2], lista5[3], lista5[4], lista5[5])

print(lista5[6], lista5[7], lista5[8], lista5[9], lista5[10], lista5[11])

print(lista5[12], lista5[13], lista5[14], lista5[15], lista5[16], lista5[17])

print(lista5[18], lista5[19], lista5[20], lista5[21], lista5[22], lista5[23])

print(lista5[24], lista5[25], lista5[26], lista5[27], lista5[28], lista5[29])

print("_" *84)
print()
print("Quadro 6")
print()
print(lista6[0], lista6[1], lista6[2], lista6[3], lista6[4], lista6[5])

print(lista6[6], lista6[7], lista6[8], lista6[9], lista6[10], lista6[11])

print(lista6[12], lista6[13], lista6[14], lista6[15], lista6[16], lista6[17])

print(lista6[18], lista6[19], lista6[20], lista6[21], lista6[22], lista6[23])

print(lista6[24], lista6[25], lista6[26], lista6[27], lista6[28], lista6[29])

print ("_" *84)

print("Vamos ver se eu acerto o número que você escolheu!")
print()

print("Dê um espaço para dividir o número da tabela")
print("exemplo: 1 2 3 ...")
print()
resposta = str(input("Quais são os quadros?\n"))

valor = resposta.split(" ")

valor2 = []

for x in valor:
    if x == '1':
        valor2.append(lista1[0])
        
    if x == '2':
        valor2.append(lista2[0])
        
    if x == '3':
        valor2.append(lista3[0])
        
    if x == '4':
        valor2.append(lista4[0])
        
    if x == '5':
        valor2.append(lista5[0])
        
    if x == '6':
        valor2.append(lista6[0])
        
num = 0        
for x in valor2:
    num = num + x
print ()
print("Hum...")
time.sleep(1)
print()
print("Analisando cartões")
time.sleep(3)
print("_" * 84)
print()
print("O número que você escolheu foi {}".format(num))
print()

sair = input("Aperte enter para sair")
