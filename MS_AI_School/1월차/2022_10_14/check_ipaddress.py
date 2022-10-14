#IP주소를 확인하는 코드


import socket
#gethostname : pc의 이름을 호출 / gethostbyname : pc이름가지고 IP를 호출
in_addr = socket.gethostbyname(socket.gethostname())
print(in_addr)