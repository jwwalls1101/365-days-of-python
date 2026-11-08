## Day 4 - Engineering Data Validator

# Objective
Develop a program that examines aircraft flight measurements, identifies invalid data, and separates valid measurements from corrupted ones. 

# Method
The program examines a dataset containing an aircraft's time, altitude, and velocity measurements. Each measurement must pass four validation requirements:

Required Keys: Every measurement must contain time, altitude, and velocity.
Data Types: All values must be integers or floats, excluding boolean values
Physical constraints: Time, altitude, and velocity must all be positive values
Chronological Order: Each time must be greater than the previously accepted time

Measurements that fail these validations are rejected, and the reason for rejection is recorded.

# Implementation
The program uses a reusable `validate_flight_data()` function that accepts a list of dictionaries.
Each measurement is evaluated using conditional statements and the `isinstance()` function. The `continue` statement is used to skip measurements that fail validation, acting as a filter to catch any invalid data before it goes through the remaining checks.
Valid measurements are stored in `valid_data` while rejected measurements and their error messages are stored in `invalid_data`.

# Results
The simulated flight dataset produced the following results:

- Total Measurements: 9
- Valid Measurements: 5
- Invalid Measurements: 4

The program successfully identified measurements with missing dictionary keys, incorrect data types, negative values, and duplicate or incorrect times.

# Takeaway
This project demonstrated the importance of validating engineering data before performing calculations.

I utilized dictionary operations, condiditonal statments, data type checking, and error handling while developing a reusable validation function.

