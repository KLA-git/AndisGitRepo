from string import ascii_letters

import csv

# Start und Ende der benötigten Jahrgangsstufen
class_range_start = 5
class_range_end = 13

letter_start = "A"
letter_end = "D"
letters_per_class = ""

name_of_new_course = "Klassenleiterstunde"


# hier werden die Züge generiert und in letters per class
def range_alpha(start_letter, end_letter):
    return ascii_letters[
           ascii_letters.index(start_letter):ascii_letters.index(end_letter) + 1
           ]


# Hilfsvariable für die for-schleife Abspeichern der Literale für die Klassenzüge
letters_per_class = range_alpha(letter_start, letter_end)
# Liste für die fertigen Zeilen (generierten Klassen: 07A, 07B, 07C, ...
generated_classes = []

# generieren der fertigen Klassen und appenden an die Liste generated_classes
for y in range(class_range_start, class_range_end + 1):
    for x in range(len(letters_per_class)):
        if (y < 10):
            generated_classes.append(f"0{y}{letters_per_class[x]}")
        else:
            generated_classes.append(f"{y}{letters_per_class[x]}")

# datei = open('courses_out.csv','w')
with open('courses_out.csv', 'w') as f:
    for x in generated_classes:
        f.write(f"\r\n{name_of_new_course} {x},{name_of_new_course} {x},,self,teacher")

with open('courses_out.csv', 'r') as f:
    lines = f.readlines()
    lines[0] = "shortname,fullname,category,enrolment_1,enrolment_1_role\r\n"


with open('courses_out.csv', 'w') as f:
    f.writelines(lines)
