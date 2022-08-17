def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if((food_type =='N' or food_type == 'V') and distance_in_kms > 0 and quantity_ordered >0):
        
        if (food_type =="N"):
            price_per_plate = 150
        else:
            price_per_plate = 120 
            
        dc=0
        
        if (distance_in_kms<= 3):
            dc=0
        elif ( 3 < distance_in_kms and distance_in_kms <= 6):
            dc=(distance_in_kms - 3) * 3
        else:
            dc=(distance_in_kms - 6 ) * 6 + 9
        
        bill_amount =(quantity_ordered * price_per_plate) +dc
    else:
        bill_amount = -1
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)