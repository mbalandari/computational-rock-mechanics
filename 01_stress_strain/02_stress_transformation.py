import math

# -------------------------
# 1. Input stress state
# -------------------------

sigma_x = 40.0  # MPa
sigma_y = 80.0  # MPa
tau_xy = 10.0  # MPa


# -------------------------
# 2. Create angle range
# -------------------------

angles = []

for angle in range(0, 181):
    angles.append(angle)


# -------------------------
# 3. Calculate transformed stresses
# -------------------------

normal_stresses = []
shear_stresses = []

for angle_deg in angles:

    theta = math.radians(angle_deg)

    sigma_n = (
        ((sigma_x + sigma_y) / 2)
        + ((sigma_x - sigma_y) / 2) * math.cos(2 * theta)
        + tau_xy * math.sin(2 * theta)
    )

    tau_n = -((sigma_x - sigma_y) / 2) * math.sin(2 * theta) + tau_xy * math.cos(
        2 * theta
    )

    normal_stresses.append(sigma_n)
    shear_stresses.append(tau_n)


# -------------------------
# 4. Display some results
# -------------------------

print("Angle    Normal Stress    Shear Stress")

for i in range(0, 181, 30):
    print(
        f"{angles[i]:5.1f}    "
        f"{normal_stresses[i]:10.2f}    "
        f"{shear_stresses[i]:10.2f}"
    )
