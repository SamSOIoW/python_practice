print ("This is how not to do Pythin Math")

num_one = int(input("Please enter a number between 1 and 100: "))
if num_one >= 101: 
    print ("I asked you to add a word not a number!!!")  # this is giving an incorrect text message
    num_two = int(input("Please enter another number between 1 and 100: "))
total = str(int(num_one) * int(num_two))
print()
print ("I will now add your numbers, this gives us a result of "  + total) # this has been multiplied and not added
print()
num_three = int(input("Lets add another number between 1 and 10: "))
print()
final_total = str(int(total)) * num_three
print ("This is the total of the origina numbers times by the last number: " + final_total)  
    # instead of multiplying the total by the last number, it is displaying the total x times 