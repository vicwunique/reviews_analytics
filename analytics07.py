
import time
import progressbar


data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        bar.update(count)
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


start_time = time.time()
wc = {}        # word_count(字典)     # 文字計數
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1   # 修改現有的 value 再存入 key
        else:
            wc[word] = 1    # 新增 key-value 到字典裡

print('檔案中合計出現過', len(wc), '個字，而重覆出現超過 100000 次的字如下：')

for word in wc:
    if wc[word] > 100000:
        print(word, ':', wc[word], '次')
end_time = time.time()

print('( 運算過程合計花費了', end_time - start_time, '秒 )')
print('----------------------------------------')

while True:
    word = input('請輸入欲查詢的字(輸入q即離開)：')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為：', wc[word], '次。')
    else:
        print('抱歉，查無此字。')

print('感謝您使用本查詢功能！')
print('----------------------------------------')
