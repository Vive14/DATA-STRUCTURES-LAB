def weirdSubtract(n,k):
    for i in range(k): 
        num_str = str(n)
        last_digit_str = num_str[-1]
        last_digit = int(last_digit_str)
        if last_digit == 0:
            n = n//10
            num_str = n
        else:
            n -=1
            num_str = n
    return num_str
       
n,s = input("Enter num and sub : ").split()
print(weirdSubtract(int(n),int(s)))


# testcase input1 163 8 -> 12