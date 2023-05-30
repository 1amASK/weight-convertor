"""
Prompt:
    Write a program which:
        1. Prompts the user for the weight they want to convert.
            "Weight: "
        2. Asks what it wants to convert to.
            "Convert to (K)gs or (L)bs? "
        3. Gives the correct conversion.
"""

#Function
def convert(weight, to_unit):
    if to_unit == "l":
        weight *= 2.2
        weight = str(weight)
        print("Weight in Lbs: " + weight)
    elif to_unit == "k":
        weight /= 2.2
        weight = str(weight)
        print("Weight in Kgs: " + weight)
    else:
        to_unit = (input("Please input what you wish to convert to; (k)gs or (L)bs? ")).lower()
        convert(weight, to_unit)

#Program
weight = float(input("Weight: "))
to_unit = (input("Convert to (k)gs or (L)bs? ")).lower()
convert(weight, to_unit)