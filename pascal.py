def pascal():
    for i in range (n):
        for j in range (i+1):
            if j==0 or j==i:
                temp_list.append(1)
            else:
                temp_list.append(list1[i-1][j-1] + list1[i-1][j])
        print(temp_list)
n=int(input())
temp_list=[]
pascal()