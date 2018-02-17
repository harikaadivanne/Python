con = int(input("Number of contacts : "))
contactlist = []
contact_dict = {}
for i in range(con) :
    contact_dict["name"] = input("Enter name ")
    contact_dict["number"] = input("Enter number ")
    contact_dict["email"] = input("Enter email ")
    contactlist.append(contact_dict.copy())
print(contactlist)
def opt() :
    x = str(input("a)Display contact by name \nb)Display contact by number \nc)Edit contact by name \nd)Exit:\n "))
    return x

if opt()=='a':
    name = str(input("Enter the name: "))
    for a in contactlist:
        if a['name'] == name:
            print(a)
if opt()=='b':
    num = str(input("Enter the number: "))
    for a in contactlist:
        if a['number'] == num:
            print(a)
if opt()=='c':
    name = str(input("Enter the name: "))
    number = int(input("Enter the number: "))
    for index,a in enumerate(contactlist):
        if a['name'] == name:
            contactlist[index]['number']=number
    print(contactlist)
if opt()=='d' :
    exit()