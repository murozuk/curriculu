while True:
	try:
		print()
		print('1: ValueError例外を発生')
		print('2: IndexError例外を発生')
		print('3: 例外を発生させない')
		print('4: 終了')
		number = int(input('選択してください。: '))
        # 問①：if文を用いて、以下の画像のように処理されるように記述しましょう。
		if number == 1:
			print("↓")
			print("ValueError")
			error1 = int("hoge")
					
			
		elif number == 2:
			print("↓")
			print("IndexError")
			error2 = ""[0]
			

		elif number == 3:
			print("↓")
			print("例外を発生させませんでした")
			
	except ValueError as e:
		print(e.args)
		print("↓")
		print("もう一度選択しましょう")

	except IndexError as d:
		print(d.args)
		print("↓")
		print("もう一度選択しましょう")

		
    # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。
	else:
		if number == 4:
			print('↓')
			print("終了します")
			print('↓')
			print('無限ループを終了します')
			break

		else:
			print("↓")
			print("もう一度選択しましょう")