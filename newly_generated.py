import numpy as np
import pandas as pd


def generate_engine_data(num_samples, climate_condition, road_condition):
    eng_rpm = (
        np.random.uniform(600, 6000, num_samples) + (climate_condition == "Hot") * 500
    )
    eng_temp = np.random.normal(90, 10, num_samples) * (climate_condition == "Hot") * 10
    fuel_cons_rate = (
        np.random.uniform(5, 15, num_samples) + (road_condition == "Rough") * 2
    )
    eng_load = np.random.uniform(0, 100, num_samples)
    return eng_rpm, eng_temp, eng_load, fuel_cons_rate


def generate_transmission_data(num_samples, climate_condition):
    trans_fluid_temp = (
        np.random.normal(80, 20, num_samples) + (climate_condition == "Hot") * 10
    )
    shift_time = np.random.uniform(0.1, 2, num_samples)
    trans_line_pressure = np.random.normal(150, 20, num_samples)
    return trans_fluid_temp, shift_time, trans_line_pressure


def generate_brakes_data(num_samples, road_condition):
    brake_pad_wear = (
        np.random.uniform(0, 100, num_samples) + (road_condition == "Rough") * 10
    )
    brake_rotor_wear = (
        np.random.uniform(0, 100, num_samples) + (road_condition == "Rough") * 10
    )
    brake_fluid_level = np.random.normal(100, 5, num_samples)
    return brake_pad_wear, brake_rotor_wear, brake_fluid_level


def generate_battery_data(num_samples):
    battery_voltage = np.random.normal(12, 0.5, num_samples)
    state_of_charge = np.random.uniform(0, 100, num_samples)
    battery_current = np.random.normal(0, 5, num_samples)
    return battery_voltage, state_of_charge, battery_current


def generate_radiator_data(num_samples, climate_condition):
    coolant_temp = (
        np.random.normal(90, 10, num_samples) + (climate_condition == "Hot") * 10
    )
    coolant_flow_rate = np.random.normal(5, 1, num_samples)
    radiator_pressure = np.random.normal(15, 2, num_samples)
    return coolant_temp, coolant_flow_rate, radiator_pressure


def generate_fuel_system_data(num_samples):
    fuel_pressure = np.random.normal(75, 5, num_samples)
    fuel_flow_rate = np.random.normal(10, 2, num_samples)
    fuel_injector_pulse_width = np.random.normal(3, 0.5, num_samples)
    return fuel_pressure, fuel_flow_rate, fuel_injector_pulse_width


def generate_maintenance_logs(num_samples):
    maintenance_interval_km = 10000
    maintenance_types = np.random.choice(
        ["Inspection", "Replacement", "Repair"], num_samples
    )
    scheduled_maintenance_interval_km = np.random.normal(
        maintenance_interval_km, 1000, num_samples
    )
    return maintenance_types, scheduled_maintenance_interval_km


def newly_generated_data(num_samples):
    climate_conditions = ["Hot", "Moderate", "Cold"]
    road_conditions = ["Paved", "Rough"]
    driving_conditions = ["Urban", "Highway"]

    new_data = []

    while len(new_data) < num_samples:
        climate_condition = np.random.choice(climate_conditions)
        road_condition = np.random.choice(road_conditions)
        driving_condition = np.random.choice(driving_conditions)

        engine_data = generate_engine_data(1, climate_condition, road_condition)
        transmission_data = generate_transmission_data(1, climate_condition)
        brakes_data = generate_brakes_data(1, road_condition)
        battery_data = generate_battery_data(1)
        radiator_data = generate_radiator_data(1, climate_condition)
        fuel_system_data = generate_fuel_system_data(1)

        maintenance_logs = generate_maintenance_logs(1)

        components_data = pd.DataFrame(
            {
                "Climate_condition": climate_condition,
                "Road_Condition": road_condition,
                "Driving_Condition": driving_condition,
                "Engine_RPM": engine_data[0],
                "Engine_Temperature": engine_data[1],
                "Fuel_Consumption_Rate": engine_data[2],
                "Engine_Load": engine_data[3],
                "Transmission_Fluid_Temperature": transmission_data[0],
                "Shift_Time": transmission_data[1],
                "Transmission_Line_Pressure": transmission_data[2],
                "Brake_Pad_Wear": brakes_data[0],
                "Brake_Rotor_Wear": brakes_data[1],
                "Brake_Fluid_Level": brakes_data[2],
                "Battery_Voltage": battery_data[0],
                "State_of_Charge": battery_data[1],
                "Battery_Current": battery_data[2],
                "Coolant_Temperature": radiator_data[0],
                "Coolant_Flow_Rate": radiator_data[1],
                "Radiator_Pressure": radiator_data[2],
                "Fuel_Pressure": fuel_system_data[0],
                "Fuel_Flow_Rate": fuel_system_data[1],
                "Fuel_Injector_Pulse_Width": fuel_system_data[2],
                "Maintenance_Type": maintenance_logs[0],
                "Scheduled_Maintenance_Interval_km": maintenance_logs[1],
            }
        )

        new_data.append(components_data)

    return pd.concat(new_data, ignore_index=True)[:num_samples]


if __name__ == "__main__":
    num_samples = 10000
    new_data = newly_generated_data(num_samples)
    new_data.to_csv("new_data.csv", index=False)
    print(new_data.head())
