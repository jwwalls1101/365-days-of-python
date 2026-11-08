flight_data = [
    {"time": 0, "altitude": 0, "velocity": 0},
    {"time": 5, "altitude": 80, "velocity": 30},
    {"time": 10, "altitude": 240, "velocity": 55},
    {"time": 10, "altitude": 265, "velocity": 58},
    {"time": 15, "altitude": "450", "velocity": 72},
    {"time": 20, "altitude": 700, "velocity": -90},
    {"time": 25, "altitude": 920, "velocity": 105},
    {"time": 30, "altitude": 1100},
    {"time": 35, "altitude": 1200, "velocity": 115}
]

def validate_flight_data(data):
        previous_time = None
        valid_data = []
        invalid_data = []

        for measurement in data:
            
            if "velocity" in measurement:
                  velocity = measurement["velocity"]
            
            else:
                  invalid_entry = {
                       "measurement": measurement,
                       "reason": "Missing velocity"
                  }
                  
                  invalid_data.append(invalid_entry)
                  continue
            
            if "time" in measurement:
                  time = measurement["time"]
                  
            else:
                  invalid_entry = {
                        "measurement": measurement,
                        "reason": "Missing time"
                    }
                  
                  invalid_data.append(invalid_entry)  
                  continue
            
            if "altitude" in measurement:
                  altitude = measurement["altitude"]
                  
            else:
                  invalid_entry = {
                    "measurement": measurement,
                    "reason": "Missing altitude"
                    }
                  
                  invalid_data.append(invalid_entry)
                  continue

            if not isinstance(velocity, (int, float)) or isinstance(velocity, bool): 
                invalid_entry = {
                    "measurement": measurement,
                    "reason": "Velocity is not a numerical value"
                }
                
                invalid_data.append(invalid_entry)
                continue
            
            if not isinstance(time, (int, float)) or isinstance(time, bool):
                invalid_entry = {
                    "measurement": measurement,
                    "reason": "Time is not a numerical value"
                    }
                
                invalid_data.append(invalid_entry)
                continue
            
            if not isinstance(altitude, (int, float)) or isinstance(altitude, bool):
                invalid_entry = {
                    "measurement": measurement,
                    "reason": "Altitude is not a numerical value"
                    }
                
                invalid_data.append(invalid_entry)
                continue

            if time < 0:
                 invalid_entry = {
                    "measurement": measurement,
                    "reason": "Time is a negative value"
                    }
                 
                 invalid_data.append(invalid_entry)
                 continue 
            
            if altitude < 0:
                 invalid_entry = {
                        "measurement": measurement,
                        "reason": "Altitude is a negative value"
                    }
                 
                 invalid_data.append(invalid_entry)
                 continue
            
            if velocity < 0:
                 invalid_entry = {
                        "measurement": measurement,
                        "reason": "Velocity is a negative value"
                    }
                 
                 invalid_data.append(invalid_entry)
                 continue

            if previous_time is not None:
                 
                 if time <= previous_time:
                      invalid_entry = {
                                "measurement": measurement,
                                "reason": "Time is not chronological"
                        }
                      
                      invalid_data.append(invalid_entry)
                      continue

            previous_time = time
            valid_data.append(measurement)
        
        return valid_data, invalid_data
            
        
            
valid, invalid = validate_flight_data(flight_data)

assert len(valid) == 5
assert len(invalid) == 4

print("Valid Data: ", len(valid))
print("Invalid Data: ", len(invalid))