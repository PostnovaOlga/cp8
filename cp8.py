try:
	print("Number_in_decimal_notation,_that is less than 256")
	n = int(input())
	if n >= 0:
		d = n
	else:
		d = -n	
	if d < 256 :
		print("Number_system_(2_or_8):")
		syst = int(input())
		if (syst == 2) or (syst == 8):
			def transform(k,s,f):
				b = ''
				while k > 0:
					b = str(k % s) + b
					k = k // s
				if f>= 0:
					print(b)
				else:
					print("-",b)	
			transform(d,syst,n)	 					
		else :
			print("Incorrect_data")
	else:
		print("Incorrect_data")		
except ValueError :
	print("Incorrect_data")
