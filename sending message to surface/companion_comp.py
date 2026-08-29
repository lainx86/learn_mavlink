from pymavlink import mavutil
import time 
from pprint import pprint

pixhawk_to_companion = mavutil.mavlink_connection('udpin:0.0.0.0:14550')

companion_to_surface = mavutil.mavlink_connection('udpout:127.0.0.1:9000')

pixhawk_to_companion.wait_heartbeat()

print(f"Pixhawk Terhubung: "
      f"System={pixhawk_to_companion.target_system} "
      f"Component={pixhawk_to_companion.target_component} ")

while True:
      try:
            companion_to_surface.mav.statustext_send(mavutil.mavlink.MAV_SEVERITY_NOTICE,
                                                           "Surface Computer will read this".encode())
      except Exception as e:

            print(f"Error: {e}")

      time.sleep(0.1)

