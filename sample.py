import math

TAX = 1.1

Kingaku = int(input("商品の金額を入力してください"))

Kosuu = int(input("商品の個数を入力してください"))

sum = Kingaku * Kosuu * 1.1

print("合計金額は", math.floor(sum), "円です")
