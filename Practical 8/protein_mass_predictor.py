RESIDUE_MASS_AMU = {
    "G": 57.02,
    "A": 71.04,
    "S": 87.03,
    "P": 97.05,
    "V": 99.07,
    "T": 101.05,
    "C": 103.01,
    "I": 113.08,
    "L": 113.08,
    "N": 114.04,
    "D": 115.03,
    "Q": 128.06,
    "K": 128.09,
    "E": 129.04,
    "M": 131.04,
    "H": 137.06,
    "F": 147.07,
    "R": 156.10,
    "Y": 163.06,
    "W": 186.08,
}

def predict_protein_mass(sequence):
    """Input: sequence (str), a protein sequence using one-letter amino-acid codes.

    Returns:
        float: Total residue mass in atomic mass units (amu).

    Raises:
        TypeError: If sequence is not a string.
        ValueError: If sequence contains an amino acid with no recorded mass.
    """
    if not isinstance(sequence, str):
        raise TypeError("Sequence must be provided as a string.")
    total_mass = 0.0
    for index, residue in enumerate(sequence.upper(), start=1):
        if residue not in RESIDUE_MASS_AMU:
            raise ValueError(
                f"Unknown amino acid '{residue}' at position {index}. "
                "No recorded residue mass is available."
            )
        total_mass += RESIDUE_MASS_AMU[residue]
    return total_mass

# An example of calliung a function #
if __name__ == "__main__":
    example_sequence = "GAV"
    mass = predict_protein_mass(example_sequence)
    print(f"Sequence: {example_sequence}")
    print(f"Predicted protein mass: {mass:.2f} amu")
    invalid_sequence = "GAX"
    try:
        predict_protein_mass(invalid_sequence)
    except ValueError as error:
        print(f"Error for sequence '{invalid_sequence}': {error}")
