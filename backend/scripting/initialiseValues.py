import random

    
time_value  =  None  # Random time value between 1 and 60
time_unit   =  random.choice(["seconds",])
# time_unit   =  random.choice(["seconds", "minutes", "hours", "days"]) # time units for longer duration jwt tokens:

if time_unit == "seconds":
    time_value = random.randint(30, 60)
# elif time_unit == "minutes":
#     time_value = random.randint(1, 3)

# ==========================================
# # Below for longer duration jwt tokens:

# elif time_unit == "hours":
#     time_value = random.randint(1, 2)

# elif time_unit == "days":
#     time_value = random.randint(1, 2)

# ==========================================


jwt_time_period = f"{time_value} {time_unit}"
print(f"Generated JWT Time Period: {jwt_time_period}")