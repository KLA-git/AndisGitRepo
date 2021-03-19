startYear = 2005
endYear = 2022

# Start values
age0_14 = 12.3
age15_49 = 39.1
age50_64 = 15.5
age_over_65 = 16.3

year = startYear

for x in range(0, (endYear - startYear)+1):
    # Results are rounded to 6 digits
    print(
        "Jahr " + str(year) + "\n" +
        "0-14 Jahre: " + str(round(age0_14, 6)) + " Mil" + "\n" +
        "15-49 Jahre: " + str(round(age15_49, 6)) + " Mil" + "\n" +
        "50-64 Jahre: " + str(round(age50_64, 6)) + " Mil" + "\n" +
        "Über 65 Jahre: " + str(round(age_over_65, 6)) + " Mil" + "\n" +
        "Insgesamt: " + str(round(age0_14 + age15_49 + age50_64 + age_over_65, 6)) + " Mil" + "\n"
    )
    year = year + 1  # Count to Next Year

    age0_14 = (age0_14 + age15_49 * (2 / 100))  # Add 2% from age15_49 to age0_14
    age0_14 = age0_14 * (93 / 100)  # Remove 7% from age age0_14


    age15_49 = age15_49 + age0_14 * (6.6 / 100)  # Add 6.6% from age0_14 to age15_49
    age15_49 = age15_49 * (97 / 100)  # Remove 3% from age age15_49

    age50_64 = age50_64 + age15_49 * (2.9 / 100)  # Add 2.9% from age15_49 to age50_64
    age50_64 = age50_64 * (92.5 / 100)  # Remove 7.5% from age age50_64

    age_over_65 = age_over_65 + age50_64 * (6.6 / 100)  # Add 6.6% from age50_64 to age_over_65
    age_over_65 = age_over_65 * (97.2 / 100)  # Remove 2.8% from age age_over_65
