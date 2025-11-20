#conditional statements

'''
if(if condition :)
only one condition

if-else
one condition,two actions

if-elif....-else
multiple conditions

nested if
'''

#if
send=True
if send:
    print("send the message")
    
send=False
if not send:
    print("message not sent")

#if-else
data={'ajay@gmail.com':1234,'ruchita@gmail.com':5678,'satish@gmail.com':2222,'tejaswini@gmail.com':9876}
mail=input("enter the mail: ")
pwd=int(input("enter the password: "))

if data.get(mail)==pwd:
    print("valid login")
else:
    print("invalid login")

#if-elif
amount=int(input("enter the amount: "))
actual_amount=amount
if amount>=10000:
    actual_amount=amount-amount*0.5
elif 8000<amount<10000:
    actual_amount=amount-amount*0.3
elif 5000<amount<8000:
    actual_amount=amount-amount*0.2
elif 2000<amount<5000:
    actual_amount=amount-amount*0.05

print(f"Amount: {amount}\nAfter discount: {actual_amount}")


budget=int(input("enter the budget: "))
if budget>20000:
    print("Trip to goa")
elif 15000<=budget<20000:
    print("Go for shopping")
elif 10000<=budget<15000:
    print("Clubbing")
elif 5000<=budget<10000:
    print("Go for cafe")
elif 2000<=budget<5000:
    print("Go for movie")
elif 1000<=budget<2000:
    print("Go to temple")
elif 500<=budget<1000:
    print("Saloon")
elif 100<=budget<500:
    print("Mobile recharge")
elif 10<=budget<100:
    print("Have tea")
else:
    print("Go to sleep")

data={
    1:'Satish will sing',
    2:'Telugu dialogue- Krishna',
    3:'Imran will give party',
    4:'Ramp walk-teja',
    5:'ask a question-ajay',
    6:'Anything-sumanth'
    }

    
print(data)
ch= int(input("Enter the choice: "))
if 1<=ch<=6:
    print(data[ch])
else:
    print("Invalid choice")

#nested if
products=['laptop','mouse','phone','keyboard','charger','speaker']
stock=[100,20,500,0,200,6]
print("*"*30)
print(products)
print("*"*30)


network=True

if network:
    product=input("Enter the product: ").strip()
    if product in products:
        index = products.index(product)
        if stock[index]==0:
            print(f'{product}- Out of stock')
        elif 1<=stock[index]<=10:
            print(f'{product}- Only few items left. Hurry up')
        else:
            print(f'{product}')

    else:
        print("product not found")

else:
    print("Checkout the internet")

data={
    'ajay':{'python':99,'mysql':88,'flask':90},
    'krishna':{'python':29,'mysql':100,'flask':50},
    'ruchita':{'python':98,'mysql':96,'flask':99},
    'nishitha':{'python':85,'mysql':86,'flask':87},
    'praneetha':{'python':50,'mysql':70,'flask':60},
    'sumanth':{'python':10,'mysql':20,'flask':30}
    }
user=input("Enter the user: ")
avg= data[user]['python']+data[user]['mysql']+data[user]['flask']
if 80<=avg<=100:
    print(f'{user} got "A" grade. \nKeep it up')
elif 60<=avg<80:
    print(f'{user} got "B" grade. \nGood, Need to improve')
elif 40<=avg<60:
    print(f'{user} got "C" grade. \nGAverage, Practice well for exams')
elif 40<avg:
    print(f'{user} got Failed. \nBring your parents')
    
    

        
        
