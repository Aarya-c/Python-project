
def welcome():

    """Upon starting the software, a welcome screen will show."""
    
    print("*******************************************************************************")
    print()
    print("        Welcome user to the laptop shop  ")
    print("          Developed by Arya Chaudhary : ")
    print()
    print("*******************************************************************************")


def Demonstratingmessages():
    
    """An introductory screen will appear upon launching the program."""

  
    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Select a desirable option")
    print("(1) || Press 1 to sell a Laptop to customers.")
    print("(2) || Press 2 to purchase a Laptop from manufacturer.")
    print("(3) || Press 3 to exit.")





def getDictionary(fileContent):

    """Here, We are organizing the data from a list into a dictionary."""
    
    data = {}
    for index in range(len(fileContent)):
        data[index+1] = fileContent[index].replace("\n","").split(",")
    return data


def printLaptops(mainData):
  
    """Here, we are constructing a table to improve the user experience."""
  
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("S.No.", "\t", "Laptop name", "\t\t\t", "Brand", "\t\t\t", "Price", "\t\t\t", "Quantitiy","\t" , "Generation","\t\t", "GPU")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for key,value in mainData.items():
        print(str(key)+str("."), "\t" , value[0], "\t\t", value[1], "\t\t", value[2], "\t\t", value[3],"\t\t", value[4],"\t\t",value[5])
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    return ""

#this code is for sale.........

def getValidSno(mainData):
    
    """We are confirming the serial number's authenticity."""
  
    validSno = False
    while validSno == False:
        SNo = input("Please input the serial number: ")
        try:
            if SNo.isdigit():
                SNo = int(SNo)
                if SNo > 0 and SNo <= len(mainData):

                    if int(mainData[SNo][3]) == 0:
                        print()
                        print("laptop is out of stock!")
                        print("\n")
                        print("Try another!")
                        print()
                        print(printing)
                        continue
        
                    else:
                        validSno = True
                        print(f"The serial number of the laptop is {SNo}.")
                        print()
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("\n")
                        print("       The laptop is currently in stock and ready for purchase.           ")
                        print("\n")
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("\n")
                        return SNo
        
                else:
                    print("The entered number is not one of the valid choices.")
                    print("\n")
          
            else:
                print("Kindly enter one of the numbers provided.")
                print("\n")
      
        except:
            print("Invalid Serial Number!")


def getValidQuantity(mainData,SNo):
  
    """We are verifying the quantity of laptops that are available for sale."""
  
    tempSellBill = []
    validQuantity = False

    while validQuantity == False:
        print("**********************************************************************************************")
        print("\n")
        quantity = input("Enter the total number of laptops you want to sell: ")
        print("\n")
        print("**********************************************************************************************")
        try:
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0 and quantity <= int(mainData[SNo][3]):
                    validQuantity = True
                    mainData[SNo][3] = str(int(mainData[SNo][3]) - quantity)
                    return quantity
                else:
                    print("The quantity requested exceeds our current inventory..")
                    print("Please enter a quantity that does not exceed our available stock.")
                    print("\n")
            else:
                print("Kindly enter one of the available numbers.")
                print("\n")
        except:
            print("Invalid Quantity!")
            

 # This code is for purchase           

def purchaseIDvalid(mainData):

    """we are verifying the authenticity of the serial number."""
    
    validId = False
    while validId == False:
        ID = input("Enter the laptop ID to purchase: ")
        if ID.isdigit():
            ID = int(ID)
            if ID > 0 and ID <= len(mainData):
                validID = True
                return ID
                break    
            else:
                print("The number you have entered is not among the available choices.")
                print("\n")
        else:
            print("Kindly enter one of the available numbers.")
            print("\n")

    

def getValidManufactureQuantity(mainData,purchase_id):

    """we are validating the quantity of laptops that will be purchased."""
    
    
    validQuad = False
    while validQuad == False:
        quantity = input("Please provide the number of items you wish to purchase: ")
        if quantity.isdigit():
            quantity = int(quantity)
            if quantity > 0 :
                mainData[purchase_id][3] = int(mainData[purchase_id][3]) + int(quantity)
                validQuad = True
                return quantity
            else:
                print("Kindly enter one of the available numbers!")
                print("\n")
            
        else:
            print("Kindly enter one of the available numbers!")
            print("\n")




# This is for sale........



            

