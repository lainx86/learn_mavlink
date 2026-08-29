from pymavlink import mavutil
from pprint import pprint
import time 

master = mavutil.mavlink_connection('udpin:0.0.0.0:9000')

master.wait_heartbeat()

print(f"Perangkat Terhubung: "
      f"System={master.target_system}"
      f"Component={master.target_component}")

while True:
    try:
        msg = master.recv_match()

        if msg is not None:
            pprint(msg.to_dict())

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(0.1)
