# created by Zayan
Input = int(input("Enter the number of days...we will convert it to years or weeks\n:"))
choice = int(input("to convert in weeks enter 1 and for years enter 2\n:"))
try:
    if choice == 1:
        weeks = Input/7
        weeks = round(weeks, 3)
        print(f"these days are equivalent to {weeks} weeks")
    elif choice == 2:
        years = Input/365
        years = round(years, 2)
        print(f"these days are equivalent to {years} years")
except:
    print("wrong input")

# created by Zayan