import random

def reCaptcha():
    digits = {}
    digits[0] = ['###', '# #', '# #', '# #', '###']
    digits[1] = [' # ', ' # ', ' # ', ' # ', ' # ']
    digits[2] = ['###', '  #', '###', '#  ', '###']
    digits[3] = ['###', '  #', '###', '  #', '###']
    digits[4] = ['# #', '# #', '###', '  #', '  #']
    digits[5] = ['###', '#  ', '###', '  #', '###']
    digits[6] = ['###', '#  ', '###', '# #', '###']
    digits[7] = ['###', '  #', '  #', '  #', '  #']
    digits[8] = ['###', '# #', '###', '# #', '###']
    digits[9] = ['###', '# #', '###', '  #', '###']

    op = []
    op.append(['   ', ' # ', '###', ' # ', '   '])
    op.append(['   ', '   ', '###', '   ', '   '])
    op.append(['   ', '# #', ' # ', '# #', '   '])

    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 2)

    result = 0
    if c == 0:
        result = a + b
    elif c == 1:
        result = a - b
    else:
        result = a * b


    print('Show me that you are a human!')
    print('-' * 20)
    for i in range(5):
        print(' ' + digits[a][i] + '  ' + op[c][i] + '  ' + digits[b][i])
    print('-' * 20)

    try:
        ans = int(input('input your answer: '))
        if ans == result:
            return True
        return False
    except:
        return False

