#setup
start_num = 2
end_num = 100

#programming
prime_num = list()
if start_num < 2:
    print('start_num can not less than 2')
else :
    for i in range(start_num, end_num):
        temp = True
        for j in range(2, i):
            if i % j == 0:
                temp = False
                break
        if temp == True:
            prime_num.append(i)
    print(len(prime_num), prime_num)