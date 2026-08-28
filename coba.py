from pymavlink import mavutil
import time 
from pprint import pprint

master = mavutil.mavlink_connection('udpin:0.0.0.0:14552')

master.wait_heartbeat()

while True:
    try:
        msg = master.recv_match()
        if msg is not None:
            pprint(msg.to_dict())
    
    except Exception as e:
        print(f"{e}")

    time.sleep(0.1)
