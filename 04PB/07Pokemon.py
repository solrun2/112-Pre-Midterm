pokemon_level = int(input("Enter level pokemon: "))
pokeball_level = input("Enter level pokeball: ")
distance = int(input("Enter distance: "))
if pokeball_level == "H" or pokeball_level == "h" :
    x = 0.01
elif pokeball_level == "M" or pokeball_level == "m" :
    if 0 <= pokemon_level <= 40 :
        x = 0.03
    elif 41 <= pokemon_level <= 60 :
        x = 0.05
    elif 61 <= pokemon_level <= 100 :
        x = 0.08
elif pokeball_level == "L" or pokeball_level == "l" :
    if 0 <= pokemon_level <= 40 :
        x = 0.05
    elif 41 <= pokemon_level <= 60 :
        x = 0.03
    elif 61 <= pokemon_level <= 100 :
        x = 0.1
s = 100 - (pokemon_level * distance * x)
if s < 0 :
    s = 0
print("{:.2f} percent.".format(s))