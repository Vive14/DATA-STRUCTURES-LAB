print("*** TorKham HanSaa ***")
en_input = input("Enter Input : ").split(",")
two_last_text = None
word_memory = []

for i in en_input:
    # print(i) #P apple
    mode = i.split()
    print(mode) # P
    if mode == "R":
        word_memory.clear() #clear list
        two_last_text = None
        print("game restarted")
    elif mode == "X":
        break
    elif mode == "P":
        text = i.split()[1] #"apple" "lemon"
        print(f"'{text}' -> ",end="")
        two_befor_text = text[:2].lower()  # "ap" "le"
        if two_last_text == None or two_last_text == two_befor_text:
            word_memory.append(text)
            two_last_text = text[-2:].lower() #apple -> le
            print(word_memory)
        else:
            print("game over")
            break
    else:
        print(f"'{i}' is Invalid Input !!!")
        break


#test case 
# input1 P Apple,P LEMON,R,P onion,X                       input2 R,R,P KK,R,P apple,R,P Lemon,R,X 
# input3  P apPLE,P leMON,R,P Durian,P ant,P pineapple,X   input4 P apple,p lemon,P onion,X