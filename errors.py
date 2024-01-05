# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program.") # added brackets this caused a syntax error 
print ("\n") # removed indent as cuased a syntax error

   # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # removed extra = and removed indent and removed additional wording -- name error as age_Str was not defined
age = str(age_Str) # chnaged from int to string 
print("I'm " + age +  " years old." ) # removed additional words and added a space

# Variables declaring additional years and printing the total years of age
years_from_now = "3" # removed indent
total_years = str(int(age) + int(years_from_now)) # removed indent (syntax error) and converted the strings to int to add as there was as valueError

print ("The total number of years " + total_years + " includes 3 additional years.")


# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = str(int(total_years) * 12 + 6) # converted str to int and added the additional 6 months required in the text, 
# had this not been done then the  * 12 result would have run 12 times
print ("In 3 years and 6 months, I'll be " + total_months + " months old.")

#HINT, 330 months is the correct answer

