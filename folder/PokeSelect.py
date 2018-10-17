import csv

    print("Pick your Pokemon Character" "\n")
    filename = "folder/charac.txt"
    file = open(filename, "r")
    print(file.read())
    file.close()


    with open( "folder/charac.txt","r") as f:
      characReader=csv.reader(f)
      id=input("\n" "Enter Pokemon ID (format:XXX)  :")
      for row in characReader:
        for field in row:
          if field==id:
       
            currentindex=row.index(id)
            player = str(row[currentindex+1])
            print("Your Chosen Pokemon Character: " + player)

