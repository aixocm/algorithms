def karatsuba(num1,num2):
    if num1 <10 or  num2 < 10:
            return  num1*num2

	        size1 = len(str(num1))
		    size2 = len(str(num2))

		        half = int(max(size1,size2) / 2)

			    a = int(str(num1)[0:half])
			        b = int(str(num1)[size1-half:])
				    c = int(str(num2)[0:half])
				        d = int(str(num2)[size2-half:])

					    z2 = karatsuba(a,c)
					        z0 = karatsuba(b,d)
						    z1 = karatsuba(a+b,c+d) - z0 - z2

						        return  z2*pow(10,2*half) + z1*pow(10,half) + z0


							print(karatsuba(1000,1000))

