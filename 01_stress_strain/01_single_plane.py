import math

sigma_x = 40.0  # MPa
sigma_y = 80.0  # MPa
tau_xy = 10.0  # MPa
theta_deg = 30.0  # degrees

theta = math.radians(theta_deg)

sigma_n = (
    ((sigma_x + sigma_y) / 2)
    + ((sigma_x - sigma_y) / 2) * math.cos(2 * theta)
    + tau_xy * math.sin(2 * theta)
)

tau_n = -((sigma_x - sigma_y) / 2) * math.sin(2 * theta) + tau_xy * math.cos(2 * theta)

print(f"Normal stress = {sigma_n:.2f} MPa")
print(f"Shear stress  = {tau_n:.2f} MPa")
