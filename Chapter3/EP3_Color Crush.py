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


inp = input("Enter Input : ").split()
S = Stack()
temp = None
combo = 0

for x in inp:
    if S.size() < 2:
        S.push(x)
    elif S.peek() == x:
        temp = S.pop()
        if S.peek() != x:
            S.push(x)
            S.push(temp)
        else:
            S.pop()
            temp = None
            combo += 1
    elif S.peek() != x:
        S.push(x)


print(S.size())
j_str = "".join(S.items)
if S.size() == 0:
    print("Empty", end='')
else:
    for items in range (S.size()-1, -1, -1):
        print(S.items[items], end='')

if combo > 1:
    print("\nCombo :",str(combo),"! ! !")

