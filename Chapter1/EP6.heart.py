print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
N_MINUS = n - 1
for y in range(3 * n - 2): # n + (n-1) * 2
    for x in range(4 * n - 3): # n*2 + (n-1) + (n-2)
        line1 = N_MINUS - y
        line2 = y + N_MINUS
        line3 = 3 * N_MINUS - y
        line4 = y + N_MINUS * 3
        line5 = y - N_MINUS
        line6 = 5 * N_MINUS - y
        region_left = line1 < x < line2 and y < n
        region_right = line3 < x < line4 and y < n
        region_bot = line5 < x < line6 and y >= n
        if x in (line1, line5, line6) or (x in (line2, line3, line4) and y < n):
            print("*", end='')
        elif region_left or region_right or region_bot:
            print("+", end='')
        else:
            print(".", end='')
    print()