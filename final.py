from hashlib import new
import pandas as pd
import csv

print("\n\nWelcome to SAURABH PRAKASH phone directory")

contactBook="contact.csv"
phFile= open(contactBook, "a+")  
phFile.close

def showMenu():
    print("---------------------------------------------------")
    print("*****MENU BAR*****")
    print("[1] Add New Contact")
    print("[2] Create contact")
    print("[3] Update Contact")
    print("[4] Delete Contact")
    print("[5] Search Contact")
    print("[6] Show All Contact")
    print("[0]  EXIT")
    print("---------------------------------------------------")

    #asking choice from user
    choice=int(input("\nEnter your Choice : "))
    while(check(choice)):
        if(choice==1):
            newContact()
        elif(choice==2):
            createContact()
        elif(choice==3):
            updateContact()
        elif(choice==4):
            deleteContact()
        elif(choice==5):
            searchContact()
        elif(choice==6):
            showContact()
        else:
            print("\n****THANK YOU FOR YOUR VISIT****\n")
            exit()

#checking users entered choice
def check(choice):
    if(choice >= 0 and choice <= 6):
        return True
    else:
        print("\nPlease enter a valid choice\n")
        return False

#function to create new contact
def newContact():
	fname=input("First Name : ")
	lname=input("Last Name : ")
	mob1=input("Mobile Number : ")
	tempMob=''
	data=[fname,lname,mob1,'']
	with open('contact.csv','a')as f:
		f.writelines(f'\n{fname.capitalize()},{lname.capitalize()},{mob1},{tempMob}')
	print("\n>>>>Contact added successfully<<<<")
	print("---------------------------------------------------\n")
	showMenu()

# function will help in case of createContact for writing to file
def helpCreateContact(fn,ln,num):
    with open("contact.csv","r") as f1, open("temp.csv","w",newline="") as f2:
        writer=csv.writer(f2)
        reader=csv.reader(f1)
        for row in reader:
            #print(row)
            if len(row)==0:
                continue
            elif row[0] !=fn and row[1]!=ln:
                writer.writerow(row)
            elif row[0] !=fn and row[1]==ln:
                writer.writerow(row)
                #print("write",row[0],row[1])
            elif row[0] ==fn and row[1]!=ln:
                writer.writerow(row)
            elif (row[0]==fn and row[1]==ln):
                if row[2]!="" and row[3]!="":
                    writer.writerow(row)
            elif (row[0]==fn and row[1]==ln):
                if row[2]!="" and row[3]=="":
                    pass
    with open("contact.csv","w",newline="") as ff1, open("temp.csv","r") as ff2:
        tempWriter=csv.writer(ff1)
        tempReader=csv.reader(ff2)
        for tempRow in tempReader:
            tempWriter.writerow(tempRow)
    print("\n>>>>Contact created successfully<<<<")
    print("---------------------------------------------------\n")

# function will create contact that is add second mobile number in a existing contact
def createContact():
    df=pd.read_csv("contact.csv")
    lst1=list(df['FirstName'])
    lst2=list(df['Mobile1'])
    num=input("Mobile Number : ")
    with open("contact.csv","r") as f1:
        reader=csv.reader(f1)
        for row1 in reader:
            if len(row1)==0:
                continue
            elif row1[2]==num:
                print("\n>>>>Contact already exist<<<<")
                print("---------------------------------------------------\n")
                showMenu()
    fn=input("First Name : ")
    ln=input("Last Name : ")
    with open("contact.csv","r") as f2:
        reader=csv.reader(f2)
        for row2 in reader:
            if len(row2)==0:
                continue
            elif row2[0]==fn and row2[1]==ln:
                #print("move for next step")
                idx=lst1.index(fn)
                with open("contact.csv","a") as ff:
                    ff.writelines(f'\n{fn.capitalize()},{ln.capitalize()},{lst2[idx]},{num}')
                helpCreateContact(fn,ln,num)
                showMenu()
        else:
            print("\n>>>>Not a valid Name to Add contact<<<<")
            print("---------------------------------------------------\n")
            showMenu()

def helpUpdateContact(fn,ln,data,reference):
    with open("contact.csv","r") as f1, open("temp.csv","w",newline="") as f2:
        reader=csv.reader(f1)
        writer=csv.writer(f2)
        for row in reader:
            if len(row)==0:
                continue
            elif (row[0]==fn and row[1]==ln):
                #print("match")
                if reference==2:
                    row[2]=data
                    writer.writerow(row)
                    #print("write", row[2])
                elif reference==3:
                    row[3]=data
                    writer.writerow(row)
                    #print("write", row[3])
            else:
                writer.writerow(row)
        
    with open("contact.csv","w",newline="") as ff1, open("temp.csv","r") as ff2:
        tempWriter=csv.writer(ff1)
        tempReader=csv.reader(ff2)
        for tempRow in tempReader:
            tempWriter.writerow(tempRow)
    print("\n>>>>Contact updated successfully<<<<")
    print("---------------------------------------------------\n")



def updateContact():
    print("Please enter the below details")
    fn=input("First Name : ")
    ln=input("Last Name : ")

    with open("contact.csv","r") as f:
        reader=csv.reader(f)
        for row in reader:
            if len(row)==0:
                continue
            elif row[0]==fn and row[1]==ln:
                print("Plese press 'Y' for yes and 'N' for no")
                m1Update=input("Do you want to update Mobile1 [ Y | N ] : ")
                if m1Update.capitalize()=='Y':
                    m1New=input("Enter new Mobile1 : ")
                    #print("call for m1")
                    helpUpdateContact(fn,ln,m1New,2)
                else:
                    pass

                m2Update=input("Do you want to update Mobile2 [ Y | N ] : ")
                if m2Update.capitalize()=='Y':
                    m2New=input("Enter new Mobile2 : ")
                    print("call for m2")
                    helpUpdateContact(fn,ln,m2New,3)
                else:
                    pass
                showMenu()
        else:
            print("\n>>>>Not a valid details to update contact<<<<")
            print("---------------------------------------------------\n")
            showMenu()
                

def deleteContact():
    fn=input("First Name : ")
    ln=input("Last Name : ")
    df=pd.read_csv("contact.csv")
    l1=list(df['FirstName'])
    l2=list(df['LastName'])
    if (fn in l1 and ln in l2):
        with open("contact.csv","r") as f1, open("temp.csv","w",newline="") as f2:
            reader=csv.reader(f1)
            writer=csv.writer(f2)
            for row in reader:
                #print(row)
                if len(row)==0:
                    continue
                elif (row[0]==fn and row[1]==ln):
                    pass
                else:
                    writer.writerow(row)
            else:
                print("\n>>>>Contact Deleted successfully<<<<")
                print("---------------------------------------------------\n")
        
        with open("contact.csv","w",newline="") as f11, open("temp.csv","r") as f22:
                tempWriter=csv.writer(f11)
                tempReader=csv.reader(f22)
                for tempRow in tempReader:
                    tempWriter.writerow(tempRow)
        showMenu()
    else:
        print("\n>>>Not a valid details to delete contact<<<<")
        print("---------------------------------------------------\n")
        showMenu()

# will search contact by its name
def searchContact():
    print("Please enter the below details")
    fn=input("First Name : ")
    ln=input("Last Name : ")

    with open("contact.csv","r") as f:
        reader=csv.reader(f)
        for row in reader:
            if len(row)==0:
                continue
            elif row[0]==fn and row[1]==ln:
                print("\n>>>>Contact Found<<<<\n")
                print("Name : ",row[0],row[1])
                print("Contact Number : ",row[2]," ",row[3])
                print("\n---------------------------------------------------\n")
                showMenu()
        else:
            print("\n>>>>Contact Not Found<<<<")
            print("---------------------------------------------------\n")
            showMenu()
    

# will show entire contact stored in file
def showContact():
    df=pd.read_csv("contact.csv")
    print("\n---------------------------------------------------\n")
    print(df)
    print("\n---------------------------------------------------\n")
    showMenu()

if __name__=='__main__':
    showMenu()