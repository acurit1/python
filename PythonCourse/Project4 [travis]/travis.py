known_users= ["Alex","Emma","Alexandra","Tester"]
print(len(known_users))

while True:
    print("Hi, my name is Travis")
    name=input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system? (y/n)").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("Good, I was hoping you wouldn't leave anyway.")
    else:
        print("Hmmmm . . . . I don't think I know you {}".format(name))
        add_me = input("Would you like to be added to the system? (y/n)").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me =="n":
            print("no problem, have a good one! :)")
