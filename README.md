Robotic Arm Package Sorter
This Python project implements a function for a robotic arm in an automation factory. The function, sort(), determines the correct stack for a package based on its volume and mass.

🎯 Objective
The primary goal is to dispatch packages to the correct stack according to their dimensions (width, height, length in centimeters) and mass (in kilograms).

📜 Sorting Rules
The sort() function categorizes packages based on the following criteria:

Bulky Package:

Its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³.

OR, any one of its dimensions (width, height, or length) is greater than or equal to 150 cm.

Heavy Package:

Its mass is greater than or equal to 20 kg.

Based on these, packages are dispatched to one of three stacks:

STANDARD: Packages that are neither bulky nor heavy.

SPECIAL: Packages that are either bulky or heavy (but not both).

REJECTED: Packages that are both bulky and heavy.

⚙️ Implementation
The core logic is encapsulated in the sort(width, height, length, mass) function.

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sorts packages based on their dimensions and mass.

    📦 Rules:
    - A package is **bulky** if its volume (Width x Height x Length) is >= 1,000,000 cm³
      or if any of its dimensions (width, height, length) is >= 150 cm.
    - A package is **heavy** if its mass is >= 20 kg.

    🏷️ Stacks:
    - **REJECTED**: If the package is both heavy AND bulky.
    - **SPECIAL**: If the package is EITHER heavy OR bulky (but not both, as that's REJECTED).
    - **STANDARD**: If the package is NEITHER heavy NOR bulky.

    Args:
        width (float): Width of the package in cm.
        height (float): Height of the package in cm.
        length (float): Length of the package in cm.
        mass (float): Mass of the package in kg.

    Returns:
        str: The name of the stack ("STANDARD", "SPECIAL", or "REJECTED") where the package should go.
    """
    # Define the thresholds for clarity
    VOLUME_THRESHOLD_CM3 = 1_000_000  # cm³
    DIMENSION_THRESHOLD_CM = 150      # cm
    MASS_THRESHOLD_KG = 20            # kg

    # Calculate the volume of the package
    volume = width * height * length

    # Determine if the package is bulky
    is_bulky = True if (volume >= VOLUME_THRESHOLD_CM3 or
                        width >= DIMENSION_THRESHOLD_CM or
                        height >= DIMENSION_THRESHOLD_CM or
                        length >= DIMENSION_THRESHOLD_CM) else False

    # Determine if the package is heavy
    is_heavy = True if mass >= MASS_THRESHOLD_KG else False

    # Dispatch the package to the correct stack based on the rules
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


🚀 Usage
To use the function, simply call sort() with the package's dimensions and mass.

Prerequisites
Python 3.x

Running the code
Save the code above as a Python file (e.g., package_sorter.py).

You can then import and use the sort function in another Python script or run it directly with some test cases.

Example
# Example usage (in a separate script or Python interpreter)
# from package_sorter import sort # If saved in package_sorter.py

# Test cases
package1_dims = {"width": 50, "height": 50, "length": 50, "mass": 10}
package2_dims = {"width": 100, "height": 100, "length": 100, "mass": 10}
package3_dims = {"width": 150, "height": 50, "length": 50, "mass": 10}
package4_dims = {"width": 50, "height": 50, "length": 50, "mass": 20}
package5_dims = {"width": 100, "height": 100, "length": 100, "mass": 25}
package6_dims = {"width": 50, "height": 50, "length": 160, "mass": 22}

print(f"Package 1 ({package1_dims}): {sort(**package1_dims)}")
# Expected: STANDARD

print(f"Package 2 ({package2_dims}): {sort(**package2_dims)}")
# Expected: SPECIAL

print(f"Package 3 ({package3_dims}): {sort(**package3_dims)}")
# Expected: SPECIAL

print(f"Package 4 ({package4_dims}): {sort(**package4_dims)}")
# Expected: SPECIAL

print(f"Package 5 ({package5_dims}): {sort(**package5_dims)}")
# Expected: REJECTED

print(f"Package 6 ({package6_dims}): {sort(**package6_dims)}")
# Expected: REJECTED

🧪 Testing
You can test the function with various inputs to ensure it behaves as expected under different conditions, including edge cases:

Packages just under/over the volume threshold.

Packages just under/over the dimension threshold.

Packages just under/over the mass threshold.

For example:

# Boundary Case: Just under bulky volume, not bulky dimension, not heavy
print(sort(width=99, height=100, length=100, mass=19))
# Expected: STANDARD

# Boundary Case: At bulky dimension, not heavy
print(sort(width=150, height=40, length=40, mass=19))
# Expected: SPECIAL

📝 Author
This solution was developed as part of a technical screen.

📄 License
This project is open source. Feel free to use, modify. 
