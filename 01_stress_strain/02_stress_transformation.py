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


max_normal_stress = max(normal_stresses)
angle_max_normal_stress = normal_stresses.index(max_normal_stress)
print(
    f"Maximum normal stress is {max_normal_stress:.2f} at angle of {angle_max_normal_stress}"
)

min_normal_stress = min(normal_stresses)
angle_min_normal_stress = normal_stresses.index(min_normal_stress)
print(
    f"Minimum normal stress is {min_normal_stress:.2f} at angle of {angle_min_normal_stress}"
)

max_absolute_shear_stress = max(shear_stresses)
angle_max_absolute_shear_stress = shear_stresses.index(max_absolute_shear_stress)
print(
    f"Maximum absolute shear stress is {max_absolute_shear_stress:.2f} at angle of {angle_max_absolute_shear_stress}"
)
