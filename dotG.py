# created ehash1 05.09.2019

import re

email = input('input e-mail without <@gmail.com> and dot:')
match = re.match('^[A-Za-z0-9_-]*$', email)
if match:
    print('\ncount char in email: ', len(email))


    arrMail = list(re.sub('(?<=\w)(\w)', ' \\1',(email)))
    for n in range(len(arrMail)):
        if arrMail[n] == ' ':
            arrMail[n] = ''

    lenX = len(email)-1
    print('total items :',pow(2, lenX))
    print('\nPattern dots:\n')

    i = 0
    while i < pow(2, lenX):

        pattern = '0' + (re.sub('(?<=\w)(\w)', '0\\1', (bin(i)[2:].zfill(lenX)))) + '0'
        pattern = list(pattern)

        for n in range(len(pattern)):
            if pattern[n] == '1':
                pattern[n] = '.'
            else:
                pattern[n] = ''

            dotG = pattern[n]+arrMail[n]
            print(str(dotG), end='')

        print("@gmail.com")
        i += 1
