name = input ("What is your name? ") #the info gained from this line just disappears. but if you name this info then you can refer to it later on.
print(len(name)) #print (name) will print the variable, whereas adding the len function will print the length of the string inputted by the user

#this is a cleaner way to do it
print(len(input("what is your name?")))

#this method allows us to reuse the variable later and makes it much more readable

username = input("what is your name? ")
length = len(username)
print(length)

#an important rule is to make your code readable. eg naming variables properly vs single letters. you can also have multiple words eg user_name
#also putting a number at the start of a variable eg 1name will cause a syntax error 
#python only cares about consistency by using the same variable name throughout code
