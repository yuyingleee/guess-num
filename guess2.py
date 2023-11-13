#產生一個隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對的話 印出“終於猜對了！”
#猜錯的話 要告訴他 比答案大/小

import random
r = random.randint(1, 100)
count = 0
while True:
	count = count + 1  #count += 1快寫法
	x = input('請猜一個介於1到100的數字:')
	x = int(x)
	if x == r:
		print('終於猜對了！')
		print('這是你猜的第', count ,'次')
		break

	elif r < x:
		print('比答案大')
	elif r > x:
		print('比答案小')
	print('這是你猜的第', count ,'次')