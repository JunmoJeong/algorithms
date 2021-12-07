from datetime import datetime

now = datetime.now()
current_hour = now.strftime("%H")
current_hour = int(current_hour)

if current_hour % 2 == 0:
    with open("time.txt", "a") as f:
        current_hour = str(current_hour)
        f.write(current_hour + '시\n')
else:
    print("홀수 시간입니다.")
