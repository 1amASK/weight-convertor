"""
    Write a program which:
        1. Prompts the user for the weight they want to convert.
            "Weight: "
        2. Asks what it wants to convert to.
            "Convert to (K)gs or (L)bs? "
        3. Gives the correct conversion.
"""
#Function
def convert(weight, x):
    if x == "l":
        weight *= 2.20462262185
        weight = str(weight)
        print("Weight in Lbs: " + weight)
    elif x == "k":
        weight /= 2.20462262185
        weight = str(weight)
        print("Weight in Kgs: " + weight)
    else:
        weight = int(input("Weight: "))
        x = (input("Convert to (k)gs or (L)bs? ")).lower()
        convert(weight, x)

#Program
weight = int(input("Weight: "))
x = (input("COnvert to (k)gs or (L)bs? ")).lower()
convert(weight, x)