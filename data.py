#!/usr/bin/python3
import random

letters = ["-", "_", "a", "!", "$", "C", "D", "*", "#", "b", "%", "&", "c", "Z", "/", "(", "d", "A", ")", "=", "B", "e", "?", "¿", "f", "X", "^", "{", "}", "Y", "g", "I", "J", ":", ";", "h", "G", "H", "<", ">", "i", "j", "3", "K", "+", "-", "L", "5", "k", "l", "4", "1", "m", "@", "7", "0" "O", "P", "2", "n", "9", "|", "M", "8", "N", "o", "7", "p", "q", "r", "s", "6", "Q", "R", "5", "t", "u", "1" "S", "4", "T", "v", "w", "6", "V", "3", "W", "E", "2", "F", "x", "y", "z", "1", "[", "]"]


def generador_1():
	gen1 = random.randint(0, 94)
	gen2 = random.randint(0, 94)
	gen3 = random.randint(0, 94)
	gen4 = random.randint(0, 94)
	gen5 = random.randint(0, 94)
	gen6 = random.randint(0, 94)
	gen7 = random.randint(0, 94)
	gen8 = random.randint(0, 94)
	gen9 = random.randint(0, 94)
	gen10 = random.randint(0, 94)
	gen11 = random.randint(0, 94)
	gen12 = random.randint(0, 94)

	r1 = letters[gen1]
	r2 = letters[gen2]
	r3 = letters[gen3]
	r4 = letters[gen4]
	r5 = letters[gen5]
	r6 = letters[gen6]
	r7 = letters[gen7]
	r8 = letters[gen8]
	r9 = letters[gen9]
	r10 = letters[gen10]
	r11 = letters[gen11]
	r12 = letters[gen12]
	out = "La contraseña generada es: {}{}{}{}{}{}{}{}{}{}{}{}".format(r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12)
	print(out)


def generador_2():
	gen1 = random.randint(0, 94)
	gen2 = random.randint(0, 94)
	gen3 = random.randint(0, 94)
	gen4 = random.randint(0, 94)
	gen5 = random.randint(0, 94)
	gen6 = random.randint(0, 94)
	gen7 = random.randint(0, 94)
	gen8 = random.randint(0, 94)
	gen9 = random.randint(0, 94)
	gen10 = random.randint(0, 94)
	gen11 = random.randint(0, 94)
	gen12 = random.randint(0, 94)
	gen13 = random.randint(0, 94)
	gen14 = random.randint(0, 94)
	gen15 = random.randint(0, 94)
	gen16 = random.randint(0, 94)

	r1 = letters[gen1]
	r2 = letters[gen2]
	r3 = letters[gen3]
	r4 = letters[gen4]
	r5 = letters[gen5]
	r6 = letters[gen6]
	r7 = letters[gen7]
	r8 = letters[gen8]
	r9 = letters[gen9]
	r10 = letters[gen10]
	r11 = letters[gen11]
	r12 = letters[gen12]
	r13 = letters[gen13]
	r14 = letters[gen14]
	r15 = letters[gen15]
	r16 = letters[gen16]
	out = "La contraseña generada es: {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16)
	print(out)