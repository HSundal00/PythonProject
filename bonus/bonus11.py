feet_inches = input("Enter feet and inches: ")

def parse(feetinches):
    parts = feetinches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


f, i = parse(feet_inches)
results = convert(f, i)

if results < 1:
    print("Kids is too small")
else:
    print("Kid can use the slide.")

