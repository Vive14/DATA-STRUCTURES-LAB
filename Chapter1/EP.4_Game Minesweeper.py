# สร้างฟังก์ชันที่รับ input เป็น list(5x5) ของ # และ - โดยแต่ละแฮช (#) แทนทุ่นระเบิดและแต่ละขีด (-) 
# แทนจุดที่ไม่มีทุ่นระเบิด ให้ return list ที่แต่ละขีดถูกแทนที่ด้วยตัวเลขที่ระบุจำนวนของทุ่นระเบิดที่อยู่ติดกับจุดนั้น (แนวนอนแนวตั้งและแนวทแยงมุม)
# Enter input(5x5) : - - - # -,- # - - -,- - # - -,- - - - -,- # - - -
# Enter input(5x5) : - - - - -,- - - - -,- - # - -,- - - - -,- - - - -


print("*** Minesweeper ***")
input_list = input("Enter input(5x5) : ").split(",")
list = []

print()
print()

for x in input_list:
    x = x.split(" ")
    list.append(x)
    print(x)

print()
print()

for row in range(len(list)):
    for cell in range(len(list[row])):
        c = list[row][cell]
        if c == "-":
            list[row][cell] = 0

for row in range(len(list)):
    for cell in range(len(list[row])):
        c = list[row][cell]
        if c == "#":
            for y in range(-1,2): # -1 0 1
                for x in range(-1, 2):
                    case1 = row + y < 0 or cell + x < 0
                    case2 = row + y > 4 or cell + x > 4
                    if case1 or case2:
                        continue
                    elif list[row+y][cell+x] == "#":
                        continue
                    else:
                        list[row+y][cell+x] +=1 
            
for row in range(len(list)):
    for cell in range(len(list[row])):
        c = list[row][cell]
        if c != "#":
            list[row][cell] = str(c)

for x in list:
    print(x)