p = [['*','*','*','*','*','*','*','*','*','*'],
    ['*','O','*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*','*','*','*']]
v=1
b=1
while True:
    for ka in p:
        for kl in ka:
            print(kl,end='')
        print()
    i = int(input())
    j = int(input())
    p[v][b]='*'
    p[i][j]='O'
    v=i
    b=j