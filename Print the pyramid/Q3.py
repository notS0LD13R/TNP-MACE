for _ in range(int(input())):
    height=int(input())
    for i in range(1,height+1):
        print((('  '*(height-i)))+('* '*(2*i-1)))