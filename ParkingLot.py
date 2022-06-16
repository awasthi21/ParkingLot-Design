from Slot import slot
import person

class ParkingLot:
  def __init__(self,numSlots):
    self.numSlots=numSlots
    self.slots=[slot(i) for i in range(1,self.numSlots+1)]
    print("Created parking of {} slots".format(numSlots))
  
  def Park(self,age,vechileRegistrationNumber):
    driver=person.Driver(age,vechileRegistrationNumber)
    for i in range(1,self.numSlots+1):
      if self.slots[i-1].getStatus()==False:
        self.slots[i-1].allot(driver)
        print("Car with vehicle registration number "+vechileRegistrationNumber+" has been parked at slot number "+str(i))
        return 
    print("Parking Lot Full")
    

  def leaveSlot(self,slotNumber):
    if slotNumber>self.numSlots:
      return
    self.slots[slotNumber-1].freeSlot()
    
  def getSlotNumberForGivenRegistationNumber(self,vechileRegistrationNumber):
    for i in range(1,self.numSlots+1):
      if self.slots[i-1].getStatus()==True:
        if self.slots[i-1].allotedto.getVechileRegistrationNumber()==vechileRegistrationNumber:
          print(i)
          return
  def getSlotNumberForGivenAge(self,age):
    ans=[]
    for i in range(1,self.numSlots+1):
      if self.slots[i-1].getStatus()==True:
        if self.slots[i-1].allotedto.getAge()==age:
          ans.append(i)
    print(",".join(str(ele) for ele in ans))

  def getVechileRegistrationNumberForDriverOfAge(self,age):
    ans=[]
    for i in range(1,self.numSlots+1):
      if self.slots[i-1].getStatus()==True:
        if self.slots[i-1].allotedto.getAge()==age:
          ans.append(self.slots[i-1].allotedto.getVechileRegistrationNumber())
    print(",".join(str(ele) for ele in ans))
  
  
  
  
    
    