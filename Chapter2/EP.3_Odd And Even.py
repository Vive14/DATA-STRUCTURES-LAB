def odd_even(type, data, mode):
    if type == "S":
        str = ""
        for i in range(len(data)):
            a = data[i]
            if mode == "Odd":
                if (i+1) % 2 == 1:
                    str += a # str.append(a) ABC  0 1 2
                    print(i)
            else:
                if (i+1) % 2 == 0:
                    str += a
        return str
            
    else:
        list = []
        data = data.split(" ")
        for i in range(len(data)):
            a = data[i]
            if mode == "Odd":
                if (i+1) % 2 == 1:
                    list.append(a)
            else:
                if (i+1) % 2 == 0:
                    list.append(a)
        return list  #"".join(list)
        

print("*** Odd Even ***")
m_input = input("Enter Input : ").split(",")
print(odd_even(m_input[0], m_input[1], m_input[2]))

# testcase 
# input1 S,ABCDEF,Odd input2 L,1 2 3 4 5,Even input3 L,ABC12345DEF,Odd input4 L,A B C 1 2 3 4 5 D E F,Odd