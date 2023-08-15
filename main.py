import csv
from src.cShip import cShip
from src.cCargo import cCargo
from src.cCruise import cCruise

def isNumeric(aux):
  try:
    float(aux)
    return True
  except ValueError:
    return False

def main() -> None:
  ships = []
  with open("ships.csv") as file:
    reader = csv.reader(file)
    next(file)
    for row in reader:

      if (row[2] == '' and row[3] == ''):
        if isNumeric(row[0]) and isNumeric(row[1]):
          shipaux = cShip(row[0],row[1])
          ships.append(shipaux)
        #print("cree un ship")

      elif (row[2]!= '' and row[3] == ''):
        if isNumeric(row[2]) and isNumeric(row[0]) and isNumeric(row[1]):
          cruiseaux = cCruise(row[2],row[0],row[1])
          ships.append((cruiseaux))
        #print("cree un cruise")

      else:
        if row[2]== '':
          row[2]=0
        if isNumeric(row[3]) and isNumeric(row[0]) and isNumeric(row[1]):
          cargoaux = cCargo(row[2],row[3],row[0],row[1])
          ships.append(cargoaux)
        #print("cree un cargo")

  print("Numero de barcos", cShip.cantBarcos)
  for i in range(len(ships)):
    try:
      loot = ships[i].is_worth_it()
      print("Barco nº",i+1,"Merece ser robado")
    except Exception:
      print("Barco nº",i+1,"No vale la pena ser robado")

if __name__ == "__main__":
  main()