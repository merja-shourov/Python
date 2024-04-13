
given = "Novenber"

month_end_31= ("January", "March", "April", "July", "August", "October", "Dec")

if( given == "February"):
    print(f"{given} has 28 days")
elif ( given in month_end_31 ):
    print(f"{given} has : 31 days")
else:
    print(f"{given} has : 30 days")