def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    rate_of_adult=no_of_adults*37550
    rate_of_child=no_of_children*(37550/3)
    without_tax= rate_of_child + rate_of_adult
    service_tax= .07 * without_tax  + without_tax
    total_ticket_cost = service_tax - .1 * service_tax

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)