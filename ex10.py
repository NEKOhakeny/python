# URLからファイルをダウンロード
import requests
url = "https://uaizuacjp-my.sharepoint.com/:x:/g/personal/s1280181_o365_u-aizu_ac_jp/EWLxYVXk6hZBk5duqpIsh6UBikqG9IKQGfdxXB11lYn8Cw?e=qKX70p"
r = requests.get(url, allow_redirects=True)
open('data.csv', 'wb').write(r.content)

# pandasでデータフレームに読み込み
import pandas as pd
df = pd.read_csv('data.csv', header=None)

# 一行目の文字列をスペースで分割
line = df.iloc[0,0]
words = line.split()

# 数字だけを抽出
numbers = []
for word in words:
  try:
    # 数字に変換できるか試す
    num = float(word)
    # 数字に変換できたらリストに追加
    numbers.append(num)
  except:
    # 数字に変換できなかったら無視
    pass

# 数字のリストを出力
#print(numbers)
print(*numbers, sep=" ")