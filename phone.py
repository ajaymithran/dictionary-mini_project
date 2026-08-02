contacts={
    "ajay":"8098866496"
}


# for adding contact 
def adding_contact():
    # for already exist contact
    name=input("name: ")
    # if name already exitis the dict will update it auto-maticially
    if contacts.get(name) is not None:
        print("the contact already exist pls try update")
        print("\n----------------------------------")
    else:
        ph_no=int(input("ph_no: "))
        if len(str(ph_no))==10:
            contacts[name]=ph_no
        # if ph_no is exces of 10 or minial of 10 digits 
        else:
            print(f"check the phno length-{len(str(ph_no))}\nwe need 10 digits of phno")
        print("contact added succesfully")
        print("\n----------------------------------")

def view_contact():
    # to view for loop .items is used to unpack
    for name,ph_no in contacts.items():
        print(f" name : {name}\nph_no : {ph_no}")
    print("\n----------------------------------")

def search_contact():
    name=input("name: ")
    # if the conntact are in  the dict
    checking_contact=contacts.get(name)
    if checking_contact == None:
        print("the contact not exist pls try adding contact")
    else:
        # get the name to acces phone number
        ph_no=contacts.get(name)
        print(f"{name} : {ph_no}")
        print("\n----------------------------------")

def update_number():
    # for update
    name=input("name: ")
    if name  not in contacts.keys():
        print("the name is not in the contact pls add")
    else:
        ph_no=int(input("ph_no: "))
        if len(str(ph_no))==10:
            contacts.update({name:ph_no})
        else:
            print(f"check the phno length-{len(ph_no)}\nwe need 10 digits of phno")
        print("contact updated succesfully")
    print("----------------------------------\n")


def delete_contact():
    # for delete 
    name=input("name: ")
    # if contact name is not in the contact
    if name  not in contacts.keys():
        print("the name is not in the contact pls add")
    else:
        del contacts[name]
        print("contact deltedd succesfully")
        print(contacts)
    print("----------------------------------\n")   

def total_contacts():
    #  for total we need only one thing len()
    total=len(contacts)
    print(total)
    print("------------------------------\n")

def exit_contact():
    print("thanks for using the contact..!!")
    print("------------------------------\n")

def clear_contact():

    contacts.clear()

while True:
    print("===========PHONE BOOK===============")
    option=int(input("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Number\n5. Delete Contact\n6. Total Contacts\n7. Exit\n8. delete all contact\noption in number: "))
    if option == 1:
        adding_contact()
    elif option == 2:
        view_contact()
    elif option == 3:
        search_contact()
    elif option == 4:
        update_number()
    elif option == 5:
        delete_contact()
    elif option == 6:
        total_contacts()
    elif option == 7:
        conframation=input("are you sure?\ny/n").strip()
        if conframation=="y":
            exit_contact()
            break
        else: continue
    elif option== 8:
        clear_contact()
    else:
        print("option is invalid try typing numbers of those function")



