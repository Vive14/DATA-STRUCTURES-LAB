class Stack:
    def __init__(self):    #ใช้สำหรับสร้าง list ว่าง
        self.items = []

    def push(self, i):        #เก็บข้อมูลลง stack
        self.items.append(i)

    def pop(self):              #นำข้อมูลออกจาก
        return self.items.pop()

    def isEmpty(self):          #รวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        if len(self.items) == 0:
            return 1
        else:
            return 0

    def size(self):             #ตรวจสอบจำนวนข้อมูลใจ stack
        return len(self.items)

print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)
