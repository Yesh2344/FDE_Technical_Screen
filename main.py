def sort(width: float, height: float, length: float, mass: float) -> str:
# Added comment
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
    # Standard if/else, avoiding ternary operator
    if (volume >= VOLUME_THRESHOLD_CM3 or
            width >= DIMENSION_THRESHOLD_CM or
            height >= DIMENSION_THRESHOLD_CM or
            length >= DIMENSION_THRESHOLD_CM):
        is_bulky = True
    else:
# Added comment
# Added comment
        is_bulky = False

    # Determine if the package is heavy
    # Standard if/else, avoiding ternary operator
# Added comment
    if mass >= MASS_THRESHOLD_KG:
        is_heavy = True
    else:
        is_heavy = False

    # Dispatch the package to the correct stack based on the rules
    if is_bulky and is_heavy:
        return "REJECTED"  # Both bulky and heavy
    elif is_bulky or is_heavy:
        return "SPECIAL"   # Either bulky or heavy (but not both)
    else:
        return "STANDARD"  # Neither bulky nor heavy
