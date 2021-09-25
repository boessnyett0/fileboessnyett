
print("***OPERASIKALKULATOR***".center(34))
print("===By Aldi Dzhq===".center(32))
print("**!masukan di bawah ini!**".center(33))
print("!1!1!1!1!1!1!\n\n".center(33))
while True:
	p=input("Password:")
	if p=="mubah":
		print("Password Succes!!")
	else:
		print("Password Failed!!")
		break
		
	k=input("\n\nMasukan + - x : Pilih Salah Satu:")
	if k not in("+","-","x",":"):
		print("Tidak Ada Di Kalkulator!")
		break
	g=int(input("Masukan Angka Pertama:"))
	p=int(input("Masukan Angka Kedua:"))
	 
	if k=="+":
	 	print("Hasil Dari",g,"+",p,"=",g+p)
	 	print("^ ^ ^ ^ ^ ^ ^ ^ ")
	 	print("| | | | | | | |")
	 	print("SEMOGA TERBANTU")
	 	print("KALKULATOR buatan -----> ALDIDZHQ\n\n")
	elif k=="-":
		print("Hasil Dari",g,"-",p,"=",g-p)
		print("^ ^ ^ ^ ^ ^ ^ ^ ")
		print("| | | | | | | |")
		print("SEMOGA TERBANTU")
		print("KALKULATOR buatan -----> ALDIDZHQ\n\n")
	elif k=="x":
 		print("Hasil Dari",g,"x",p,"=",g*p)
	 	print("^ ^ ^ ^ ^ ^ ^ ^ ")
	 	print("| | | | | | | |")
	 	print("SEMOGA TERBANTU")
	 	print("KALKULATOR buatan -----> ALDIDZHQ\n\n")
	elif k==":":
 		print("Hasil Dari",g,":",p,"=",g/p)
	 	print("^ ^ ^ ^ ^ ^ ^ ^ ")
	 	print("| | | | | | | |")
	 	print("SEMOGA TERBANTU")
	 	print("KALKULATOR buatan -----> ALDIDZHQ\n\n")

		