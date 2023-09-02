# addresses = {'Saad Akhtar': {'name':'saad', 'gender':'male', 'email':'f2019065077@umt.edu.pk'},
#             'Asad Akhtar': {'name':'asad', 'gender':'male', 'email':'saadsaifalasad@gmail.com'},
#             'Jack Lio' : {'name':'jack', 'gender':'male', 'email':'saad.akhtar.se@gmail.com'}}


import os
file = os.path.abspath("C:\JARVIS\Data\Contacts\people.txt")

def get_email_address(name):
    with open(file) as f:
        lines = f.readlines() # All lines
        for i in range(len(lines)): # i is index from lines(contain all lines)
            address = lines[i].split(", ") # make array of a line (to separate each data)
            if address[0] in name.lower():
                print("Name: " + address[0].capitalize() + "\nID: " + address[2])
                return (address[2])
        else:
            return "None"

def get_name(name):
    with open(file) as f:
        lines = f.readlines() # All lines
        for i in range(len(lines)): # i is index from lines(contain all lines)
            address = lines[i].split(", ") # make array of a line (to separate each data)
            if address[0] in name.lower():
                return (address[0]) #reutrn name from contact info
        else:
            return "None"
                


