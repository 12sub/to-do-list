print("To-Do List")

test = int(input("How Many Things do you want to do:"))

for interest in range(test):
    strength = str(input("What do u want to write:"))
    halo = [strength]
print("What Would yo do:\n 1.Add Notes\n 2.Delete To-do\n 3. Select To-do")
temp = int(input())

if temp == 1:
    notes =  str(input("Put in a to-do List:"))
    if notes == strength:
        print("You have already created this To-Do")
    else:
        halo.append(notes)
if temp == 2:
    print("Are you sure:\n 1.Yes\n2.No")
    select = int(input())
    if select == 1:
        halo.pop()
        print(halo)
    if select == 2:
        print("Exiting....")
    else:
        print("Invalid Input")
if temp == 3:
    print("Which to-do do you want to see:")
    select = int(input())
    for halos in halo:
        print(halo)
        if halos[0]:
            print(halos)
        elif halo[1]:
            print(halos)
        elif halo[2]:
            print(halos)
        elif halo[3]:
            print(halos)
        elif halo[4]:
            print(halos)
        else:
            print("Out of range")

print("Do you want to save your work \n 1.Yes \n 2.No")
texts = int(input())
if texts == 1:
    print("Saved")
    print("Do you want to Open your work: \n 1.Yes\n 2.No")
    text2 = int(input())
    if text2 == 1:
        for halos in halo:
            print(halos)
    if text2 == 2:
        print(".....Exiting")
if texts == 2:
    print("....Exiting")
