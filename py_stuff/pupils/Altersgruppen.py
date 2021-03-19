#Definition Altersgruppen

alter_0_14 = 12.3
alter_15_49 = 39.1
alter_50_65 = 15.5
alter_über_65 = 16.3
startjahr = 2005
endjahr = 2021

#Definition Altersänderung

# for i in range(startjahr, endjahr-startjahr):


bleiben_0_14 = alter_0_14 * 0.93 + 0.02 * alter_15_49
werden_15_49 = alter_0_14 * 0.066

bleiben_15_49 = alter_15_49 * 0.97
werden_50_65 = alter_15_49 * 0.029

bleiben_50_65 = alter_50_65 * 0.925
werden_über_65 = alter_50_65 * 0.066

bleiben_über_65 = alter_über_65 * 0.972

#Anzeige der Zahlen

print(f"In der Altersgruppe 0-14 bleiben {bleiben_0_14} Menschen.")

print()

print(f"Aus der Altersgruppe 0-14 werden {werden_15_49} Menschen 15.")

print()

print(f"In der Altersgruppe 15-49 bleiben {bleiben_15_49} Menschen.")

print()

print(f"Aus der Altersgruppe 15-49 werden {werden_50_65} Menschen 50.")

print()

print(f"In der Altersgruppe 50-65 bleiben {bleiben_50_65} Menschen.")

print()

print(f"Aus der Altersgruppe 50-65 werden {werden_über_65} älter als 65.")

print()

print("Angaben in Millionen.")

#Frage: Wie kann man Zahlen runden lassen. "round" funktioniert nicht.