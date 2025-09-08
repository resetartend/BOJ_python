import sys
import time

number = int(input("숫자를 입력하세요. :"))

start_time = time.time()
for i in range(number) :
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

end_time = time.time()

print('time :', (end_time - start_time) / number)