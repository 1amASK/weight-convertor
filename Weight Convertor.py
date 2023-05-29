"""
    Write a program which:
        1. Prompts the user for the weight they want to convert.
            "Weight: "
        2. Asks what it wants to convert to.
            "(K)gs or (L)bs? "
        3. Gives the correct conversion.
"""
def convert(weight, x):
    pass
    if x == "k":
        
        print("Weight in Lbs: ")
    elif x == "l":

        print("Weight in Kgs: ")
    else:
        weight = int(input("Weight: "))
        x = (input("Convert to (k)gs or (L)bs? ")).lower()
    convert(weight, x)
weight = int(input("Weight: "))
x = (input("Convert to (k)gs or (L)bs? ")).lower()
convert(weight, x)