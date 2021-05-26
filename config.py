import logging
import sys

# Create basic logger
logger = logging.getLogger('power_monitor')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
logger.addHandler(ch)


# Using a multimeter, measure the voltage of the receptacle where your 9V AC transformer will plug into. Enter the measured value below.
GRID_VOLTAGE = 124.2
# Using a multimeter, measure the output voltage of your AC transformer. Using the value on the label is not ideal and will lead to greater accuracy in the calculations.
AC_TRANSFORMER_OUTPUT_VOLTAGE = 10.2

# InfluxDB Settings
db_settings = {
    'host' : 'localhost',
    'port' : 8086,
    'username' : 'root',
    'password' : 'password',
    'database' : 'power_monitor'
}


# Define Variables
ct0_channel = 0             # Orange Pair           | House main (leg 1 - left)  (orange pair)
ct1_channel = 1             # Green Pair            | House main (leg 2 - right) (green pair)
ct2_channel = 2             # Blue Pair             | Subpanel main (leg 1 - top)
ct3_channel = 3             # Brown Pair            | Solar Power 
ct4_channel = 6             # 3.5mm Input #1        | Subpanel main (leg 2 - bottom)
ct5_channel = 7             # 3.5mm Input #2        | Unused

ct6_channel = 0             # Chip 2
ct7_channel = 1             # Chip 2
ct8_channel = 2             # Chip 2
ct9_channel = 3             # Chip 2
ct10_channel = 4            # Chip 2
ct11_channel = 5            # Chip 2
ct12_channel = 6            # Chip 2
ct13_channel = 7            # Chip 2

board_voltage_channel =  4  # Board voltage ~3.3V
v_sensor_channel = 5        # 9V AC Voltage channel

# The values from running the software in "phase" mode should go below!
ct_phase_correction = {
    'ct0' : 1,
    'ct1' : 1,
    'ct2' : 1,
    'ct3' : 1,
    'ct4' : 1,
    'ct5' : 1,
    
    'ct6' : 1,
    'ct7' : 1,
    'ct8' : 1,
    'ct9' : 1,
    'ct10' : 1,
    'ct11' : 1,
    'ct12' : 1,
    'ct13' : 1,
}

# AFTER phase correction is completed, these values are used in the final calibration for accuracy. See the documentation for more information.
accuracy_calibration = {
    'ct0' : 1,
    'ct1' : 1,
    'ct2' : 1,
    'ct3' : 1,
    'ct4' : 1,
    'ct5' : 1,
    
    'ct6' : 1,
    'ct7' : 1,
    'ct8' : 1,
    'ct9' : 1,
    'ct10' : 1,
    'ct11' : 1,
    'ct12' : 1,
    'ct13' : 1,
    
    'AC'  : 1,
}
