from pathlib import Path
DATA_DIR = Path(__file__).resolve().parent


def read_fasta(filename):
    """Read one FASTA file and return its header and sequence."""
    path = DATA_DIR / filename
    header = "" 
    sequence_lines = []

    with path.open() as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header:
                    raise ValueError(f"{filename} contains more than one sequence.")
                header = line[1:]
            else:
                sequence_lines.append(line.upper())
    sequence = "".join(sequence_lines)
    if not header:
        raise ValueError(f"{filename} does not contain a FASTA header.")
    if not sequence:
        raise ValueError(f"{filename} does not contain a protein sequence.")
    return header, sequence


def read_blosum62(filename):
    """Read a BLOSUM62 text file and return a matrix dictionary."""
    path = DATA_DIR / filename
    useful_lines = []

    with path.open() as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                useful_lines.append(line)
    if not useful_lines:
        raise ValueError(f"{filename} does not contain a scoring matrix.")

    column_amino_acids = useful_lines[0].split()
    matrix = {}

    for line in useful_lines[1:]:
        parts = line.split()
        row_amino_acid = parts[0]
        scores = parts[1:]
        if len(scores) != len(column_amino_acids):
            raise ValueError(f"Invalid BLOSUM62 row for amino acid {row_amino_acid}.")
        matrix[row_amino_acid] = {}
        for amino_acid, score in zip(column_amino_acids, scores):
            matrix[row_amino_acid][amino_acid] = int(score)
    return matrix


def blosum_score(matrix, amino_acid_1, amino_acid_2):
    """Return the BLOSUM62 score for one amino acid pair."""
    try:
        return matrix[amino_acid_1][amino_acid_2]
    except KeyError:
        raise ValueError(
            f"No BLOSUM62 score for amino acid pair "
            f"{amino_acid_1}-{amino_acid_2}."
        )


def compare_sequences(comparison_name, sequence_1, sequence_2, matrix):
    """Compare two equal-length sequences without gaps."""
    if len(sequence_1) != len(sequence_2):
        raise ValueError(
            f"Cannot compare {comparison_name}: sequence lengths are "
            f"{len(sequence_1)} and {len(sequence_2)}. "
            "A non-gapped global alignment needs sequences of equal length."
        )

    total_score = 0
    identical_count = 0

    for amino_acid_1, amino_acid_2 in zip(sequence_1, sequence_2):
        total_score += blosum_score(matrix, amino_acid_1, amino_acid_2)
        if amino_acid_1 == amino_acid_2:
            identical_count += 1

    percentage_identity = (identical_count / len(sequence_1)) * 100

    return {
        "name": comparison_name,
        "length": len(sequence_1),
        "score": total_score,
        "identical": identical_count,
        "identity": percentage_identity,
    }


def print_result(result):
    """Print one comparison result clearly."""
    print(f"Comparison: {result['name']}")
    print(f"Sequence length: {result['length']} amino acids")
    print(f"BLOSUM62 alignment score: {result['score']}")
    print(f"Identical amino acids: {result['identical']}")
    print(f"Percentage identity: {result['identity']:.2f}%")
    print()


def main():
    """Run all three pairwise comparisons."""
    matrix = read_blosum62("BLOSUM62.txt")

    human_header, human_sequence = read_fasta("human_DLX5.fasta")
    mouse_header, mouse_sequence = read_fasta("mouse_DLX5.fasta")
    random_header, random_sequence = read_fasta("random_protein.fasta")

    print("Pairwise non-gapped global alignment using BLOSUM62")
    print("=" * 40)
    print(f"Human sequence: {human_header}")
    print(f"Mouse sequence: {mouse_header}")
    print(f"Random sequence: {random_header}")
    print()

    comparisons = [
        ("human DLX5 vs mouse DLX5", human_sequence, mouse_sequence),
        ("human DLX5 vs random protein", human_sequence, random_sequence),
        ("mouse DLX5 vs random protein", mouse_sequence, random_sequence),
    ]
    results = []

    for comparison_name, sequence_1, sequence_2 in comparisons:
        result = compare_sequences(comparison_name, sequence_1, sequence_2, matrix)
        results.append(result)
        print_result(result)

    best_by_score = max(results, key=lambda result: result["score"])
    best_by_identity = max(results, key=lambda result: result["identity"])
    print("Closest related sequence pair")
    print("=" * 40)

    if best_by_score["name"] == best_by_identity["name"]:
        print(
            f"{best_by_score['name']} is the most closely related pair because "
            "it has both the highest BLOSUM62 score and the highest percentage "
            "identity."
        )
    else:
        print(
            "The two measures do not select the same pair, so the result should "
            "be interpreted carefully."
        )
        print(
            f"Highest BLOSUM62 score: {best_by_score['name']} "
            f"({best_by_score['score']})"
        )
        print(
            f"Highest percentage identity: {best_by_identity['name']} "
            f"({best_by_identity['identity']:.2f}%)"
        )


if __name__ == "__main__":
    main()