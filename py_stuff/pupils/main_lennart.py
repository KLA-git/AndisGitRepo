alter14 = 12.3
alter49 = 39.1
alter64 = 15.5
alter65 = 16.3

startJahr = 2005


while startJahr < 2100:
    startJahr = startJahr + 1
    print(

        "Jahr " + str(startJahr) + ": " + "\n" +
        "0-14 Jahre: " + str(alter14) + "\n" +
        "15-49 Jahre: " + str(alter49) + "\n" +
        "50-64 Jahre: " + str(alter64) + "\n" +
        "65 Jahre: " + str(alter65) + "\n"

    )
    alter14 = alter14 * 0.93 + (alter49 * 0.02)
    alter49 = alter14 * 0.066 + (alter49 * 0.97)
    alter64 = alter49 * 0.029 + alter64 * 0.925
    alter65 = alter64 * 0.066 + alter65 * 0.972

