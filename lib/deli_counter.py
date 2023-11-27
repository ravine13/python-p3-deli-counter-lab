katz_deli = ["Don", "Peggy", "Betty", "Pete"] # list of customers currently in line

def line(katz_deli): # function to display the current line of customers
    
    if katz_deli == []: # check if the line is empty
        print("The line is currently empty.") # if it is, print a message showing that it is empty
    else:
        message = "The line is currently:" # if not, start a message with the current line
        for person in katz_deli: # iterate over each person in line
            place_in_line = katz_deli.index(person) + 1 # get the person's place in line i.e index + 1
            message += f" {place_in_line}. {person}" # add the person's place and name to the message
        print(message) # print the full message

line(katz_deli) # calling the function to display the current line

def take_a_number(katz_deli, new_customer): # function to add new customer to the line
    
    katz_deli.append(new_customer) # adds a new customer to the end of the line
    print(f"Welcome, {new_customer}. You are number {len(katz_deli)} in line.") # prints a welcome message for the new customer and their number in line

take_a_number(katz_deli, "Joan") # calling the function for adding new customer in line

def now_serving(katz_deli): # function to serve the next customer in line
    
    if katz_deli == []: # check if there are any customers in line
        print("There is nobody waiting to be served!") # if not, print a message indicating that there is nobody waiting to be served
    else:
        print(f"Currently serving {katz_deli[0]}.") # if there are customers in line, print a message indicating who is being served
        katz_deli.pop(0) # remove the served customer from the line

now_serving(katz_deli) # calling the function to serve the next customer