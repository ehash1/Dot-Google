# created ehash1 05.09.2019

import re

email = input('input e-mail without <@gmail.com> and dot:')
match = re.match('^[A-Za-z0-9_-]*$', email)
if match:
    count = input('count email: ')
    for i in range(int(count)):
        print(email + '+' + str(i) + '@gmail.com')
