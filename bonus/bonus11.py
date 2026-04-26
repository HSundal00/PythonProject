feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters


results = convert(feet_inches)

if results < 1:
    print("Kids is too small")
else:
    print("Kid can use the slide.")

