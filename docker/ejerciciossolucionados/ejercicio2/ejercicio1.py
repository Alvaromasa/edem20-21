import time
from datetime import datetime
ahora = time.strftime("%H:%M:%S")
while True:
   
    print("this prints once a minute")
    print(datetime.now())
    time.sleep(60)