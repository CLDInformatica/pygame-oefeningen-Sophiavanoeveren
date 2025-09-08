# Bekijk de voorbeelden en verander de functies
# Maak vervolgens de opdracht hieronder
# Voorbeeld1
def rekenen1():
  getal1 = 50
  getal2 = 5
  return getal1 + getal2

def rekenen2():
  getal1 = 50
  getal2 = 5
  return getal1 - getal2

def rekenen3():
  getal1 = 50
  getal2 = 5
  return getal1 * getal2

getal = rekenen2()
print(getal)

# Voorbeeld2
def locatie(land):
  print("Ik kom uit " + land)

locatie("Amerika")

# Voorbeeld3
def kwadraat(getal):
  resultaat = getal * getal
  return resultaat

mijnKwadraat = kwadraat(4)
print(mijnKwadraat)


# Maak 5 functies die allemaal in een andere taal "Goedemorgen" printen.
# Roep daarna elke functie minimaal 2 keer aan (callen) waardoor er minimaal 10 keer "Goedemorgen" naar de console wordt geprint!

def goedemorgen_nederlands():
  print("Goedemorgen")

def goedemorgen_spaans():
  print("Buenos días")

def goedemorgen_frans():
  print("Bonjour")

def goedemorgen_duits():
    print("Guten morgen")

def goedemorgen_engels():
  print("Goodmorning")

goedemorgen_nederlands()
goedemorgen_nederlands()
goedemorgen_spaans()
goedemorgen_spaans()
goedemorgen_frans()
goedemorgen_frans()
goedemorgen_duits()
goedemorgen_duits()
goedemorgen_engels()
goedemorgen_engels()
