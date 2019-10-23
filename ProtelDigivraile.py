import string

def insert_angka(h, word):
	if h != 1:
		kata = word[:h]+'#'+word[h:]
		return kata
	else:
		kata = '#' + word[h:]
		return kata

def insert_hurufBesar(h, word):
	if h != 1:
		kata = word[:h]+'~'+word[h:]
		return kata
	else:
		kata = '~' + word[h:]
		return kata

def kembali_huruf(h, word):
	kata = word[:h]+';'+word[h:]
	return kata

def huruf_besar_semua(word):
	if len(word) == 2:
		kata = '~' + word
		return kata
	else:
		kata = '~~' + word
		return kata

def konversi(huruf):
	if huruf == 'a' or huruf == '2':
		return '100001'
	elif huruf == 'b' or huruf == '3':
		return '110001'
	elif huruf == 'c' or huruf == '4':
		return '100101'
	elif huruf == 'd' or huruf == '5':
		return '100111'
	elif huruf == 'e' or huruf == '6':
		return '100011'
	elif huruf == 'f' or huruf == '7':
		return '110101'
	elif huruf == 'g' or huruf == '8':
		return '110111'
	elif huruf == 'h' or huruf == '9':
		return '110011'
	elif huruf == 'i' or huruf == '10':
		return '010101'
	elif huruf == 'j' or huruf == '1':
		return '010111'
	elif huruf == 'k':
		return '101001'
	elif huruf == 'l':
		return '100101'
	elif huruf == 'm':
		return '101101'
	elif huruf == 'n':
		return '101111'
	elif huruf == 'o':
		return '101011'
	elif huruf == 'p':
		return '111101'
	elif huruf == 'q':
		return '111111'
	elif huruf == 'r':
		return '111011'
	elif huruf == 's':
		return '011011'
	elif huruf == 't':
		return '011111'
	elif huruf == 'u':
		return '101002'
	elif huruf == 'v':
		return '111002'
	elif huruf == 'w':
		return '010112'
	elif huruf == 'x':
		return '101102'
	elif huruf == 'y':
		return '101112'
	elif huruf == 'z':
		return '101012'
	elif huruf == '#':
		return '001112'
	elif huruf == '-':
		return '001002'
	elif huruf == '.':
		return '010012'
	elif huruf == '~':
		return '000002'
	elif huruf == ';':
		return '011001'
	elif huruf == ',':
		return '010001'


input_now = input("Masukkan kata: ")
if input_now.isupper():
	input_now = huruf_besar_semua(input_now)

h = 1
status = 1

while(h<len(input_now)):
	if input_now[h].isdigit():
		if status == 2 :
			h=h+2
		else:
			input_now = insert_angka(h,input_now)
			h=h+3
			status = 2
	elif input_now[h] in string.punctuation:
		h=h+2
	else:
		if status == 2 :
			if input_now[h].isupper():
				input_now = kembali_huruf(h,input_now)
				input_now = insert_hurufBesar(h+2, input_now)
				h=h+4
				status = 1
			else:
				input_now = kembali_huruf(h,input_now)
				h=h+3
				status = 1
		else:
			if input_now[h].isupper():
				input_now = insert_hurufBesar(h, input_now)
				h=h+2
			else:
				h=h+1

input_now = input_now.lower()

if len(input_now)<=4:
	for h in range(len(input_now)):
		braille = konversi(input_now[h])
		b1 = int(braille[0])
		b2 = int(braille[1])
		b3 = int(braille[2])
		b4 = int(braille[3])
		b5 = int(braille[4])
		b6 = int(braille[5])
		print (b1, b2, b3, b4, b5, b6)
else:
	#potong_kata = int(len(input_now)/4)+1
	if len(input_now)>= 5 and len(input_now)<=8:
		input_now_1 = input_now[0:4]
		for h in range(len(input_now_1)):
			braille = konversi(input_now_1[h])
			b1 = int(braille[0])
			b2 = int(braille[1])
			b3 = int(braille[2])
			b4 = int(braille[3])
			b5 = int(braille[4])
			b6 = int(braille[5])
			print (b1, b2, b3, b4, b5, b6)
		input_now_2 = input_now[4::]
		for h in range(len(input_now_2)):
			braille = konversi(input_now_2[h])
			b1 = int(braille[0])
			b2 = int(braille[1])
			b3 = int(braille[2])
			b4 = int(braille[3])
			b5 = int(braille[4])
			b6 = int(braille[5])
			print (b1, b2, b3, b4, b5, b6)
	elif len(input_now)>=9 and len(input_now)<=12:
		input_now_1 = input_now[0:4]
		for h in range(len(input_now_1)):
			braille = konversi(input_now_1[h])
			b1 = int(braille[0])
			b2 = int(braille[1])
			b3 = int(braille[2])
			b4 = int(braille[3])
			b5 = int(braille[4])
			b6 = int(braille[5])
			print (b1, b2, b3, b4, b5, b6)
		input_now_2 = input_now[4:8]
		for h in range(len(input_now_2)):
			braille = konversi(input_now_2[h])
			b1 = int(braille[0])
			b2 = int(braille[1])
			b3 = int(braille[2])
			b4 = int(braille[3])
			b5 = int(braille[4])
			b6 = int(braille[5])
			print (b1, b2, b3, b4, b5, b6)
		input_now_3 = input_now[8::]
		for h in range(len(input_now_3)):
			braille = konversi(input_now_3[h])
			b1 = int(braille[0])
			b2 = int(braille[1])
			b3 = int(braille[2])
			b4 = int(braille[3])
			b5 = int(braille[4])
			b6 = int(braille[5])
			print (b1, b2, b3, b4, b5, b6)
	else: #maksimal 16 karakter
		input_now_1 = input_now[0:4]
		for h in range(len(input_now_1)):
			braille = konversi(input_now_1[h])
			b1 = int(braille[0])
			b2 = int(braille[1])
			b3 = int(braille[2])
			b4 = int(braille[3])
			b5 = int(braille[4])
			b6 = int(braille[5])
			print (b1, b2, b3, b4, b5, b6)
		input_now_2 = input_now[4:8]
		for h in range(len(input_now_2)):
			braille = konversi(input_now_2[h])
			b1 = int(braille[0])
			b2 = int(braille[1])
			b3 = int(braille[2])
			b4 = int(braille[3])
			b5 = int(braille[4])
			b6 = int(braille[5])
			print (b1, b2, b3, b4, b5, b6)
		input_now_3 = input_now[8:12]
		for h in range(len(input_now_3)):
			braille = konversi(input_now_3[h])
			b1 = int(braille[0])
			b2 = int(braille[1])
			b3 = int(braille[2])
			b4 = int(braille[3])
			b5 = int(braille[4])
			b6 = int(braille[5])
			print (b1, b2, b3, b4, b5, b6)
		input_now_4 = input_now[12::]
		for h in range(len(input_now_4)):
			braille = konversi(input_now_4[h])
			b1 = int(braille[0])
			b2 = int(braille[1])
			b3 = int(braille[2])
			b4 = int(braille[3])
			b5 = int(braille[4])
			b6 = int(braille[5])
			print (b1, b2, b3, b4, b5, b6)