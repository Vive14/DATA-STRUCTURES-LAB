# def three_sum(num):
#     pass




# n = [int(x) for x in input("Enter Your List :").split(" ")]
# print(n)


def threeofsum(num):
    num.sort()
    result = []
    for i in range(0,len(num)):
        for j in range(i+1,len(num)):
            for k in range(j+1,len(num)):
                if num[i] + num[j] + num[k] == 5 and [num[i],num[j],num[k]] not in result:
                    result.append([num[i],num[j],num[k]])

    return result
 

List = list(input("Enter Your List : ").split())
print(List)
List = [int(i) for i in List]
if len(List) > 2:
    print(threeofsum(List))
else:
    print("Array Input Length Must More Than 2")
