#!/usr/bin/env python3
import sys
import os
import serial

def main():
		pidfile="run.pid"
		ttyport = "/dev/ttyS0"
		with open(pidfile, "w") as w:
				print(str(os.getpid()),file=w)
		ser = serial.Serial()
		ser.baudrate = 19200
		ser.port = ttyport
		ser.timeout=1
		try:
				ser.open()
		except Exception as e:
				print(e)
				sys.exit()
		print("Writing to port.")
		ser.write(b"test_mode=1\r\n")
		print("Done.")
		while os.path.exists(pidfile) and ser.is_open:
				try:
						# txt=ser.readline()
						txt=ser.read(20)
						if txt:
								print(txt.strip())
				except Exception:
						print(e)
						os.unlink(pidfile)

				
				

if __name__ == "__main__":
		main()  
