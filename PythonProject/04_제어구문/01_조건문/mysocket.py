import socket

ip = '192.168.10.60' # 문자열
port = 21            # 숫자

s = socket.socket()
s.connect((ip, port))
ans = s.recv(1024)
print(ans) # binary 형태로 전송이 된 것 확인 가능

if 'vsFTPd 2.3.4' in str(ans):
    print('[  OK  ] Backdoor Command Execution')
elif 'vsFTPd 3.0.3' in str(ans):
    print('[  OK  ] Remote Denial of Service')
elif 'vsFTPd 2.0.5' in str(ans):
    print('deny_file Option REmote Denial of Service')
else:
    print('[ FAIL ] Not Vulunerable')