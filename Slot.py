class slot:
  def __init__(self,slotNumber):
    self.__isBooked=False
    self.__slotNumber=slotNumber
    self.allotedto=None
  def getStatus(self):
    return self.__isBooked
  def setStatus(self,status):
    self.__isBooked=status
  def getSlotNumber(self):
    return self.__slotNumber

  def allot(self,driver):
    self.allotedto=driver
    self.setStatus(True)

  def freeSlot(self):
    if self.getStatus()==False:
      print("Slot already vacant")
    else:
      self.setStatus(False)
      print("Slot number "+str(self.getSlotNumber())+" vacated, the car with vehicle registration number "+self.allotedto.getVechileRegistrationNumber()+" left the space, the driver of the car was of age "+str(self.allotedto.getAge()))
      self.allotedto=None
      
  
  