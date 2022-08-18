class Stack:
    def __init__(self, lis = None):    #ใช้สำหรับสร้าง list ว่าง
       if lis == None:
             self.items = []
       else:
            self.items = None

    def push(self, i):        #เก็บข้อมูลลง stack
        self.items.append(i)

    def pop(self):              #นำข้อมูลออกจาก stack
        return self.items.pop()
    
    def peek(self):               #มองข้อมูลจาก stack
        return self.items[-1]

    def isEmpty(self):          #รวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        return self.items == []

    def size(self):             #ตรวจสอบจำนวนข้อมูลใจ stack
        return len(self.items)

def isMatch(op, cl):
    open_paren = "({["
    close_paren = ")}]"
    return open_paren.index(op) == close_paren.index(cl)

def isMatch2(open_paren, close_paren):
    return (open_paren == "{" and close_paren == "}")or\
            (open_paren == "(" and close_paren == ")")or\
            (open_paren == "[" and close_paren == "]")

def parenMatch(paren):
    s = Stack()
    error = 0

    for i in range(len(paren)):
        if paren[i] in "({[":
            s.push(paren[i])
        elif paren[i] in ")}]":
            if s.size() > 0:
                a = s.peek()
                b = paren[i]
                if isMatch(a, b):
                    s.pop()  # ดึงข้อมูลออกมา เวลาดึงก็จะลบที่อยู่ใน stack ด้วย
                elif not isMatch2(a, b):
                    error = 1 #print("Unmatch open-close")
                    return error,s,paren,i
            else:
                error = 2 #print("close paren excess")
                return error,s,paren,i
                
    if not s.isEmpty()  :
        error = 3 #print("open paren excess")
        return error,s,paren,i 
    else:
        error == 4 #print("match")
        return error,s,paren,i 

bracket_input = input("Enter expresion : ")
err,s,paren,i = parenMatch(bracket_input)
j_str = "".join(s.items)
if err == 1:
    print(f"{bracket_input} Unmatch open-close")
elif err == 2:
    print(f"{bracket_input} close paren excess")
elif err == 3:
    print(f"{bracket_input} open paren excess   {s.size()} : {j_str}")
else:
    print(f"{bracket_input} MATCH")

