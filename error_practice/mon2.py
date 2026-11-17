# 第2問：合計金額の計算と表示
price = 500
tax = 50

#price = int(500)      int処理しなくても大丈夫だと後で気づきました。
#tax = int(50)　　　　　int処理しなくても大丈夫だと後で気づきました。

total = price + tax

#print("合計金額は " + total+ " 円です。")
#print("合計金額は " + {total}+ " 円です。")
print("合計金額は " + str(total)+ " 円です。")
#TypeError: can only concatenate str (not "int") to str
#TypeError: can only concatenate str (not "set") to str