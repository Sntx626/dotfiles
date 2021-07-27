import time
import os

cmd = input("Please enter the command you want to benchmark: ")
start = time.time()
os.system(cmd)
stop = time.time()
print("Execution Time:", str(stop-start))