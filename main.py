import time

Reset = '\033[0m'
Red = '\033[31m'
Cyan = '\033[34m'

sent = '0'

print('''Conversions you can do:
      Hours - Minutes - Seconds
      NOTATIONS [h - min - s]
      Kilmeters - Centimeters - Meters
      NOTATIONS [km - m - cm]''')

time.sleep(1)

Num = input("Enter the value you would like to convert with its unit(Example: 12m or 12min): ").lower()

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
    a_value = int(sent)
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
    a_value = int(sent)
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
        a_value = int(sent)
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
        a_value = int(sent)
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
        a_value = int(sent)
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
        a_value = int(sent)
        print("Would you like to convert the distance into (Kilometers) or (Centimeters)")
        user_Input = input(f"Enter {Cyan}1{Reset} for Kilometers and {Cyan}2{Reset} for Centimeters: ")
        if user_Input == '1':
            Km_val = a_value/1000
            print(f"Your converted value is {Red}{Km_val}km{Reset}")
        else:
            Cm_val = a_value * 100
            print(f"Your converted value is {Red}{Cm_val}cm{Reset}")
elif Unit == 'g':
    pass