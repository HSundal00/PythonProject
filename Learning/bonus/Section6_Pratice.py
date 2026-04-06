
# Ask the user for their name
name = input("What is your name? ")
f = open("files/diary.txt", 'a')
f.write(name + "\n")
f.close()

# Ask the user if the want to create a new note
response = input("Would you like to create a new note or used the existing note? ").lower()

if response == "no":
    note = input("Write your note: ")
    f = open("files/diary.txt", 'a')
    f.write(note + "\n")
    f.close()

    print("Notes Saved!")

    f = open("files/diary.txt", 'r')
    content = f.read()
    f.close()

    print("Your note says: \n", content)

elif response == "yes":
    filename = input("What would you would like to name your note file? ")
    note = input("write your new note: ")
    f = open(f"files/{filename}.txt", 'a')
    f.write(note + "\n")
    f.close()

    print(f"Notes saved in {filename}.txt")

    f = open(f"files/{filename}.txt", 'r')
    content = f.read()
    f.close()

    print("Your notes says: \n", content)






