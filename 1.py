def count_handshake(n):
    temp = 0
    for i in range(0,n):
        temp += i
    return temp

result_1 = count_handshake(4)
result_2 = count_handshake(7)

print('result : {} '.format(result_1))
print('result : {} '.format(result_2))