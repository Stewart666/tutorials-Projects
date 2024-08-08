import time

#geting the current 
display_time = time.strftime("%H: %M: %S")
current_time = int(time.strftime("%H")) 

#identifing if is morning, afternoon, enin or night and Greating acording to cerrent time
if current_time > 3:
    current_time = "morning"
    print(f"Good morning Mr/Ms! and the time is ({display_time})")

elif current_time > 11:
    current_time = "afternoon"
    print(f"Good afternoon Mr/Ms! and the time is ({display_time})")

elif current_time > 15:
    current_time = "evining"
    print(f"Good evining Mr/Ms! and the time is ({display_time})")

else:
    current_time = "night"
    print(f"Have a good night Mr/Ms! and the time is ({display_time})")

