import csv

class PokeSelect():
  def PokeSelect():
    checker = True
    data = ["","","","",""]
    print("#############################################")
    print("Pick your Pokemon Character")
    print("ID:     Name:")
    filename = "folder/charac.txt"
    file = open(filename, "r")
    characReader=csv.reader(file)
    for column in characReader:
        a = ""
        b = ""
        a = column[0]
        b = column[1]
        print("%s     %s" % (a,b))


    file.close()
    print("=============================================")

    while checker:
      #Opens and Display
      with open( "folder/charac.txt","r") as f:
        characReader=csv.reader(f)
        id=input("Enter Pokemon ID (format:XXX)  :")

        #Opens and Finds
        for row in characReader:
          for field in row:
            if field==id:
              currentindex=row.index(id)
              data[0] = str(row[currentindex+1])
              data[1] = str(row[currentindex +2])
              data[2] = str(row[currentindex +3])
              data[3] = str(row[currentindex + 4])
              data[4] = str(row[currentindex + 5])
              print("#############################################")
              print("Your Chosen Pokemon Character: " + data[0])
              print("Attributes: \n Att: %s \n Def: %s \n Agt: %s" % (data[1], data[2], data[3]))

      if(data[0] == ""):
        checker = True
        print("Input not Recognized. Pls Try Again")
      else:
        checker = False
      
    print("#############################################")
    return data
