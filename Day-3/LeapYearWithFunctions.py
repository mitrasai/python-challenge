def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap year."
            else:
                return "Not a Leap year."
        else:
            return "Leap year."
    else:
        return "Not a Leap year."


year = int(input("Enter an year: "))
result = isLeap(year)
print(result)

# create two files, first file consists of leap function and start import this file in second file and use the that function
