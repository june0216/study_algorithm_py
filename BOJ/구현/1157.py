words = input().upper()
word = list(set(words))
cnt_list = []

for w in word:
    cnt = words.count(w)
    cnt_list.append(cnt)
if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(word[max_index])

