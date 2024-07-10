data = []
time = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		time += 1
		if time % 1000 == 0:
			print('正在讀取第', time, '筆資料')
print('總計有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
ave = sum_len/len(data)	

print('全部字串的平均長度為', ave)