# WAP To Calculate the selling price of book based on the cost price and discount.
###  profit= s.p - c.p
###  Loss= c.p-s.p

cost_price=float(input('Enter the cost price:'))
discount=float(input('Enter the discount percentage:'))

discount_amount= cost_price*discount/100
selling_price= cost_price-discount_amount

print('Discount amount=',discount_amount)
print('Selling price=',selling_price)