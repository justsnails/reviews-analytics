data = []
time = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		time += 1
		if time % 1000 == 0:
			print('正在讀取第', time, '筆資料')
print('讀取完畢，總計有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
ave = sum_len/len(data)	

print('全部字串的平均長度為', ave)


count = 0
for d in data:
	if len(d) < 100:
		count += 1
print('字串小於100的資料有', count, '筆')


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆資料小於100')
print(new[0])

