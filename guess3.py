import random
#讓使用者自行決定範圍
start = input('請決定隨機數字開始值：')
end = input('請決定隨機數字結束值：')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	x = input('請猜一個數字：')
	x = int(x)
	if x == r:
		print('終於猜對了')
		print('這是你猜的第', count ,'次')
		break
	elif x > r:
		print('比答案大')
	elif x < r:
		print('比答案小')
	print('這是你猜的第', count ,'次')
		
