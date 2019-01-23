import serial

ser = serial.Serial(
	port='COM41',
	baudrate=115200,
)
'''
print("insert op:")
op = input()
ser.write(op.encode())
'''
result = 0.0

while True:
	if ser.readable():
		flag = int(ser.readline()[:-2].decode())
		print('flag=', flag)

		if flag == 1:
			suma = float(ser.readline()[:-2])
			print('arduino sum=',suma)
		else:
			a = float(ser.readline()[:-2])#.decode('utf-8')
			b = float(ser.readline()[:-2])#.decode())
			result += (a+b)
			result = round(result, 3)
			print(result)
			ser.write(str(result).encode())


		#print(res.decode('utf-8'))
		#print(res[:len(res)-1].decode())

	