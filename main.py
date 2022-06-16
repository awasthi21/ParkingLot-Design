from route import Routes
from ParkingLot import ParkingLot
file1 = open('input.txt', 'r')
Lines = file1.readlines()
Parking_Lot=None
for lines in Lines:
  ls=lines.split()
  if ls[0]=='Create_parking_lot':
    Parking_Lot=ParkingLot(int(ls[1]))
  else:
    Routes(ls,Parking_Lot)