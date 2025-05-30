import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
\d
Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'
user_input = input()
#x = re.compile(r'coreyms\.com')
x = re.compile(user_input)
y=x.finditer(text_to_search)
for i in y:
    print(i)
    k = 24
    #print(str(i)[24:k])
    num1 = ''
    num2 = ''
    s1 = str(i)[k:]
    for j in s1:
        #print(j)
        if j.isnumeric():
            num1 += j
            #print(num1)
            k+=1
        else:
            break
    num1 = int(num1)
    #m = k+3
    s2 = str(i)[k+2:]
    for l in s2:
        if l.isnumeric():
            num2 += l
        else:
            break
    num2 = int(num2)
    print(num1)
    print(num2)
    print(text_to_search[num1:num2])

