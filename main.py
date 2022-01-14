binary = input("Binary : ").split(".")
oct1 = binary[0]
oct2 = binary[1]
oct3 = binary[2]
oct4 = binary[3]

def IpToBi(ip):
	ip = list(map(int,ip))
	bi = [128,64,32,16,8,4,2,1]
	x = 0
	for i in ip:
		if ip[x] == 1:
			ip[x] = bi[x]
		
		x+=1
	return sum(ip)
print(f"{IpToBi(oct1)}.{IpToBi(oct2)}.{IpToBi(oct3)}.{IpToBi(oct4)}")

oct1 = IpToBi(oct1)

if (oct1 >= 1 and oct1 <= 126):
	print("Class : A")
	print("Subset : 255.0.0.0")
elif (oct1 >= 128 and oct1 <= 191):
	print("Class : B")
	print("Subset : 255.255.0.0")
elif (oct1 >= 192 and oct1 <= 223):
	print("Class : C")
	print("Subset : 255.255.255.0")

