def mystery_museum():
    print("\n🕵‍♂ Welcome, Detective! There's been a robbery at the museum.")
    print("You arrive at the scene. Do you CHECK the security footage or INTERROGATE the guard?")
    
    choice1 = input("(footage/guard): ").lower()
    
    if choice1 == "footage":
        print("\n📽 You see a masked figure leave through the back door.")
        choice2 = input("Do you FOLLOW the trail or CALL backup? (follow/call): ").lower()
        if choice2 == "follow":
            print("\n👣 You find footprints leading to the storage room.")
            choice3 = input("Enter the room or wait? (enter/wait): ").lower()
            if choice3 == "enter":
                print("\n🎯 You catch the thief hiding in the closet. Case solved! You win!")
            else:
                print("\n🕒 You wait too long and the thief escapes. Game over.")
        else:
            print("\n📞 Backup arrives late. The thief is gone. Game over.")

    elif choice1 == "guard":
        print("\n🗣 The guard is nervous and lies.")
        choice2 = input("Do you PRESS him harder or LEAVE him? (press/leave): ").lower()
        if choice2 == "press":
            print("\n😓 He admits he helped the thief and tells you the hideout.")
            print("You arrest both and solve the case. You win!")
        else:
            print("\n🕵‍♂ You miss the clue and the case goes cold. Game over.")
    else:
        print("⛔ Invalid choice. Game over.")

mystery_museum()