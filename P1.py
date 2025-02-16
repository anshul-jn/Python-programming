# write a programme to calculate the total count of money in the piggy bank given the coin of rs 10 , 5, 2 , 1 
a=int(input("Enter the number of 10 rs coin in the piggy bank:")) # taking the input from hte user 
b=int(input("enter the number of 5 rs coins in the piggy bank:")) #taking the input from the user 
c=int(input("Enter the nummber of 2 rs coin in the piggy bank:"))
d=int(input("Enter the number of 1 rs coins in the piggy bank:"))

# here we calculate the total amount with the mathematical form
TotalAmount=a*10+b*5+c*2+d*1  
#print the total amount
print("Total Amount in the piggy bank",TotalAmount)