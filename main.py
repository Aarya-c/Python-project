#Importing
import datetime
import operations
import read
import write


loop = True
while loop == True:
    operations.welcome()

    operations.Demonstratingmessages()
    
    selectedOption = int(input("Enter a option: "))
    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    if selectedOption == 1:
        tempSellBill = []
        loop1=True
        while loop1==True:
            print("\n")
            print("Let's trade a Laptop :)")
            print("\n")
            fileContent = read.getFileContent()
            mainData = operations.getDictionary(fileContent)
            printing = operations.printLaptops(mainData)
            SNo = operations.getValidSno(mainData)
            quantity = operations.getValidQuantity(mainData,SNo)
            tempSellBill.append([mainData[SNo][0], mainData[SNo][1], mainData[SNo][2], quantity])
        
            userSellsLaptops = True
            
           
    
            while userSellsLaptops == True:
              
                
                valid_input = False
                while valid_input == False:
                    wantAnother = input("Do you want to sell more(yes/no)? ")
                    if wantAnother.lower() == "yes":
                        print("\n")        
                      
                        print("\n")
                        valid_input = True
                        userSellsLaptops = False
                        break
                    elif wantAnother.lower() == "no":
                        print("\n")
                        write.generateBill(tempSellBill)
                        loop1=False
                        userSellsLaptops = False
                        valid_input = True
                    else:
                        print("Invalid Input !!")
                        print("\n")
                        continue 
                write.updateTextFile(mainData)
                print("\n")

    elif selectedOption == 2:
        tempSellBill = []
        loop1=True
        while loop1==True:
            print("\n")
            print("Let's purchase a Laptop :)")
            print("\n")
            fileContent = read.getFileContent()
            mainData = operations.getDictionary(fileContent)
            laptop_print=operations.printLaptops(mainData)
            purchase_id = operations.purchaseIDvalid(mainData)
            quantity = operations.getValidManufactureQuantity(mainData,purchase_id)
            userBuysLaptops = True
 
    
            while userBuysLaptops == True:
                print(laptop_print)
                tempSellBill.append([mainData[purchase_id][0], mainData[purchase_id][1], mainData[purchase_id][2], quantity])


                valid_input = False
                while valid_input == False:
                    buyAnother = input("Do you want to purchase more(yes/no)? ")
                    if buyAnother.lower() == "yes":
                        print("\n")
                        valid_input = True
                        userBuysLaptops=False
                        break
                    elif buyAnother.lower() == "no":
                        print("\n")
                        write.generateBuyBill(tempSellBill)
                        loop1=False
                        userBuysLaptops = False
                        valid_input = True
                    else:
                        print("Kindly select an option from the choices provided!!")
                        print("\n")
                        continue 
                write.updateTextFile(mainData)
                print("\n")
        
              
    elif selectedOption == 3:
        print("\n")
        print("**********************************************************************************************************************************")
        print("\n")
        print("\n")
        print("         Greetings and thank you for visiting our store :)")
        print("\n")
        print("\n")
        print("**********************************************************************************************************************************")
        loop=False

    else:
        print("\n")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("\n")
        print("Invalid input! :( ")
        print("\n")
        print("5)")
        print("\n")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            
        
