
"""
Autor: Tomasz Głuc
Program Wrozby Icing
"""
import random
import time

                         #Zmienne
WROZBA = []                           #zmienna wrozby
H = {}                                #zmienna slownika wrozby
HEKSAGRAMY = {('---', '---', '---', '---', '---', '---'): 1,
              ('- -', '- -', '- -', '- -', '- -', '- -'): 2,
              ('- -', '---', '- -', '- -', '- -', '---'): 3,
              ('---', '- -', '- -', '- -', '---', '- -'): 4,
              ('- -', '---', '- -', '---', '---', '---'): 5,
              ('---', '---', '---', '- -', '---', '- -'): 6,
              ('- -', '- -', '- -', '- -', '---', '- -'): 7,
              ('- -', '---', '- -', '- -', '- -', '- -'): 8,
              ('---', '---', '- -', '---', '---', '---'): 9,
              ('---', '---', '---', '- -', '---', '---'): 10,
              ('- -', '- -', '- -', '---', '---', '---'): 11,
              ('---', '---', '---', '- -', '- -', '- -'): 12,
              ('---', '---', '---', '---', '- -', '---'): 13,
              ('---', '- -', '---', '---', '---', '---'): 14,
              ('- -', '- -', '- -', '---', '- -', '- -'): 15,
              ('- -', '- -', '---', '- -', '- -', '- -'): 16,
              ('- -', '---', '---', '- -', '- -', '---'): 17,
              ('---', '- -', '- -', '---', '---', '- -'): 18,
              ('- -', '- -', '- -', '- -', '---', '---'): 19,
              ('---', '---', '- -', '- -', '- -', '- -'): 20,
              ('---', '- -', '---', '- -', '- -', '---'): 21,
              ('---', '- -', '- -', '---', '- -', '---'): 22,
              ('---', '- -', '- -', '- -', '- -', '- -'): 23,
              ('- -', '- -', '- -', '- -', '- -', '---'): 24,
              ('---', '---', '---', '- -', '- -', '---'): 25,
              ('---', '- -', '- -', '---', '---', '---'): 26,
              ('---', '- -', '- -', '- -', '- -', '---'): 27,
              ('- -', '---', '---', '---', '---', '- -'): 28,
              ('- -', '---', '- -', '- -', '---', '- -'): 29,
              ('---', '- -', '---', '---', '- -', '---'): 30,
              ('- -', '---', '---', '---', '- -', '- -'): 31,
              ('- -', '- -', '---', '---', '---', '- -'): 32,
              ('---', '---', '---', '---', '- -', '- -'): 33,
              ('- -', '- -', '---', '---', '---', '---'): 34,
              ('---', '- -', '---', '- -', '- -', '- -'): 35,
              ('- -', '- -', '- -', '---', '- -', '---'): 36,
              ('---', '---', '- -', '---', '- -', '---'): 37,
              ('---', '- -', '---', '- -', '---', '---'): 38,
              ('- -', '---', '- -', '---', '- -', '- -'): 39,
              ('- -', '- -', '---', '- -', '---', '- -'): 40,
              ('---', '- -', '- -', '- -', '---', '---'): 41,
              ('---', '---', '- -', '- -', '- -', '---'): 42,
              ('- -', '---', '---', '---', '---', '---'): 43,
              ('---', '---', '---', '---', '---', '- -'): 44,
              ('- -', '---', '---', '- -', '- -', '- -'): 45,
              ('- -', '- -', '- -', '---', '---', '- -'): 46,
              ('- -', '---', '---', '- -', '---', '- -'): 47,
              ('- -', '---', '- -', '---', '---', '- -'): 48,
              ('- -', '---', '---', '---', '- -', '---'): 49,
              ('---', '- -', '---', '---', '---', '- -'): 50,
              ('- -', '- -', '---', '- -', '- -', '---'): 51,
              ('---', '- -', '- -', '---', '- -', '- -'): 52,
              ('---', '---', '- -', '---', '- -', '- -'): 53,
              ('- -', '- -', '---', '- -', '---', '---'): 54,
              ('- -', '- -', '---', '---', '- -', '---'): 55,
              ('---', '- -', '---', '---', '- -', '- -'): 56,
              ('---', '---', '- -', '---', '---', '- -'): 57,
              ('- -', '---', '---', '- -', '---', '---'): 58,
              ('- -', '---', '- -', '- -', '---', '---'): 60,
              ('---', '---', '- -', '- -', '---', '- -'): 61,
              ('- -', '- -', '---', '---', '- -', '- -'): 62,
              ('- -', '---', '- -', '---', '- -', '---'): 63,
              ('---', '- -', '---', '- -', '---', '- -'): 64}                       # 64 heksagramy


                 ########Rzuty monetami-Losowanie wróżby##########

MONETA = ["Orzeł", "Reszka"]
RZUTY = [["".join(random.choice(MONETA)) for t in range(3)] for y in range(6)]


X = 0
for t in RZUTY:
    if RZUTY[X].count('Orzeł') == 0:
        WROZBA.append('---')
    elif RZUTY[X].count('Reszka') == 0:
        WROZBA.append('- -')
    elif RZUTY[X].count('Reszka') == 1:
        WROZBA.append('- -')
    else: WROZBA.append('---')
    X += 1

                  #######Drukowanie wrózby#######
Y = 0
for t, n in enumerate(RZUTY):
    print('Rzut nr:', (t+1), n, '\t', WROZBA[Y])
    Y += 1
    time.sleep(1)


X = 0
print("*"*20)
while X != 6:        #petla printujaca wylosowany heksagram
    print("*      ", WROZBA[X], "       *")
    X += 1
print("*"*20)


H = {str(WROZBA): '1'}     # tworzenie slownika wrozby
print("*", "Heksagram nr:", HEKSAGRAMY.get(tuple(WROZBA)), "*", "\n")  #wartosc klucza slownika heksagramy

NUM = int(HEKSAGRAMY.get(tuple(WROZBA)))

with open(f"{NUM}.txt", "r", encoding="utf-8", errors='ignore') as t:
    print(t.read())


input("\n Wciśnij Enter aby zakończyć.")
