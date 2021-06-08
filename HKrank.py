if __name__ == '__main__':
    N = int(input())
    a = []
    for i in range(N):
        l = list(input().split())

        if l[0] == 'insert':
            a.insert(int(l[1]), int(l[2]))
        elif l[0] == 'remove':
            a.remove(int(l[1]))
        elif l[0] == 'append':
            a.append(int(l[1]))
        elif l[0] == 'sort':
            a.sort()
        elif l[0] == 'pop':
            a.pop()
        elif l[0] == 'reverse':
            a.reverse()

        elif l[0] == 'print':
            print(a)

