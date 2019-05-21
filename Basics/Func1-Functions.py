#####  MAKE FUNCTION INSTEAD OF COPYING CODE  #####
def yell(text):
    text = text.upper()
    numchar = len(text)
    result = text + "!" * (numchar // 2)
    print(result)

# praise
praise = "You are doing great"
# praise = praise.upper()
# numchar = len(praise)

# result = praise + "!" * numchar

# print(result)
yell(praise)

# advice
advice = "Don't forget to ask for help"

# advice = advice.upper()
# numchar = len(advice)

# result = advice + "!" * numchar

# print(result)
yell(advice)

# Call function again
yell("Don't repeat yourself.  Keep code DRY")
