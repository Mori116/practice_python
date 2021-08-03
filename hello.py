print ("Hello World!")


# 変数使用
momo = 100 * 5
mikan = 40 * 8
nashi = 80 * 5
suika = 90 * 2
print (momo + mikan + nashi + suika)


# 使用頻度の高い関数は、モジュールを指定せずに使用可能
abs_practice = abs(100)
abs_practice_2 = abs(100 * -1) # 負の値を指定しても、正の値に変換されて返ってくる
print (abs_practice)
print(abs_practice_2)

round_practice = round(1.12, 1) # 第2引数の指定で、小数部分の表示箇所を選択する。(1.12, 2)の場合=1.12となる
print(round_practice)

min_practice = min(10, 20, 5, 30) # 最小値を表示する
print(min_practice)

max_practice = max(10, 20, 5, 30) # 最大値を表示する
print(max_practice)


# ここから
# 以下、モジュールを指定してから使用する必要がある
import math # mathモジュールを使用します宣言
math_practice = math.sqrt(2.0) # インポート済みの mathモジュールを使って、平方根を計算する
print(math_practice)

import calendar # calenderモジュールを使用します宣言
calendar.prmonth(2021, 8) # 2021年８月のカレンダーを表示する

print("もも５つとみかん８つで", 100 * 5 + 40 * 8, "円です。")
# 文字列と数値の表示
#ここまで


string = input("文字を入力してください：")
print("文字", string, "が入力されました。")
# input関数でキーボードから入力が可能


text = "123"
print(int(text))
# integer型(整数)に変換できる

text = "123.4"
print(float(text))
# float型に変換できる

num = 123
print(str(num))
# string型(文字型)に変換できる


text = "lower letters"
uppered_text = text.upper()
print(uppered_text)
# upper()メソッドで文字列を大文字へ変換する

text = "LOWER LETTERS"
lower_text = text.lower()
print(lower_text)
# lower()メソッドで文字列を小文字へ変換する

text = "The shells she sells are sea-shells, I'm sure."
find_text = text.find("sea")
print(find_text)
# 結果：25（25番目の文字がseaであるの意。※先頭の文字を０から数える）


data = 0.5
data_integer = data.as_integer_ratio()
print(data_integer)
# 実数を分数のように2つの整数の比で表す


# 比較演算子
true = 100 > 10
print(true)

false = 10 > 100
print(false)


# 文字列の比較
# 数字は、文字の0が最小、9が最大(0 < 1 < 2 < ... < 9)
# アルファベットでは、a が最小、z が最大 (a < b < c < ... < z)
# 大文字は小文字より小さい (A < a, B < b, ...)
# 数字は、アルファベットよりも小さい (0 < 9 < A)
number = '123' < '456'
print(number)

lang = 'python' < 'Python'
print(lang)

lang_1 = 'Python-1' < 'Python-a'
print(lang_1)