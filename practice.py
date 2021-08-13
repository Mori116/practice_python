a = 90

if a == 100:  # a が 100 と等しければ、print()関数を実行する
    print("100点満点!") # インデント：4文字分が必要
else:
    print("失格!")


# if文以外の条件式
print("123は数字ですか？", "123".isdecimal())
print("abcは数字ですか？", "abc".isdecimal())
# isdecimal()：文字列が全て数字ならTrueを返す

string = input("文字列を入力してください:")
if string.isdecimal():
    print(string, "は数字です")
else:
    print(string, "は数字ではありません")


print("123はアルファベットですか？", "123".isalpha())
print("abcはアルファベットですか？", "abc".isalpha())
# isalpha()：文字列が全てアルファベットならTrueを返す

string = input("文字列を入力してください:")
if string.isdecimal():
    print(string, "は数字です")
elif string.isalpha():
    print(string, "はアルファベットです")
else:
    print(string, "は数字でもアルファベットでもありません")


# プール型(TrueかFalseが返ってくる)
print("abc" == "abc")
print(1 > 2)


# and演算子
# 年齢が 10 またはそれより大きい/身長が 120 またはそれより大きい
age = 9
height = 130

if (10 <= age) and (120 <= height):
    print("乗車可能です")
else:
    print("ご遠慮ください")


# or演算子
# 年齢が10以下/年齢が80以上
age = 70
if (age <= 10) or (80 <= age):
    print("ご遠慮ください")
else:
    print("乗車可能です")


# not演算子
# 10歳以外
age = 9
if not (age < 10):
    print("乗車可能です")
else:
    print("ご遠慮ください")