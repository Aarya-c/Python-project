def getFileContent():
    """Here, We are retrieving information from the txt file and storing it in a list.."""

    file = open("laptops.txt","r")
    data = file.readlines()
    file.close()
    return data

