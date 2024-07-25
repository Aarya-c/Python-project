import datetime
import random
#this code will generate bill for purchase
def generateBuyBill(tempSellBill):
    
    """Here, We are creating a bill for the purchase in both sehell and text file formats."""
    
    validName = False
    while validName == False:
        Name = str(input("Please enter your name: "))
        if Name.replace(" ", "").isalpha():
            validName = True
        else:
            print("Sorry, You typed your name incorrectly!")
            print("\n")
              
          
    validPhoneNumber = False
    while validPhoneNumber == False:
        phoneNumber = str(input("Enter your Phone Number: "))
        if phoneNumber.isdigit():
            validPhoneNumber = True
        else:
            print("Sorry, You typed your Phone Number incorrectly!")
            print("\n")
    
    Address = str(input("Enter your address: "))
    GST = random.randint(1000, 5000)
    Year = (datetime.datetime.now().year)
    Month = (datetime.datetime.now().month)
    Day = (datetime.datetime.now().day)
    Hour = (datetime.datetime.now().hour)
    Minute = (datetime.datetime.now().minute)
    Second = (datetime.datetime.now().second)
    microSecond = (datetime.datetime.now().microsecond)
    print("\n")
    print("**********************************************************************************************************************************************")
    print("\n")
    print("----------------------------------------------laptop Shop-------------------------------------------------------------------------------------")
    print("                                           Kathmandu, Nepal                                              ")
    print(f"                                             GST.NO:-{GST}                                              ")
    print("----------------------------------------------Purchase Bill-----------------------------------------------------------------------------------")
    print(f"Date:- {Year}-{Month}-{Day}                                                               Time:- {Hour}:{Minute}:{Second}:{microSecond}")
    print(f"Customer Name: {Name}")
    print(f"Phone Number: {phoneNumber}")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("S.No.", "\t", "laptop Name", "\t\t\t", "Brand", "\t\t\t", "Price", "\t\t", "Quantity", "\t\t", "Amount")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    row = ""
     
    counter = 0
    finalPrice = 0
    for i in range(len(tempSellBill)):
        counter += 1
        VAT = 0.13
        for j in range(len(tempSellBill[i])):
            dollarprice = float(tempSellBill[i][2].replace("$",""))
            priceDetail = dollarprice * tempSellBill[i][3]
            row = row + str(tempSellBill[i][j]) + "\t\t"    
        print(counter,"\t",row, "\t", priceDetail)
        finalPrice = finalPrice + priceDetail
        row = ""
        VAT_amount = finalPrice * VAT
        Grand_total = finalPrice + VAT_amount
        
        
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print(f"                                         Total Price: ${finalPrice}                                       ")
    print("\n")
    print(f"                                         VAT amount is : {VAT_amount}                                       ")
    print("\n")
    print(f"                                    Grand total Price with VAT amount is : ${Grand_total}                                       ")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                    We appreciate your visit to our store!!                                      ")
    print("                                           Visit again :)                                                ")
    print()
    print("----------------------------------A bill has been created in text file as well.---------------------------------------------------------------")
    print("\n")
    print("**********************************************************************************************************************************************")

 
    #This code prints the bill in txt formate.
    text = f"Purchase-{Name}.txt"
    file = open(text,"w")
    file.write("********************************************************************************************************************************************************************************************")
    file.write("\n")
    file.write("---------------------------------------------laptop Shop------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("                                           Kathmandu, Nepal                                              ")
    file.write("\n")
    file.write(f"                                             GST.NO:-{GST}                                              ")
    file.write("\n")
    file.write("---------------------------------------------Purchase Bill----------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    
    file.write("\n")
    file.write(f"Customer Name: {Name}")
    file.write("\n")
    file.write(f"Phone Number: {phoneNumber}")
    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("S.No. \t\t laptop Name\t\t\t\t Brand \t\t\t\t price \t\t\t Quantity \t\t\t\t Amount")
    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    row = ""
     
     
    counter = 0
    finalPrice = 0
    for i in range(len(tempSellBill)):
        counter += 1
        VAT = 0.13
        for j in range(len(tempSellBill[i])):
            dollarprice = float(tempSellBill[i][2].replace("$",""))
            priceDetail = dollarprice * tempSellBill[i][3]
            row = row + str(tempSellBill[i][j]) + "\t\t\t"
        file.write(f"{counter} \t\t {row} \t\t{priceDetail}")
        file.write("\n")
        finalPrice = finalPrice + priceDetail
        row = ""
        VAT_amount = finalPrice * VAT
        Grand_total = finalPrice + VAT_amount
        
    file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write(f"                                                        Total Price: ${finalPrice}                                         ")
    file.write("\n")
    file.write(f"                                                        VAT amount is : {VAT_amount}                                         ") 
    file.write("\n")
    file.write(f"                                                 Grand total Price with VAT amount is : ${Grand_total}                                          ") 
    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("                                                  We appreciate your visit to our store!!                                       ")
    file.write("\n") 
    file.write("                                                         Visit again :)                                                ")
    file.write("\n")
    file.write("********************************************************************************************************************************************************************************************")
    file.close()







#This code will generate bill for sale

def generateBill(tempSellBill):
  
    """In this function we are passing 2d list"""
    
    validName = False
    while validName == False:
        Name = str(input("Please enter your name: "))
        if Name.replace(" ", "").isalpha():
            validName = True
            
    validPhoneNumber = False
    while validPhoneNumber == False:
        phoneNumber = str(input("Enter your Phone Number: "))
        if phoneNumber.isdigit():
            validPhoneNumber = True
        
    
    Address = str(input("Enter your address: "))
    GST = random.randint(1000, 5000)
    Year = (datetime.datetime.now().year)
    Month = (datetime.datetime.now().month)
    Day = (datetime.datetime.now().day)
    Hour = (datetime.datetime.now().hour)
    Minute = (datetime.datetime.now().minute)
    Second = (datetime.datetime.now().second)
    microSecond = (datetime.datetime.now().microsecond)
    print("\n")
    print("**********************************************************************************************************************************************")
    print("\n")
    print("---------------------------------------------laptop Shop--------------------------------------------------------------------------------------")
    print("                                           Kathmandu, Nepal                                              ")
    print(f"                                             GST.NO:-{GST}                                              ")
    print("-----------------------------------------------sell Bill--------------------------------------------------------------------------------------")
    print(f"Date:- {Year}-{Month}-{Day}                                                               Time:- {Hour}:{Minute}:{Second}:{microSecond}")
    print(f"Customer Name: {Name}")
    print(f"Phone Number: {phoneNumber}")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("S.No.", "\t", "laptop Name", "\t\t\t", "Brand", "\t\t\t", "Price", "\t\t", "Quantity", "\t\t", "Amount")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    row = ""
     
    counter = 0
    finalPrice = 0
    for i in range(len(tempSellBill)):
        counter += 1
        shipping = 10
        for j in range(len(tempSellBill[i])):
            dollarprice = float(tempSellBill[i][2].replace("$",""))
            priceDetail = dollarprice * tempSellBill[i][3]
            row = row + str(tempSellBill[i][j]) + "\t\t"    
        print(counter,"\t",row, "\t", priceDetail)
        finalPrice = finalPrice + priceDetail
        row = ""
        Grand_total = finalPrice + shipping
        
            
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print(f"                                         Total Price: ${finalPrice}                                        ")
    print("\n")
    print(f"                                       Shipping cost is :{shipping}                                        ")
    print("\n")
    print(f"                                     Grand total Price with shipping: ${Grand_total}                                        ")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                    We appreciate your visit to our store!!                                      ")
    print("                                                Visit again :)                                                ")
    print()
    print("-----------------------------------A bill has been created in text file as well.--------------------------------------------------------------")
    print("\n")
    print("**********************************************************************************************************************************************")   

 
    #This code prints the bill in txt formate.
    text = f"Trade-{Name}.txt"
    file = open(text,"w")
    file.write("********************************************************************************************************************************************************************************************") 
    file.write("\n")
    file.write("------------------------------------------laptop Shop--------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("                                           Kathmandu, Nepal                                              ")
    file.write("\n")
    file.write(f"                                             GST.NO:-{GST}                                              ")
    file.write("\n")
    file.write("----------------------------------------------Trade Bill------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write(f"Date:- {Year}-{Month}-{Day}                                                               Time:- {Hour}:{Minute}:{Second}:{microSecond}")
    file.write("\n")
    file.write(f"Customer Name: {Name}")
    file.write("\n")
    file.write(f"Phone Number: {phoneNumber}")
    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("S.No. \t\t laptop Name \t\t\t\t Brand \t\t\t\t price \t\t\t Quantity \t\t\t\t Amount")
    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    row = ""
     
    counter = 0
    finalPrice = 0
    for i in range(len(tempSellBill)):
        counter += 1
        shipping = 10
        for j in range(len(tempSellBill[i])):
            dollarprice = float(tempSellBill[i][2].replace("$",""))
            priceDetail = dollarprice * tempSellBill[i][3]
            row = row + str(tempSellBill[i][j]) + "\t\t\t"
        file.write(f"{counter} \t\t {row} \t\t{priceDetail}")
        file.write("\n")
        finalPrice = finalPrice + priceDetail
        row = ""
        Grand_total = finalPrice + shipping
        
            
    file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write(f"                                                   Total Price: ${finalPrice}                                          ")
    file.write("\n") 
    file.write(f"                                                     shipping = 10                                          ")
    file.write("\n")
    file.write(f"                                              Grand total Price with shipping : ${Grand_total}                                          ")
    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("                                              We appreciate your visit to our store!!                      ")
    file.write("\n")
    file.write("                                                    Visit again :)                                                ")
    file.write("\n") 
    file.write("********************************************************************************************************************************************************************************************") 

    file.close()
    
    
    
def updateTextFile(mainData):

    """Here, we are adding the updated information to the text file in the form of a string."""
    
    file = open("laptops.txt", "w")
    for value in mainData.values():
        file.write(str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) +"," + str(value[4]) + "," + str(value[5]) + "\n")
    file.close()
            
