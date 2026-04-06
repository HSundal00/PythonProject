date = input("What is today's date? ")
mood = input("On a scale of 1-10, how well did you day go? ")
thoughts = input("Write your thoughts: \n")

with open(f"Journal/{date}.txt", "w") as file:
    file.write(mood + 2 * '\n')
    file.write(thoughts)


