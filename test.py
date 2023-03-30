import pymorphy2

# Абдуллин Кирилл
# Маренич Элия
# Хан Арсений
# Борисюк Екатерина
morph = pymorphy2.MorphAnalyzer()
list_of_names = ['Абдуллин Кирилл', 'Маренич Элия', "Хан Арсений", "Борисюк Екатерина"]
all_names = ""
for names in list_of_names:
    name_in_dat_padezh = ""
    print(morph.parse(names.split()[1])[0])
    if morph.parse(names.split()[1])[0].tag.gender == "masc":
        case = 'masc'
    else:
        case = "femn"
    print(case)
    for word in names.split():
        name = morph.parse(word)[0]
        name_in_dat_padezh += name.inflect({"datv", case}).word.capitalize() + " "
    all_names += name_in_dat_padezh + "\n"
print(all_names)