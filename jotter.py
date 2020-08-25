import time
print("Hello, This is a jotter app")

print("Which jotter do u want to use:")
print("1.Jotter1 \n 2.Jotter2 \n 3.Jotter3")
jotter = int(input("Select:"))
if jotter == 1:
    jotter1 = str(input("Put in your memo:"))
    print("Click to save")
    input()
    jotter1Demo = [jotter1]
    print("1.Save \n 2:Dont Save")
    veris = int(input())
    if veris == 1:
        print("Saved")
    elif veris == 2:
        jotter1Demo.pop()
        print("Which jotter do u want to use:")
        print("1.Jotter1 \n 2.Jotter2 \n 3.Jotter3")
        jotters = int(input())
        if jotters == 1:
            print("Put in Your Memo:")
            input()
        elif jotters == 2:
            print("Put in your Memo:")
            input()
        elif jotters == 3:
            print("put in your memo:")
            input()
    else:
        print("invalid input")
if jotter == 2:
    jotter2 = str(input("Put in your memo:"))
    print("Click to save")
    input()
    jotter2Demo = [jotter2]
    print("1.Save \n 2:Dont Save")
    veris = int(input())
    if veris == 1:
        print("Saved")
    elif veris == 2:
        jotter2Demo.pop()
        print("Which jotter do u want to use:")
        print("1.Jotter1 \n 2.Jotter2 \n 3.Jotter3")
        veris = int(input())
        if veris == 1:
            print("Saved")
        elif veris == 2:
            jotter2Demo.pop()
            print("Which jotter do u want to use:")
            print("1.Jotter1 \n 2.Jotter2 \n 3.Jotter3")
            jotters = int(input())
            if jotters == 1:
                print("Put in Your Memo:")
                input()
            elif jotters == 2:
                print("Put in your Memo:")
                input()
            elif jotters == 3:
                print("put in your memo:")
                input()
            else:
                print("Invalid Syntax")
        print("Do you want to save Your Memo")
        print("1.Yes \n 2.No\n")
        answer = int(input())
        if answer == 1:
            print(".......Saving")
            print("saved")
        if answer == 2:
            print("Exiting....")
            time.sec(5)

    else:
        print("invalid input")
if jotter == 3:
    jotter3 = str(input("Put in your memo:"))
    print("Click to save")
    input()
    jotter3Demo = [jotter3]
    print("1.Save \n 2.Dont Save")
    veris = int(input())
    if veris == 1:
        print("Saved")
    elif veris == 2:
        jotter3Demo.pop()
        print("Which jotter do u want to use:")
        print("1.Jotter1 \n 2.Jotter2 \n 3.Jotter3")
        jotters = int(input())
        if jotters == 1:
            print("Put in Your Memo:")
            input()
        elif jotters == 2:
            print("Put in your Memo:")
            input()
        elif jotters == 3:
            print("put in your memo:")
            input()
        else:
            print("Invalid Syntax")
        print("Do you want to save Your Memo")
        print("1.Yes \n 2.No\n")
        answer = int(input())
        if answer == 1:
            print(".......Saving")
            print("saved")
        if answer == 2:
            print("Exiting....")
            time.second(5)
else:
    print("invalid input")

print("Do You want to open saved files")
print("1.Yes \n2.No ")
ans = int(input())
if ans == 1:
    if ans == jotter1Demo:
        print(jotter1Demo)
    if ans == jotter2Demo:
        print(jotter2Demo)
    if ans == jotter3Demo:
        print(jotter3Demo)
elif ans == 2:
    print("Exiting")
else:
    print("Invalid input")
