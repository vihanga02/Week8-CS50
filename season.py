#import datetime ,sys and inflect modules
from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    #prompt user to enter a date
    date = input("Enter your birthday:")
    dateValidate = get_date(date)  
    print(dateValidate)
    minutes = calculate(dateValidate)
    print(phrase(minutes))

def get_date(d):
    try:
        #check whether input in a correct date foam
        a = date.fromisoformat(d)
        return a
    except ValueError:
        #if the date pattern is wrong,exit and output a error messege
        sys.exit("Invalied date")

def calculate(bday):
    #get today's date
    today = date.today()
    #calculate how many days between today and inputed date
    duration = today - bday
    #conver days into minutes
    min = duration.days *24 *60
    
    return min

def phrase(m):
    #convert numbers of minutes in to words
    t = p.number_to_words(m,andword="")
    return t

if __name__ == "__main__":
    main()

