"""
Prompt:
    Write a program which:
        1. Prompts the user for the weight they want to convert.
            "Weight: "
        2. Asks what it wants to convert to.
            "Convert to (K)gs or (L)bs? "
        3. Gives the correct conversion.
"""

#Function Creation
def convert(weight, to_unit):
    if to_unit != "k" and to_unit != "l": #stamps out the edge case of neither 'k' nor 'l' being inputted by the user
        to_unit = (input("Please input what you wish to convert to; (k)gs or (L)bs? ")).lower()
        convert(weight, to_unit)
    elif to_unit == "l": #runs to convert to lbs
        weight *= 2.2
        weight = str(weight)
        print("Weight in Lbs: " + weight)
    else: #runs to convert to kgs
        weight /= 2.2
        weight = str(weight)
        print("Weight in Kgs: " + weight)

#Program Creation
weight = float(input("Weight: "))
to_unit = (input("Convert to (k)gs or (L)bs? ")).lower()
convert(weight, to_unit)