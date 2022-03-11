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
