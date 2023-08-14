import csv
from src.cShip import cShip
from src.cCargo import cCargo
from src.cCruise import cCruise

def main() -> None:
  ships = []
  with open("ships.csv") as file:
    reader = csv.reader(file)
    next(file)
    for row in reader:

      if (row[2] == '' and row[3] == ''):
        shipaux = cShip(row[0],row[1])
        ships.append(shipaux)
        #print("cree un ship")

      elif (row[2]!= '' and row[3] == ''):
        cruiseaux = cCruise(row[2],row[0],row[1])
        ships.append((cruiseaux))
        #print("cree un cruise")

      else:
        cargoaux = cCargo(row[2],row[3],row[0],row[1])
        ships.append(cargoaux)
        #print("cree un cargo")

  print("Numero de barcos",cShip.cantBarcos)
  for i in range(len(ships)):
    try:
      loot = ships[i].is_worth_it()
      print("draft",ships[i].draft,"Merece ser robado")
    except Exception:
      print("draft",ships[i].draft,"No vale la pena ser robado")

if __name__ == "__main__":
  main()