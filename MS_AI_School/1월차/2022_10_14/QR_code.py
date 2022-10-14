# QR 코드를 생성하는 기능

import qrcode

qr_data = 'www.naver.com'
qr_image = qrcode.make(qr_data)

qr_image.save(qr_data+'.png')

# text 파일을 불러와 그 안에 있는 내용으로 qr코드 생성

# 텍스트 파일을 읽기모드로 불러와 한줄씩 읽어서 리스트 생성
# with를 사용해서 파일을 열어 작업하면 with블록이 끝나는 순간 파일이 자동으로 닫힌다.
with open('site_list.txt', 'r', encoding='UTF8') as f:
    # 전체 파일에 있는 모든 라인을 읽음
    read_lines = f.readlines()
    for line in read_lines:
        # strip : 글자 이외의 것들을 떼어냄, \n 과 같은 특수문자들을 걸러낸다. 
        line = line.strip()

        # qr코드 생성하고 저장
        qr_data = line
        qr_image = qrcode.make(qr_data)

        qr_image.save(qr_data+'.png')


