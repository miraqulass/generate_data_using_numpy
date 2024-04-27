import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)


# Function to generate random dates
def generate_random_dates(start_date, end_date, num_dates):
    return pd.to_datetime(
        np.random.randint(start_date.value, end_date.value, num_dates)
    ).date


# Function to generate and save data to CSV
def generate_and_save_data(filename, data_dict, dates):
    df = pd.DataFrame(data_dict)
    df["date"] = dates
    df.to_csv(filename, index=False)
    print(f"Data saved to '{filename}'")


# Define date range
start_date = pd.Timestamp("2023-01-01")
end_date = pd.Timestamp("2023-12-31")

# Generate synthetic data for engine parameters
engine_data = {
    "engine_rpm": np.random.uniform(600, 6000, 20000),
    "engine_temperature": np.random.uniform(80, 110, 20000),
    "fuel_consumption_rate": np.random.uniform(5, 15, 20000),
    "engine_load": np.random.uniform(20, 80, 20000),
}
engine_dates = generate_random_dates(
    start_date, end_date, len(engine_data["engine_rpm"])
)
generate_and_save_data("engine_data.csv", engine_data, engine_dates)

# Generate synthetic data for transmission parameters
transmission_data = {
    "transmission_fluid_temperature": np.random.uniform(80, 120, 20000),
    "shift_time": np.random.uniform(0.5, 1.5, 20000),
    "transmission_line_pressure": np.random.uniform(50, 250, 20000),
    "gear_position": np.random.randint(4, 11, 20000),
}
transmission_dates = generate_random_dates(
    start_date, end_date, len(transmission_data["transmission_fluid_temperature"])
)
generate_and_save_data("transmission_data.csv", transmission_data, transmission_dates)

# Generate synthetic data for brake parameters
brake_data = {
    "brake_pad_wear": np.random.uniform(0, 12, 20000),
    "brake_fluid_level": np.random.uniform(0, 100, 20000),
    "brake_rotor_wear": np.random.uniform(0, 5, 20000),
}
brake_dates = generate_random_dates(
    start_date, end_date, len(brake_data["brake_pad_wear"])
)
generate_and_save_data("brake_data.csv", brake_data, brake_dates)

# Generate synthetic data for battery parameters
battery_data = {
    "battery_voltage": np.random.uniform(11, 14, 20000),
    "battery_current": np.random.uniform(-100, 100, 20000),
    "state_of_charge": np.random.uniform(0, 100, 20000),
    "battery_temperature": np.random.uniform(0, 50, 20000),
}
battery_dates = generate_random_dates(
    start_date, end_date, len(battery_data["battery_voltage"])
)
generate_and_save_data("battery_data.csv", battery_data, battery_dates)

# Generate synthetic data for fuel system parameters
fuel_system_data = {
    "fuel_pressure": np.random.uniform(200, 500, 20000),
    "fuel_flow_rate": np.random.uniform(5, 50, 20000),
    "fuel_injector_pulse_width": np.random.uniform(1, 5, 20000),
}
fuel_system_dates = generate_random_dates(
    start_date, end_date, len(fuel_system_data["fuel_pressure"])
)
generate_and_save_data("fuel_system_data.csv", fuel_system_data, fuel_system_dates)

# Generate synthetic data for radiator parameters
radiator_data = {
    "coolant_temperature": np.random.uniform(70, 110, 20000),
    "coolant_flow_rate": np.random.uniform(0.5, 2.5, 20000),
    "radiator_pressure": np.random.uniform(10, 20, 20000),
    "fan_speed": np.random.uniform(500, 2500, 20000),
}
radiator_dates = generate_random_dates(
    start_date, end_date, len(radiator_data["coolant_temperature"])
)
generate_and_save_data("radiator_data.csv", radiator_data, radiator_dates)
