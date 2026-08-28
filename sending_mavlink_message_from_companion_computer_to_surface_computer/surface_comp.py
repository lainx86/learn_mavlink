from pymavlink import mavutil
import time 
from pprint import pprint

master = mavutil.mavlink_connection('udpin:0.0.0.0:9000')

master.wait_heartbeat()

print(
    f"Vehicle terdeteksi: "
    f"system={master.target_system}"
    f"component={master.target_component}"
)

while True:
    try:
        msg = master.recv_match()
        if msg is not None:
            pprint(msg.to_dict())
    
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(0.1)
