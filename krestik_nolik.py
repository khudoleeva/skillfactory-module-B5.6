L = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
M = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
print(L[0][0], "|", L[0][1], "|", L[0][2])
print(L[1][0], "|", L[1][1], "|", L[1][2])
print(L[2][0],"|", L[2][1], "|", L[2][2])
L = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

def input_a():
	global M
	a = input("Игрок 'КРЕСТИК' введите номер клетки:   ")
	if a not in M[0] and a not in M[1] and a not in M[2]:
		print("Неверный номер")
		return input_a()
	else:
		return a
def input_b():
	global M
	a = input("Игрок 'НОЛИК' введите номер клетки:   ")
	if a not in M[0] and a not in M[1] and a not in M[2]:
		print("Неверный номер")
		return input_b()
	else:
		return a
def fun_krest(af):
	global M
	global L
	b = af()
	for i in [0, 1, 2]:
		for j in [0, 1, 2]:
			if b == M[i][j]:
				M[i][j] = "X"
				L[i][j] = "X"
	print(L[0][0], "|", L[0][1], "|", L[0][2])
	print(L[1][0], "|", L[1][1], "|", L[1][2])
	print(L[2][0], "|", L[2][1], "|", L[2][2])
def fun_nolik(f):
	global M
	global L
	b = f()
	for i in [0, 1, 2]:
		for j in [0, 1, 2]:
			if b == M[i][j]:
				M[i][j] = "O"
				L[i][j] = "O"
	print(L[0][0], "|", L[0][1], "|", L[0][2])
	print(L[1][0], "|", L[1][1], "|", L[1][2])
	print(L[2][0], "|", L[2][1], "|", L[2][2])

def proverka():
	global M, L
	for i in range(len(M)):
		if M[i][0] == M[i][1] == M[i][2]:
			print(f'Победил {"НОЛИК" if M[i][0] == "O" else "КРЕСТИК"}')
			return True
		elif M[0][i] == M[1][i] == M[2][i]:
			print(f'Победил {"НОЛИК" if M[0][i] == "O" else "КРЕСТИК"}')
			return True
		elif i == 0 and (M[i][i] == M[i + 1][i + 1] == M[i + 2][i + 2] or M[i][i + 2] == M[i + 1][i + 1] == M[i + 2][i]):
			print(f'Победил {"НОЛИК" if M[i + 1][i + 1] == "O" else "КРЕСТИК"}')
			return True
	if "-" not in L[0] and "-" not in L[1] and "-" not in L[2]:
		print("Ничья")
		return True

while True:
	fun_krest(input_a)
	p = proverka()
	if p:
		break
	fun_nolik(input_b)
	p = proverka()
	if p:
		break



