def hbd(age):
    if age % 2 == 0:
        a = 20
        x = age / 2 
        y = int(x)
    else:
        a = 21
        x = age // 2 
        y = int(x)
    return f"saimai is just {a}, in base {y}!"

year = input("Enter year : ")
print(hbd(int(year)))

# Enter year : 555 
# saimai is just 21, in base 277!

# Enter year : 6
# saimai is just 20, in base 3!

# Enter year : 320
# saimai is just 20, in base 160!