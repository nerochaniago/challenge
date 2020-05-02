def print_figure(high):
    for i in range(0,high):
        if i == high-1:
            break
        for j in range(0,i):
            print('*', end= ' ')
            for k in range(0,high-2):
                print('=', end= ' ')
            for l in range(0,high-4):
                print('*' ,end= ' ')
            print('\n')




input_user = 5
if input_user % 2 != 0:
    print_figure(input_user)
else:
    print('numbers must be odd')