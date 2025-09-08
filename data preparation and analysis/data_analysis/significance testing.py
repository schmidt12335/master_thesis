from scipy.stats import chi2_contingency, fisher_exact

"""
# Define the tables
table_AB = [[16, 14], [8, 1]]
table_AC = [[16, 14], [22, 1]]
table_BC = [[8, 1], [22, 1]]

# Create a dictionary of tables for labeling
tables = {
    "A vs B": table_AB,
    "A vs C": table_AC,
    "B vs C": table_BC
}

# Perform and print results
for label, table in tables.items():
    chi2, p, dof, expected = chi2_contingency(table)
    print(f"=== {label} ===")
    print(f"Chi² statistic: {chi2:.4f}")
    print(f"p-value: {p:.4f}")
    print(f"Degrees of freedom: {dof}")
    print("Expected frequencies:")
    for row in expected:
        print("  " + "  ".join(f"{val:.2f}" for val in row))
    print()
"""
# example p-values from pairwise tests
p_values = []

# Run all 3 pairwise tests and collect p-values
p_values.append(fisher_exact([[16, 14], [8, 1]])[1])  # A vs B
p_values.append(fisher_exact([[16, 14], [22, 1]])[1])  # A vs C
p_values.append(fisher_exact([[8, 1], [22, 1]])[1])  # B vs C

# Bonferroni corrected threshold
alpha_corrected = 0.05 / len(p_values)

# Check significance
for i, p in enumerate(p_values):
    print(f"Comparison {i + 1}: p = {p:.4f} {'(significant)' if p < alpha_corrected else ''}")