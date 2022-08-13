# รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 ให้ show 
# ผลรวมของจำนวนทั้งสอง แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 ให้ show ผลคูณของจำนวนทั้งสอง

print("*** multiplication or sum ***")
x, y = [int(x) for x in input("Enter num1 num2 : ").split()]
z = x*y
if z > 1000:
    print("The result is", x+y)
else :
    print("The result is " + str(x*y))

# *** multiplication or sum ***
# Enter num1 num2 : 20 30
# The result is 600

# *** multiplication or sum ***
# Enter num1 num2 : 40 60
# The result is 100