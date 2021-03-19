# Populationsentwicklung

#Eingabe
jahre= int(input("Bitte geben Sie das gewünschte Jahr in der Form 0000 ein!    "))
if jahre <= 2005: print("Die Eingabe ist fehlerhaft. Bitte versuchen Sie es erneut")
ausf= jahre-2005 #Anzahl der Jahre, die berechnet werden sollen. (Schleifendurchläufe)

#Startwerte
g_0_14 = float(12.3)
g_15_49 = float(39.1)
g_50_64 = float(15.5)
g_65 = float(16.3)
gest=0

# Verarbeitung
schritt = 0
while schritt < ausf:
    hilf=g_0_14*0.93+(g_15_49*0.02)
    g_15_49=g_15_49*0.97+(g_0_14*0.06)-(g_15_49*0.029)
    g_50_64=g_50_64*0.925+(g_15_49*0.029)-(g_50_64*0.066)
    g_65=g_65*0.972+(g_50_64*0.066)
    g_0_14= hilf
    schritt=schritt+1



# Ausgabe
print('')

print('Anzahl der Jahre nach 2005: ', schritt)
print('Anzahl Menschen zwischen 0 und 14 in Millionen: ', g_0_14)
print('Anzahl Menschen zwischen 15 und 49 in Millionen: ', g_15_49)
print('Anzahl Menschen zwischen 50 und 64 in Millionen: ', g_50_64)
print('Anzahl Menschen über 65 in Millionen: ', g_65)

#g_0_14 Jahre -> 93 % bleiben
#g_15_49 Jahre-> 97% bleiben + 6% g_0_14 Jahre+ (g_0_14* 2%)
#g_50_64 Jahre -> 92,5% bleiben+ 29% g_15_49
#g_65 Jahre -> 97,2% bleiben+ 6% g_50_64