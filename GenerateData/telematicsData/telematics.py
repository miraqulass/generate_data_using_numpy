import numpy as np
import pandas as pd
import geopy.distance

num_data_points = 10000
time_interval = 1
noise_stddev = 2


def generate_fixed_waypoints():
    waypoints = [
        (-1.286389, 36.817223),  # Nairobi
        (-1.2921, 36.8219),  # Kenya Center
        (-0.303099, 36.080025),  # Nakuru
        (-0.102210, 34.761710),   # kisumu
        (-4.043740, 39.658871),  # Mombasa
        (0.5167, 35.2833),  # Uasin Gishu
        (0.282731, 34.751863),  # Kakamega
        (-0.677334, 34.779603),  # Kisii
    ]

    return waypoints


route_waypoints = generate_fixed_waypoints()


def generate_telematics_data(route_waypoints):
    current_waypoint = 0
    current_latitude, current_longitude = route_waypoints[current_waypoint]
    initial_speed = 5
    acceleration_mean = 0.2
    max_speed = 100

    gps_data = [(current_latitude, current_longitude)]
    speed_data = [initial_speed]
    acceleration_data = [0]

    for i in range(1, num_data_points):
        distance_to_waypoint = geopy.distance.distance(
            (current_latitude, current_longitude), route_waypoints[current_waypoint]
        ).meters

        if distance_to_waypoint > 5:
            acceleration_data.append(np.random.normal(acceleration_mean, noise_stddev))
            speed_data.append(np.clip(speed_data[i - 1] + acceleration_data[i] * time_interval, 0, max_speed))
        else:
            acceleration_data.append(-speed_data[i - 1] / time_interval if i > 0 else 0)
            speed_data.append(0)

        bearing = np.arctan2(route_waypoints[current_waypoint][1] - current_longitude, route_waypoints[current_waypoint][0] - current_latitude)
        current_latitude += speed_data[i] * time_interval * np.cos(bearing) + np.random.normal(0, noise_stddev)
        current_longitude += speed_data[i] * time_interval * np.sin(bearing) + np.random.normal(0, noise_stddev)

        current_latitude = np.clip(current_latitude, -90, 90)

        rounded_latitude = round(current_latitude, 6)
        rounded_longitude = round(current_longitude, 6)

        if distance_to_waypoint <= 5:
            current_waypoint = (current_waypoint + 1) % len(route_waypoints)

        gps_data.append((rounded_latitude, rounded_longitude))

    return gps_data, speed_data, acceleration_data


gps, speed, acceleration = generate_telematics_data(route_waypoints)

telematics_data = pd.DataFrame({
    "Time": np.arange(0, num_data_points) * time_interval,
    "GPS": gps,
    "Speed(km/hr)": speed,
    "Acceleration": acceleration,
})

telematics_data.to_csv("telematics_data_random_route.csv", index=False)


print(telematics_data)