class Stack:
    def __init__(self, lis=None):  # ใช้สำหรับสร้าง list ว่าง
        if lis == None:
            self.items = []
        else:
            self.items = list

    def push(self, s):  # เก็บข้อมูลลง stack
        self.items.append(s)

    def pop(self):  # นำข้อมูลออกจาก stack
        return self.items.pop()

    def peek(self):  # มองข้อมูลจาก stack
        return self.items[-1]

    def isEmpty(self):  # รวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        return self.items == []

    def size(self):  # ตรวจสอบจำนวนข้อมูลใจ stack
        return len(self.items)

def dec2bin(decnum):

    s = Stack()
    output=""
    while decnum > 0:
        s.push(decnum % 2)
        decnum = decnum // 2
        
    while s.size() != 0:
        output+=str(s.pop())
    return output
    
print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))