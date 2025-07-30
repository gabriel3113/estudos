valid_name = False
valid_salary = False
valid_bonus = False

while not valid_name:
    try:
        name = input("Enter your name: ")
        if len(name) == 0 :
            raise ValueError("Empty field")
        elif any(char.isdigit() for char in name):
            raise ValueError("The name can't have numbers")
        else:
            valid_name = True
            print('Valid name')
    
    except ValueError as e:
        print(e)

while not valid_salary:
    try:
        salary = input("Enter the value of your salary: ")
        
        if len(salary) == 0:
            raise ValueError("Empty Field")
        elif any(char.isalpha() for char in salary):
            raise ValueError("Salary can't contain letters")
        salary = float(salary)
        if salary <= 0 :
            raise ValueError("please enter a valid salary")
        else:
            valid_salary = True
    except ValueError as e:
        print(e)

while not valid_bonus:
    try:
        bonus = input('Enter the value of your bonus: ')
        if len(bonus) == 0 : 
            raise ValueError("Empty field")
        elif any(c.isalpha() for c in bonus):
            raise ValueError("please enter a valid salary")
        
        bonus = float(bonus)

        if bonus <= 0 :
            raise ValueError("enter a positive bonus")
        valid_bonus = True
    except ValueError as e:
        print(e)

plr = (salary + 1000) * bonus

print(f"congratulations{name} your plr is {plr} ")