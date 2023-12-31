# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12

# k = 'ноутбук'

# import re
# string = k. upper()
# scrab_dic_en = {1: "A, E, I, O, U, L, N, S, T, R", 2: "D, G", 3: "B, C, M, P", 4 : "F, H, V, W, Y", 5: "K", 8: "J, X", 10: "Q, Z"}
# scrab_dic_ru = {1: "А, В, Е, И, Н, О, Р, С, Т", 2: "Д, К, Л, М, П, У", 3: "Б, Г, Ё, Ь, Я", 4 : "Й, Ы", 5: "Ж, З, Х, Ц, Ч", 8: "Ш, Э, Ю", 10: "Ф, Щ, Ъ"}
# scoreSum = 0
# if re.search("[А-Я]", string): 
#     for i in string:
#         for m, n in scrab_dic_ru.items():
#             if i in n:
#                 scoreSum += m 
# elif re.search ("[A-Z]", string):
#     for i in string:
#         for m, n in scrab_dic_en.items():
#             if i in n:
#                 scoreSum += m 
# else:
#     print ("Вы ввели не слово!")
# print (f"Сумма очков = {scoreSum}")            

k = 'ящерица'


word = []
for i in k.upper():
    word.append(i)

scrab_dic_en = {1: "A, E, I, O, U, L, N, S, T, R", 2: "D, G", 3: "B, C, M, P", 4 : "F, H, V, W, Y", 5: "K", 8: "J, X", 10: "Q, Z"}
scrab_dic_ru = {1: "А, В, Е, И, Н, О, Р, С, Т", 2: "Д, К, Л, М, П, У", 3: "Б, Г, Ё, Ь, Я", 4 : "Й, Ы", 5: "Ж, З, Х, Ц, Ч", 8: "Ш, Э, Ю", 10: "Ф, Щ, Ъ"}
scoreSum = 0

for m, n in scrab_dic_ru.items():
    if word[0] in n:
        for m, n in scrab_dic_ru.items():
            for i in word:
                if i in n:
                    scoreSum += m

for m, n in scrab_dic_en.items():
            for i in word:
                if i in n:
                    scoreSum += m

print (f"Сумма очков = {scoreSum}")

