from bonus.parsers import parse
from bonus.converters import parse

feet_inches = input("Enter feet and inches: ")


f, i = parse(feet_inches)
results = convert(f, i)

if results < 1:
    print("Kids is too small")
else:
    print("Kid can use the slide.")

