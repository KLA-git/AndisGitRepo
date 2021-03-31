from string import ascii_letters

# Start und Ende der benötigten Jahrgangsstufen
class_range_start = 6
class_range_end = 6

letter_start = "A"
letter_end = "F"
count = 0
for l in ascii_letters:
    if (l == letter_end):
        break
    else:
        count = count + 1

durchlaufe = (class_range_end - class_range_start + 1) * count

name_of_new_course = "Abstimmung Wintersportwoche 6"

kursIDsDict = {

}


# hier werden die Züge generiert und in letters per class
def range_alpha(start_letter, end_letter):
    return ascii_letters[
           ascii_letters.index(start_letter):ascii_letters.index(end_letter) + 1
           ]


# Hilfsvariable für die for-schleife Abspeichern der Literale für die Klassenzüge
letters_per_class = range_alpha(letter_start, letter_end)

# Liste für die fertigen Zeilen (generierten Klassen: 07A, 07B, 07C, ...
generated_classes = []

# Dictionary anlegen, in welcher die ID der Klasse zugeordnet wird, der Art: (11A, 245)
with open("../data/overview_KursIDs_moodle.html", mode="r") as f:
    content = f.readlines()
    for i in content:
        lines = i.split(" ")
        klasse = lines[-1]
        klasse = klasse[0:3]
        # print(klasse)
        courseID = lines[22]
        courseID = courseID[7:10]
        # print(courseID)
        if (kursIDsDict.__contains__(klasse) == False):
            kursIDsDict[klasse] = courseID
        else:
            continue
    for item in kursIDsDict.items():
        print(item)
    f.close()

# generieren der fertigen Klassen und appenden an die Liste generated_classes
y: int
for y in range(class_range_start, class_range_end + 1):
    for x in range(len(letters_per_class)):
        if y < 10:
            generated_classes.append(f"0{y}{letters_per_class[x]}")
        else:
            generated_classes.append(f"{y}{letters_per_class[x]}")

with open('courses_out.csv', 'w+') as f:
    for x in generated_classes:
        #    f.write(f"\r\n{name_of_new_course} {x},{name_of_new_course} {x},{kursIDsDict[x]},self,teacher")
        f.write(f"\r\n{name_of_new_course} {x},{name_of_new_course} {x},{kursIDsDict[x]}")
    f.seek(0)
    lines = f.readlines()
    print(len(lines))
    f.seek(0)
    #  lines[0] = "shortname,fullname,category,enrolment_1,enrolment_1_role\r\n"
    lines[0] = "shortname,fullname,category\r\n"
    f.writelines(lines)
    f.close()
