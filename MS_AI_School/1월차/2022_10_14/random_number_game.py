# 숫자 맞추기 게임
# 컴퓨터가 임의의 숫자를 생성하고 사용자가 숫자를 입력해 맞추는 게임이다.

import random
# 1~100사이의 정수를 무작위 생성한다.
random_number = random.randint(1,100)
# 입력횟수 카운터
game_count = 1

while True:
    try:
    
        my_number = int(input("1-100사이의 숫자를 입력하세요. : "))

        if(my_number > random_number):
            print("Down!!")
        elif(my_number < random_number):
            print("Up!!")
        else:
            print("축하합니다. {}번 만에 맞추셨습니다.".format(game_count))
            break
        
        game_count = game_count+1
    #예외처리문. 입력값이 숫자가 아니면 출력한다.
    except :
        print("숫자로 입력해주세요.")