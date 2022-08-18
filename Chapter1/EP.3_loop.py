print(" *** Summation of each digit *** ")
def getSum(n):
    
    sum = 0
    while (n != 0):
       
        sum = sum + (n % 10)
        n = n//10
    return sum

n = int(input("Enter a positive number : "))
print("Summation of each digit = ", getSum(n)) # ถ้าใส่ + ตรง ,ต้องใส่ str ด้วย


# จงเขียนโปรแกรมรับตัวเลขจำนวนเต็ม ไม่เกิน 30 หลัก แล้วหาผลรวมของเลขโดด แต่ละหลัก 
# รับตัวเลข 123 => 1+2+3=6
# รับตัวเลข 7892 => 7+8+9+2=26 
# รับตัวเลข 32189657 => 3+2+1+8+9+6+5+7=41


#  *** Summation of each digit ***
# Enter a positive number : 123
# Summation of each digit =  6

#  *** Summation of each digit ***
# Enter a positive number : 7892
# Summation of each digit =  26

# *** Summation of each digit ***
# Enter a positive number : 32189657
# Summation of each digit =  41

#  *** Summation of each digit ***
# Enter a positive number : 111111111122222222223333333333
# Summation of each digit =  60

