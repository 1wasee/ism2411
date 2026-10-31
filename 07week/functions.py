#The first bug I spotted was the missing colon just by going through and looking at the code because that is a basic mistake.
# apply_discount(price, tier) takes the original price and the customer's tier as inputs. It applies the correct discount based on whether the tier and then returns the discounted price. Yes, you could use it without reading the body because the function name, inputs, and output clearly describe what it does.
#The AI helped build my understanding because I only used it to explain what the errors meant instead of asking it to fix my code. I still had to find the bugs and make the corrections myself.




#--exercise1—
Def calculate_tax(price, rate):
        Return price * rate


tax1= calculate_tax (100, 0.07)
tax2 = calculate_tax (250, 0.08)


print(f”Tax on $100 at 7%: ${tax1:.2f}”)
print(f”Tax on $250 at 8%: ${tax2:.2f}”)


print(f”another tax: ${calculate_tax (150, 0.05):.2f}”)


#--Exercise2—


Def apply_discount (price, tier) : 
        If tier == “gold”
                Return price * 0.85
        Eilf tier == silver
                Return price * 0.90
        Elif tier == bronze
                Return price *95
        Else:
                Return price


print(f”gold: ${apply_discount(price, ‘gold’):.2f}”)
print(f”silver: ${apply_discount(print, ‘silver’):.2f}”)
print(f”bronze: ${apply_discount(print, ‘bronze’):.2f}”)
print(f’none: ${apply_discount(print, ‘none’):.2f}”)








#--exercise3–
Discounted = apply discount(200, “gold)
Tax = calculate_tax(discounted, 0.07)
After_tax = discounted + tax
print(f”After gold discount: ${discounted:.2f}”)
print(f”After Tax: ${after_tax:.2f}”)


Def final_price(price, tier, tax_rate):
        Discounted = apply_discount(price, tier)
        tax = calculate_tax(discounted, tax_rate)
        Return discounted + tax


print(f”Final price: ${final_price(200, ‘gold’, 0.07):.2f}”)


#--exercise4–
Orders = [(200, “gold”), (150, “silver”), (80, “bronze”), (500, “none”)]


For price, tier in orders:
        Total = final_price(price, tier, 0.07)
        print(f”price: ${price:.2f}, Tier {tier}, Final: ${total:.2f}”)


#---exercise5—
#The three bugs are putting = instead of += in line 4, a missing colon in line 7, and using <= #instead of just = in line 11. 


# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]


total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")


count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")


i = 0
while i = len(sales):
    print(sales[i])
    i += 1






#--exercise6–
x = 100


Def double_it():
        global x
        x = 999
        Return x * 2
print(x)
print(double_it())
print(x)