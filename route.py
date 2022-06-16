def Routes(string,Parking_Lot):
  if string[0]=="Park":
    Parking_Lot.Park(int(string[3]),string[1])
  elif string[0]=='Vehicle_registration_number_for_driver_of_age':
    Parking_Lot.getVechileRegistrationNumberForDriverOfAge(int(string[1]))
  elif string[0]=='Leave':
    Parking_Lot.leaveSlot(int(string[1]))
  elif string[0]=='Slot_number_for_car_with_number':
    Parking_Lot.getSlotNumberForGivenRegistationNumber(string[1])
  elif string[0]=="Slot_numbers_for_driver_of_age":
    Parking_Lot.getSlotNumberForGivenAge(int(string[1]))
  else:
    print("Invalid Command")
    return
    
    