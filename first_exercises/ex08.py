# Measurement Converter
meter_measurement = float(input('Enter the measurement in meters: '))
measurement_cm = meter_measurement * 100
measurement_mm = meter_measurement * 1000
print('The measurement of {:.2f} meters in centimeters is: {:.2f} and in millimeters is: {:.2f}'.format(meter_measurement, measurement_cm, measurement_mm))
