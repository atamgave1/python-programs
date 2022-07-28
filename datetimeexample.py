import datetime
today=datetime.datetime.now()
print("TOdays date:", today)
form1=today.strftime("%d/%m/%Y")
print(form1)
form2=today.strftime("%B %d,%Y")
print(form2)
form3=today.strftime("%b-%m-%Y")
print(form3)
