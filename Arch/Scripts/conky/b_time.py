import time

print(f"{time.strftime('%H')}:{time.strftime('%M')}:{round(int(time.strftime('%S')) + time.time()-int(time.time()),2)}")
