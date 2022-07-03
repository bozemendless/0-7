# 0-7 問三次TF猜出來
num = 0
a_group = "1,3,5,7\n" #2進位的XX1
b_group = "2,3,6,7\n" #2進位的X1X
c_group = "2,4,6,7\n" #2進位的1XX
truefalse = "有沒有這些數字啊~請回答T or F\n"

TorF = input(a_group + truefalse)
if TorF == "T" or TorF == "t":
    num += 1
TorF = input(b_group + truefalse)
if TorF == "T" or TorF == "t":
    num += 2
TorF = input(c_group + truefalse)
if TorF == "T" or TorF == "t":
    num += 4
print(f"你猜的就是{num:3.0f}")