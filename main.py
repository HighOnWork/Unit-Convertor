import time

Reset = '\033[0m'
Red = '\033[31m'
Cyan = '\033[34m'

sent = '0'

print('''Conversions you can do:
      Hours - Minutes - Seconds
      NOTATIONS [h - min - s]
      Kilmeters - Centimeters - Meters
      NOTATIONS [km - m - cm]
      Kilograms - Grams - Miligrams
      NOTATIONS [kg - g - mg]''')

time.sleep(1)

valid_units = ['h', 'min', 's', 'km', 'm', 'cm', 'kg', 'g', 'mg']
Num = input("Enter the value you would like to convert with its unit(Example: 12m or 12min): ").lower()
if Num not in valid_units:
    print("Invalid unit provided try again...")

unit_difference = Num[-2:]
if unit_difference == 'in':
    unit_difference = Num[-3:]

length = len(Num)

Num = list(Num)

if unit_difference == 'min':
    Unit = Num[-3]
else:
    Unit = Num[-1]



#Hours
if Unit == 'h':
    value = Num[0: -1]
    for val in value:
        sent += val
    a_value = float(sent)
    print("Would you like to convert the time into (minutes) or (seconds)")
    user_Input = input(f"Enter {Cyan}1{Reset} for minutes and {Cyan}2{Reset} for seconds: ")
    if user_Input == '1':
        m_val = a_value * 60
        m_val = round(m_val, 3)
        print(f"Your converted value is {Red}{m_val}m{Reset}")
    else:
        s_val = a_value * 3600
        s_val = round(s_val, 3)
        print(f"Your converted value is {Red}{s_val}s{Reset}")
#Seconds
elif Unit == 's':
    value = Num[0: -1]
    for val in value:
        sent += val
    a_value = float(sent)
    print("Would you like to convert the time into (1.hours) or (2.minutes)")
    user_Input = input(f"Enter {Cyan}1{Reset} for hours and {Cyan}2{Reset} for minutes")
    if user_Input == '1':
        h_val = a_value/3600
        h_val = round(h_val, 3)
        print(f"Your converted value is {Red}{h_val}h{Reset}")
    else:
        m_val = a_value/60
        m_val = round(m_val, 3)
        print(f"Your converted value is {Red}{m_val}m{Reset}")
        
elif Unit == 'm':
    
    
    #Minutes shortened to in
    if unit_difference == 'min':
        print("On to converting minutes")
        value = Num[0: length - 3]
        for val in value:
            sent += val
        a_value = float(sent)
        print("Would you like to convert the time into (1.hours) or (2.seconds)")
        user_Input = input(f"Enter {Cyan}1{Reset} for hours and {Cyan}2{Reset} for seconds: ")
        if user_Input == '1':
            h_val = a_value/60
            h_val = round(h_val, 3)
            print(f"Your converted value is {Red}{h_val}h{Reset}")
        else:
            s_val = a_value * 60
            s_val = round(s_val, 3)
            print(f"Your converted value is {Red}{s_val}s{Reset}")
    

    elif unit_difference == 'cm':
        value = Num[0: length - 2]
        for val in value:
            sent += val
        a_value = float(sent)
        print("Would you like to convert the distance into (Kilometers) or (Meters)")
        user_Input = input(f"Enter {Cyan}1{Reset} for Kilometers and {Cyan}2{Reset} for Meters: ")
        if user_Input == '1':
            Km_val = a_value/100000
            print(f"Your converted value is {Red}{Km_val}km{Reset}")
        else:
            Cm_val = a_value / 100
            print(f"Your converted value is {Red}{Cm_val}m{Reset}")
    
    elif unit_difference == 'km':
        value = Num[0: length - 2]
        for val in value:
            sent += val
        a_value = float(sent)
        print("Would you like to convert the distance into (Kilometers) or (Meters)")
        user_Input = input(f"Enter {Cyan}1{Reset} for Meters and {Cyan}2{Reset} for Centimeters: ")
        if user_Input == '1':
            Km_val = a_value * 1000
            print(f"Your converted value is {Red}{Km_val}m{Reset}")
        else:
            Cm_val = a_value * 100000
            print(f"Your converted value is {Red}{Cm_val}cm{Reset}")

    else:
        value = Num[0: -1]
        for val in value:
            sent += val
        a_value = float(sent)
        print("Would you like to convert the distance into (Kilometers) or (Centimeters)")
        user_Input = input(f"Enter {Cyan}1{Reset} for Kilometers and {Cyan}2{Reset} for Centimeters: ")
        if user_Input == '1':
            Km_val = a_value/1000
            print(f"Your converted value is {Red}{Km_val}km{Reset}")
        else:
            Cm_val = a_value * 100
            print(f"Your converted value is {Red}{Cm_val}cm{Reset}")
elif Unit == 'g':
    if unit_difference == 'kg':
        value = Num[0: length - 2]
        for val in value:
            sent += val
        a_value = float(sent)
        print("Would you like to convert the distance into (Grams) or (Miligrams)")
        user_Input = input(f"Enter {Cyan}1{Reset} for Grams and {Cyan}2{Reset} for Miligrams: ")
        if user_Input == '1':
            g_val = a_value * 1000
            print(f"Your converted value is {Red}{g_val}g{Reset}")
        else:
            mg_val = a_value * 100000
    
    elif unit_difference == 'mg':
        value = Num[0: length - 2]
        for val in value:
            sent += val
        a_value = float(sent)
        print("Would you like to convert the distance into (Kilograms) or (Grams)")
        user_Input = input(f"Enter {Cyan}1{Reset} for Kilograms and {Cyan}2{Reset} for Grams: ")
        if user_Input == '1':
            Kg_val = a_value/1000000
            print(f"Your converted value is {Red}{Kg_val:.7f}kg{Reset}")
        else:
            mg_val = a_value / 1000
            print(f"Your converted value is {Red}{mg_val}g{Reset}")

    else:
        value = Num[0: -1]
        for val in value:
            sent += val
        a_value = float(sent)
        print("Would you like to convert the weight into (Kilograms) or (Miligrams)")
        user_Input = input(f"Enter {Cyan}1{Reset} for Kilograms and {Cyan}2{Reset} for Miligram: ")
        if user_Input == '1':
            Kg_val = a_value/1000
            print(f"Your converted value is {Red}{Kg_val}kg{Reset}")
        else:
            mg_val = a_value * 1000
            print(f"Your converted value is {Red}{mg_val}mg{Reset}")
