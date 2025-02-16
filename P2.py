#Write a programme to calculate the bill amount a night giving its quantity sold, value, discount and tax 
#taking input from the user
#a=quantity , b=value , c= Discount , d=Tax 
a=eval(input("Enter the quantity of item sold:"))
b=eval(input("Enter the value of item:"))
c=eval(input("Enter the discount you want:"))
d=eval(input("Enter the tax:"))
#do some mathematical calculation                          
amt=a*b
discount= (amt*c)/100
subtotal=amt-discount 
tax=(subtotal*d)/100
totalamount=subtotal+tax

print(" Quantity Sold \n",a)
print("value \n",b)
print("Total amount:",)
