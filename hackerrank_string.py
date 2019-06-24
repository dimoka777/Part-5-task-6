def hackerrank(s):
    counter = 0
    hack = 'hackerrank'
    for i in range(len(hack)):
        for j in range(len(s)):
            if s[j] == hack[i]:
                s = s[j + 1:]
                counter += 1
                break
    if counter == 10:
        print('YES')
    else:
        print('NO')


hackerrank('rhackerank')