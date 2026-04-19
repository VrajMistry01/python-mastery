def ticket_price(age:int, is_student:bool,day:str):
    if age < 0:
        return ("Invalid age")
    elif age < 12:
        price = 0 
        return ("$"+str(price))
    elif age >=65:
        price = 5
        return ("$"+str(price))
    else:
        if is_student:
            price = 8
            return ("$"+str(price))
        else:
            if day in ['Saturday',"Sunday"]:
                price=15
                return ("$"+str(price))
            else:
                price = 12
                return ("$"+str(price))

    
print(ticket_price(10, False, "Monday"))
print(ticket_price(70, False, "Saturday"))
print(ticket_price(20, True, "Sunday"))
print(ticket_price(30, False, "Sunday"))
print(ticket_price(30, False, "Monday"))
print(ticket_price(-5, False, "Monday"))
print(ticket_price(12, False, "Monday"))
print(ticket_price(65, False, "Monday"))
