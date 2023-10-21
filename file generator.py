#written by Ali Akhlaghi
import os

def main():
    print("\n-------------------------------------------------")
    print("!*****|Simple Text File Generator|*****!")
    
    startMenu = ("\nPress 1 to create text file\n" +
        "Press 2 to write the text file\n" +
          "Press 3 to open the text file")

    print(startMenu)

    txtInput = input("\nChoose a number above and hit enter:")

    #Creating a text file    
    if txtInput == '1':
        txtName = input("\nEnter the text file name or type /N to back to menu:")
        if(txtName == "/N"):
           main() 
        else:
            while (txtName == ""):
                print("Please don't leave a blank name")
                txtName = input("Enter the text file name:")
        
            if(txtName != ""):
                while(os.path.isfile(txtName + '.txt')):
                    print("\nFile name already exist")
                    txtName = input("Enter the text file name:")
                
            txtFile = open( txtName + ".txt", "w")
            print("\nThe text file has been created!")
            txtFile.close()
            input("\nPress enter to go back to menu..")
            main()

    #Writing a text file
    elif txtInput == '2':
        txtName = input("\nEnter the text file name or type /N to back to menu:")
        if(txtName == "/N"):
           main() 
        else:
            while not os.path.isfile(txtName):
                print("\nFile not exist")
                txtName = input("\nEnter the text file name or type /N to back to menu:")

                if(txtName == "/N"):
                   main()

            print("\n" +txtName + " Has been opened!")
            txtMsg = input("Please write something to your text file:")

            while (txtMsg == ""):
                txtMsg = input("Please write something to your text file:")

            txtFile = open(txtName, "w")
            txtFile.writelines(txtMsg)
            txtFile.close()
            print("\nSuccesfully write a text!")
            input("Press enter to go back to menu...")
            main()
        
    #Opening a Text File
    elif txtInput == '3':
        txtName = input("\nEnter the text file name or type /N to back to menu:")

        if(txtName == "/N"):
           main() 
        else:
            while not os.path.isfile(txtName):
                print("\nFile not exist")
                txtName = input("\nEnter the text file name or type /N to back to menu:")

                if(txtName == "/N"):
                   main()
                   
            print("Opening the file..\n")
            os.startfile(txtName)
            input("Press enter to go back to menu...")
            main()      

    else:
        print("\nPlease enter only the number in the menu\n")
        input("Press enter to continue...")
        main()

main()
