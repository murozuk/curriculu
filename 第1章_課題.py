# int型のリストdataを作成し、値を1,3,5,7で初期化
data = [1, 3, 5, 7]


for i in data:
    print(i ** 2 )

for j in range(len(data)):
    print(data[j] ** 2)

all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
	if place in "横浜":
        	print(place + "のチケットが当選しました！")

	elif place in {"札幌","大阪"}:
        	print(place + "のチケットは結果待ち")

	else:
		print(place + "のチケットは落選しました")

three_place = get_place + wait_place

print("{}と{}と{}のチケットが当選しました!".format(*three_place))

