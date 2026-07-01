#Sozdanie sluchainogo chisla
import random

iskomoe = str (random.randint(0,999))#Generacija sluchainogo chisla ot 0 do 999
#print(iskomoe) #Udalit`


dlina= len( iskomoe )
#print( dlina )#Udalit`
while dlina <3:
   iskomoe = "0"+iskomoe
   dlina = len(iskomoe)
   #print( iskomoe ) #Udalit`

list_iskomoe = [iskomoe]
#print(list_iskomoe [0][0])

popitok=11
while popitok > 0:
    popitok -= 1

    if popitok == 0 :
        print( '\nПоражение!!!' )
        print('\nКонец игры')
        print("Искомое число: ", iskomoe)
        break
    elif popitok == 1 :
        formulirovka = ' попытка'
    elif popitok == 2 or popitok == 3 or popitok == 4 :
        formulirovka = ' попытки'
    else:
        formulirovka = ' попыток'
    print( '\nОсталось ', popitok, formulirovka)
    versija = input('Введите число: ')
    if len( versija ) != 3:
        print("Можно вводить только целые числа в диапазоне от 001 до 999!")
        continue
    #Proverka na chislitelnoe
    try:
        vers_proverka = int( versija )
    except:
        print("Можно вводить только целые числа в диапазоне от 001 до 999!")
        continue

    #Sravnenie strokovoj iskomoe i versija
    if str( versija ) == iskomoe:
        print("\nВы победили!" )
        print("\nИскомое число: ", versija )
        break
    #Sravnenie na pozicijah
    list_versija = [versija]

    if list_versija [0][0]  == list_iskomoe [0][0] or list_versija [0][1]  == list_iskomoe [0][1] or list_versija [0][2]  == list_iskomoe [0][2]:
        print ("\nСовпадение по месту!")
        continue

    #Sravnenie mnovestvo_iskomoe i mnozestvo versija
    if list_versija [0][0]  == list_iskomoe [0][1] or list_versija [0][0]  == list_iskomoe [0][2]:
        print ("\nСовпадение по знаку!")
        continue
    if list_versija [0][1]  == list_iskomoe [0][0] or list_versija [0][1]  == list_iskomoe [0][2]:
        print ("\nСовпадение по знаку!")
        continue
    if list_versija [0][2]  == list_iskomoe [0][0] or list_versija [0][2]  == list_iskomoe [0][1]:
        print ("\nСовпадение по знаку!")
        continue
    else:
        print("Совпадений нет.")