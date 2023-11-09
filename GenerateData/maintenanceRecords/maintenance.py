import pandas as pd
import numpy as np
from datetime import datetime, timedelta

num_vehicles = 10000


def generate_maintenance_records(num_records_per_vehicle=5):

    maintenance_records = []

    for vehicle_id in range(1, num_vehicles + 1):
        current_mileage = 0
        for _ in range(num_records_per_vehicle):
            maintenance_type = np.random.choice(['Oil Change', 'Brake Replacement', 'Tire Rotation', 'Air Filter Replacement'])
            if maintenance_type in ['Oil Change', 'Tire Rotation']:
                maintenance_category = 'Routine Maintenance'
                maintenance_frequency = 'Every 3 months'
                maintenance_severity = 'Moderate'
            elif maintenance_type == 'Brake Replacement':
                maintenance_category = 'Repairs'
                maintenance_frequency = 'As needed'
                maintenance_severity = 'High'
            else:
                maintenance_category = 'Schedules'
                maintenance_frequency = 'Every 6 months'
                maintenance_severity = 'Low'

            maintenance_date = datetime.now() - timedelta(days=np.random.randint(1, 365))

            maintenance_cost = np.round(np.random.uniform(5000, 60000), 2)

            maintenance_interval = np.random.randint(1, 365)

            current_mileage += np.random.randint(5000, 100000)

            record = {
                'VehicleID': vehicle_id,
                'MaintenanceType': maintenance_type,
                'MaintenanceCategory': maintenance_category,
                'MaintenanceFrequency': maintenance_frequency,
                'MaintenanceSeverity': maintenance_severity,
                'MaintenanceDate': maintenance_date.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
                'MaintenanceCost(Ksh)': maintenance_cost,
                'MaintenanceInterval': f"{maintenance_interval} days",
                'EventMileage': current_mileage,
            }

            maintenance_records.append(record)

    return pd.DataFrame(maintenance_records)


maintenance_data = generate_maintenance_records(num_records_per_vehicle=5)

maintenance_data.to_csv('maintenance_data.csv', index=False)

print(maintenance_data)
