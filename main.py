import numpy as np
import pandas as pd

num_data_points = 10000
time_interval = 1
noise_stddev = 2

time = np.arange(0, num_data_points) * time_interval


def generate_sensor_data(sensor_name):
    if sensor_name == "Temperature":
        base_temperature = 80
        amplitude = 10
        frequency = 0.1
        temperature_data = (
            base_temperature + amplitude + np.sin(frequency*time) + np.random.normal(0, noise_stddev, num_data_points)
        )
        return temperature_data

    elif sensor_name == "Speed":
        min_speed = 20
        max_speed = 70
        speed_data = np.random.uniform(min_speed, max_speed, num_data_points)
        return speed_data

    elif sensor_name == "EngineKnock":
        mean_intensity = 5
        knock_data = np.random.poisson(mean_intensity, num_data_points)
        return knock_data

    elif sensor_name == "CoolantTemperature":
        base_temperature = 80
        amplitude = 10
        frequency = 0.05
        coolant_temp_data = (
            base_temperature + amplitude + np.sin(frequency * time) + np.random.normal(0, noise_stddev, num_data_points)
        )
        return coolant_temp_data

    elif sensor_name == "ThrottlePosition":
        min_position = 0
        max_position = 100
        throttle_position_data = np.random.uniform(min_position, max_position, num_data_points)
        return throttle_position_data

    elif sensor_name =="MAPSensor":
        min_pressure = 80
        max_pressure = 120
        map_data = np.random.uniform(min_pressure, max_pressure, num_data_points)
        return map_data

    elif sensor_name == "OxygenSensor":
        base_oxygen_level = 0.2
        oxygen_data = base_oxygen_level + np.random.normal(0, noise_stddev, num_data_points)
        return oxygen_data

    elif sensor_name == "RainSensor":
        rain_intensity = np.random.uniform(0, 1, num_data_points)
        rain_data = rain_intensity +np.random.normal(0, noise_stddev, num_data_points)
        return rain_data

    elif sensor_name == "VoltageSensor":
        base_voltage = 12.0
        voltage_data = base_voltage + np.random.normal(0, noise_stddev, num_data_points)
        return voltage_data

    elif sensor_name == "CamshaftPosition":
        angular_velocity = 1
        initial_position = 0

        camshaft_position_data = (
            initial_position + angular_velocity * time + np.random.normal(0, noise_stddev, num_data_points)
        )
        camshaft_position_data = camshaft_position_data % 360
        return camshaft_position_data


temperature_data = generate_sensor_data("Temperature")
speed_data = generate_sensor_data("Speed")
knock_data = generate_sensor_data("EngineKnock")
coolant_temp_data = generate_sensor_data("CoolantTemperature")
throttle_position_data = generate_sensor_data("ThrottlePosition")
map_data = generate_sensor_data("MAPSensor")
oxygen_data = generate_sensor_data("OxygenSensor")
rain_data = generate_sensor_data("RainSensor")
voltage_data = generate_sensor_data("VoltageSensor")
camshaft_position_data = generate_sensor_data("CamshaftPosition")

data = pd.DataFrame({
    "Time": time,
    "Temperature": temperature_data,
    "Speed": speed_data,
    "EngineKnock": knock_data,
    "CoolantTemp": coolant_temp_data,
    "ThrottlePosition": throttle_position_data,
    "MAPSensor": map_data,
    "OxygenSensor": oxygen_data,
    "RainSensor": rain_data,
    "VoltageSensor": voltage_data,
    "CamshaftPosition": camshaft_position_data,
})

data.to_csv("sensor_data.csv", index=False)

print(data)

# print("Temperature Data:", temperature_data)
# print("Speed Data:", speed_data)
# print("Engine Knock Data:", knock_data)
# print("Voltage Data:", voltage_data)


