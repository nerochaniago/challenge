number = [4,9,10,13,21]
value = []

def total_element(number):
    result1 = 0
    result2 = 0
    result3 = 0
    result4 = 0
    result5 = 0
    for i in range(0,len(number)):
        while number[i] != 4:
            result1 += number[i]
            break
        while number[i] != 9:
            result2 += number[i]
            break
        while number[i] != 10:
            result3 += number[i]
            break
        while number[i] != 13:
            result4 += number[i]
            break
        while number[i] != 21:
            result5 += number[i]
            break
    print('angka 4 : 9+10+13+21 = {}'.format(result1))
    print('angka 9 : 4+10+13+21 = {}'.format(result2))
    print('angka 10: 4+9+13+21 = {}'.format(result3))
    print('angka 13: 4+9+10+21 = {}'.format(result4))
    print('angka 21: 4+9+10+13 = {}'.format(result5))
    value.append(result1)
    value.append(result2)
    value.append(result3)
    value.append(result4)
    value.append(result5)
    total = sorted(value)
    print('Maka angka terkecilnya adalah {} dan {}'.format(total[0],total[1]))
    return ''


print(total_element(number))