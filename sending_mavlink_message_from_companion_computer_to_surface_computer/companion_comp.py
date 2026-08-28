import time 
from pymavlink import mavutil
from pprint import pprint

pixhawk = mavutil.mavlink_connection('udpin:0.0.0.0:14550')

companion_to_surface = mavutil.mavlink_connection('udpout:127.0.0.1:9000')

pixhawk.wait_heartbeat()

print(
    f"Pixhawk terhubung: "
    f"system={pixhawk.target_system}, "
    f"component={pixhawk.target_component}"
)

while True:
    try:
        msg = pixhawk.recv_match()

        if msg is not None:
            packet = msg.get_msgbuf()

            companion_to_surface.write(packet)

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(0.1)
