#
#   Sergio Munguia
#
#   dateconvert.py
#
#   Input: Date in "mm/dd/yyyy" format
#
#   Processing:
#               1. prompt user for date
#               2. split date into month, day, year
#               3. define a sequence of months
#               4. index to retrieve the appropriate month
#               4. display date as "month day, year" using month as
#                   
#
#   Output: Converts a date in form "mm/dd/yyyy" to "month day, year"

def main():
    # get the date
    date = input("Enter a date (mm/dd/yyyy): ")

    # split into components
    month, day, year = date.split("/")

    # list of months 
    months = ["January", "Febuary", "March", "April",
              "May", "June", "July", "August", "September", "October", "November",
              "December",]
    month = months[int(month)-1]

    # output result in month day, year format
    print("The converted date is:", month, day+",", year)

main()
