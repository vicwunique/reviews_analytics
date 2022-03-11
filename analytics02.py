data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 1000 == 0:       # 使用 count 在每1000次時列印出讀取進度 (求餘數使用%)
            print(len(data))
print('檔案讀取完畢，總共有', len(data), '筆留言')
print('----------------------------------------')
print('第一筆留言如下：')
print(data[0])
print('----------------------------------------')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)      # 此處將字串當清單，使用 len() 計算留言長度；sum_len 計算總留言長度
print('平均留言長度為', sum_len/len(data))
print('----------------------------------------')
