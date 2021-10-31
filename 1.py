
a = 'b'
while a != 'q':
    print('c. 섭씨온도에서 화씨온도로 변환')
    print('f. 화씨온도에서 섭씨온도로 변환')
    print('q. 종료')
    a = str(input('원하는 프로그램을 입력하세요'))
    
    if a == 'c' :
        
        n = float(input('섭씨온도를 입력하세요.'))
        k = 9/5*n + 32
        print('화씨온도:', k)

    elif a == 'f' :
        
        p = float(input('화씨온도를 입력하세요.'))
        q = 5/9*(p-32)
        print('섭씨온도:', q)
    elif a == 'q':
        break
    else:
        print('잘못된 입력입니다.')
        break

print('프로그램을 종료합니다.')
