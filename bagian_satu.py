
print('Gaji dalam waktu sehari')
n = int(input('Masukan Jumlah Karyawan yang ingin dihitung gajinya: '))
print()
for i in range (1,n+1) :
	nama = str(input('Masukan Nama :'))
	jam = int(input('Masukan Jumlah Jam :'))
	
	#jika jam kerja lebih dari 24 jam maka akan masuk kedalam jam lembur
	if jam >= 24 :
		lembur = jam - 24
		upah = 24 * 20000 + lembur * 25000
	else :
		upah = jam*20000
	print (upah)