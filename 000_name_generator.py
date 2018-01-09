import random
import sys

female_names = ['Anna', 'Maria','Katarzyna','Małgorzata','Agnieszka','Krystyna','Barbara','Ewa','Elżbieta','Zofia','Janina','Teresa','Joanna','Magdalena','Monika',
'Jadwiga','Danuta','Irena','Halina','Helena','Beata','Aleksandra','Marta','Dorota','Marianna','Grażyna','Jolanta',
'Stanisława','Iwona','Karolina','Bożena','Urszula','Justyna','Renata','Alicja','Paulina','Sylwia','Natalia',
'Wanda','Agata','Aneta','Izabela','Ewelina','Marzena','Wiesława','Genowefa','Patrycja','Kazimiera','Edyta','Stefania']


male_names = [
'Jan','Andrzej','Piotr','Krzysztof','Stanisław','Tomasz','Paweł','Józef','Marcin','Marek','Michał','Grzegorz','Jerzy','Tadeusz','Adam',
'Zbigniew','Ryszard','Dariusz','Henryk','Mariusz','Kazimierz','Wojciech','Robert','Mateusz','Marian','Rafał','Jacek','Janusz','Mirosław','Maciej',
'Sławomir','Jarosław','Kamil','Wiesław','Roman','Władysław','Jakub','Artur','Zdzisław','Edward','Mieczysław','Damian','Dawid','Przemysław',
'Sebastian','Czesław','Leszek','Daniel','Waldemar']

surnames = [
'Nowak','Kowalski','Wiśniewski','Dąbrowski','Lewandowski','Wójcik','Kamiński','Kowalczyk','Zieliński','Szymański','Woźniak','Kozłowski','Jankowski','Wojciechowski','Kwiatkowski','Kaczmarek','Mazur','Krawczyk','Piotrowski','Grabowski',
'Nowakowski','Pawłowski','Michalski','Nowicki','Adamczyk','Dudek','Zając','Wieczorek','Jabłoński','Król','Majewski','Olszewski','Jaworski','Wróbel',
'Malinowski','Pawlak','Witkowski','Walczak','Stępień','Górski','Rutkowski','Michalak','Sikora','Ostrowski','Baran','Duda',
'Szewczyk','Tomaszewski','Pietrzak','Marciniak','Wróblewski','Zalewski','Jakubowski','Jasiński','Zawadzki','Sadowski','Bąk','Chmielewski','Włodarczyk',
'Borkowski','Czarnecki','Sawicki','Sokołowski','Urbański','Kubiak','Maciejewski','Szczepański','Kucharski','Wilk','Kalinowski','Lis','Mazurek',
'Wysocki','Adamski','Kaźmierczak','Wasilewski','Sobczak','Czerwiński','Andrzejewski','Cieślak','Głowacki','Zakrzewski','Kołodziej',
'Sikorski','Krajewski','Gajewski','Szymczak','Szulc','Baranowski','Laskowski','Brzeziński','Makowski','Ziółkowski','Przybylski'
]

def generate_random_female_name():
    index = random.randint(0, len(female_names))
    return female_names[index]

def generate_random_male_name():
    index = random.randint(0, len(male_names))
    return male_names[index]

def generate_random_male_surname():
    index = random.randint(0, len(surnames))
    return surnames[index]
def generate_random_female_surname():
    index = random.randint(0, len(surnames))
    female_surname = surnames[index]
    if female_surname[-2:] == 'ki':
        female_surname = female_surname.replace('ki', 'ka')
    return female_surname


while True:
    gender = input('What name do you want to generate? [MALE/FEMALE]')
    if gender == 'FEMALE' or gender == 'female':
        print(gender)
        print('Your random Polish name is: ')
        print(generate_random_female_name())
        print(generate_random_female_surname())
    elif gender == 'MALE' or gender == 'male':
        print(gender)
        print('Your random Polish name is: ')
        print(generate_random_male_name())
        print(generate_random_male_surname())
    else:
        print("Please enter MALE or FEMALE")

    again = input('Do you want to generate a name again? [YES/NO]')
    if again == 'NO' or again == 'no':
        break