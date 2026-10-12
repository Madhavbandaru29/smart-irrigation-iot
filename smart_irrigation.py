
# Smart Irrigation System - Python Simulation

def check_soil_moisture(moisture):
    print(f"Soil moisture: {moisture}%")

    if moisture < 30:
        print("Soil is dry. Irrigation is ON.")
    else:
        print("Soil moisture is sufficient. Irrigation is OFF.")


# Example sensor readings (simulated)
check_soil_moisture(20)
check_soil_moisture(45)
