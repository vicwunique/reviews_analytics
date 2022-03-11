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

new = []
for d in data:
    if len(d) < 100:        # "篩選"長度<100的留言，新增到new清單內
        new.append(d)
print('留言長度小於100的共計有', len(new), '筆')
print('第一筆留言如下：')
print(new[0])
print('----------------------------------------')

good = []
for d in data:
    if 'good' in d:         # "篩選"內容有提到'good'的留言，新增到good清單內
        good.append(d)
print('留言內容有提到good的共計有', len(good), '筆')
print('第一筆留言如下：')
print(good[0])
print('----------------------------------------')
