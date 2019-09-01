#Author: Tony Quinn
#Date: 25-8-19
#Description: Dictionary

monthConversions = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions["Nov"])
print(monthConversions.get("Luv","Not a valid key"))
