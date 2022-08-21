class Stack:

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, s):
            self.items.append(s)

    def pop(self):
            return self.items.pop()

    def peak(self):
            return self.items[-1]
    
    def isEmpty(self):
            return self.items == []

    def size(self):
            return len(self.items)
    
    def hight_A(self):
        if self.size() > 0:
            return self.peak()
        else:
            return 0

S = Stack()
inp = input('Enter Input : ').split(',')


for i in inp:
    if i[0] == "A":
        while S.hight_A() <= int(i[2:]) and not S.isEmpty():
            S.pop()

        S.push(int(i[2:]))
        j_str = "".join(S.items) 
        print(j_str)    
    else:
         print(S.size())
       
