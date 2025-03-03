# data=155 
# data1=200
# result=0
# result=data+data1
# print("ADDITION:",result)
# result=data-data1
# print("SUBTRACTION:",result)
# result=data*data1
# print("MULIPLY:0:",result)
# result=data/data1
# print("DIVISION:",result)
# result=data%data1
# print("MODULO:",result)



# add=int(input("Enter the value"))
# add1=int(input("Enter the value"))
# sum=add+add1
# print('Addition:',sum)



##discount price of  product
original_price = 1200
discount_percentage = 15
discount_amount = (original_price * discount_percentage) / 100  # Multiplication and Division
final_price = original_price - discount_amount  # Subtraction
print(f"Discounted Price: ${final_price}")


# tax deduction

annual=float(input("Annual income "))

#takeHome=annual-(annual*0.300);

tax=(annual*30)/100

takeHome=annual-tax;

print(takeHome,"from",annual,"after tax deduction",tax)