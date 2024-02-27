def  factorial(n):
    if (n == 1):
        return 1
    else:
        return (n * factorial(n - 1))
    

#print(factorial(5))


def defactorial(a):
    total = 1
    curr_num = 1
    member_list = []
    while(total < a):
        total = total * curr_num
        member_list.append(curr_num)
        curr_num += 1

    if total == a:
        print(str(a), "=", "*".join(str(x) for x in member_list))
    else:
        print("Could not defactorial", a)

defactorial(24)
    