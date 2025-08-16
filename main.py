Reset = '\033[0m'
Red = '\033[31m'
Cyan = '\033[34m'

sent = '0'

print('''Conversions you can do:
      Hours - Minutes - Seconds''')

Num = input("Enter the value you would like to convert with its unit(Example: 12m): ").lower()

Num = list(Num)
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
        m_val = round(m_val, 2)
        print(f"Your converted value is {Red}{m_val}m{Reset}")
    else:
        s_val = a_value * 3600
        s_val = round(s_val, 2)
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
        h_val = round(h_val, 2)
        print(f"Your converted value is {Red}{h_val}h{Reset}")
    else:
        m_val = a_value/60
        m_val = round(m_val, 2)
        print(f"Your converted value is {Red}{m_val}m{Reset}")
#Minutes
elif Unit == 'm':
    value = Num[0: -1]
    for val in value:
        sent += val
    a_value = int(sent)
    print("Would you like to convert the time into (1.hours) or (2.seconds)")
    user_Input = input(f"Enter {Cyan}1{Reset} for hours and {Cyan}2{Reset} for seconds")
    if user_Input == '1':
        h_val = a_value/60
        h_val = round(h_val, 2)
        print(f"Your converted value is {Red}{h_val}h{Reset}")
    else:
        s_val = a_value * 60
        s_val = round(s_val, 2)
        print(f"Your converted value is {Red}{s_val}s{Reset}")
