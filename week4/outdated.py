import sys
month=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    Try:
        date=input('Date:').strip()
        if "/"in date:
            Month,day,year=date.split('/')
            print(f"{year}--{Month}--{day}")
        elif ","in date:
            
            