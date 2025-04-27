import random
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate  # For nicer console output
import hashlib  # For better encryption
from scipy import stats  # For distribution tests


# Step 1: Generate the dataset
def create_age_dataset(num_rows, mean=40, stddev=10, enforce_normal=True):
    if enforce_normal:
        # Generate normal distribution
        ages = np.random.normal(mean, stddev, num_rows * 5)
        # filter age
        ages = ages[(ages >= 18) & (ages <= 70)]
        ages = ages[:num_rows]
        ages = ages.astype(int)

    # output
    sample_size = min(10, num_rows)
    sample_ages = ages[:sample_size]
    print(f"\n Generated {num_rows} age records (showing first {sample_size}):")
    print(f"  {sample_ages} {'...' if num_rows > sample_size else ''}")
    print(f"  Age range: {np.min(ages)}-{np.max(ages)}, Average: {np.mean(ages):.1f}")

    return ages


# Step 2: Encrypt the dataset
def deterministic_encrypt(value):
    hash_obj = hashlib.sha256(str(value).encode())
    # Take first 10 digits of hexadecimal representation
    encrypted_value = int(hash_obj.hexdigest()[:10], 16)
    return encrypted_value

def encrypt_dataset(dataset):
    encrypted = [deterministic_encrypt(age) for age in dataset]
    #  output
    sample_size = min(5, len(dataset))
    sample_data = list(zip(dataset[:sample_size], encrypted[:sample_size]))
    print("\n Encrypted dataset:")
    print("  Original → Encrypted (showing first 5):")
    for original, encrypted_val in sample_data:
        print(f"  {original} → {encrypted_val}")

    return encrypted


# Step 3: Simulate range queries
def simulate_queries(dataset, num_queries):
    queries = []
    for i in range(num_queries):
        low = random.randint(18, 65)
        high = random.randint(low, 70)
        result_indices = [i for i, age in enumerate(dataset) if low <= age <= high]
        queries.append((low, high, result_indices))
    # output
    print(f"\n Simulated {num_queries} range queries (showing first 5):")
    sample_queries = queries[:5]
    table_data = []
    for i, (low, high, indices) in enumerate(sample_queries):
        count = len(indices)
        percent = (count / len(dataset)) * 100
        table_data.append([i + 1, f"{low}-{high}", count, f"{percent:.1f}%"])
    headers = ["Query", "Age Range", "Matches", "% of Dataset"]
    print(tabulate(table_data, headers=headers, tablefmt="simple"))

    return queries


# Step 4: Reconstruct data using leakage
def reconstruct_data(queries, num_rows, min_age=18, max_age=70, enforce_normal=True, mean=40, stddev=10):
    print(f"\n Reconstructing data from {len(queries)} queries...")
    approximated_ages = np.zeros(num_rows, dtype=float)
    counts = np.zeros(num_rows, dtype=int)
    # Basic reconstruction
    for low, high, indices in queries:
        for idx in indices:
            approximated_ages[idx] += (low + high) / 2
            counts[idx] += 1

    approximated_ages = np.divide(approximated_ages, counts, out=np.zeros_like(approximated_ages), where=counts > 0)
    approximated_ages = np.clip(approximated_ages, min_age, max_age)

    # Keep track of which indices were actually reconstructed
    reconstructed_mask = counts > 0

    # Get ranks of the approximated values (for the reconstructed indices)
    recon_values = approximated_ages[reconstructed_mask]
    if len(recon_values) > 0:
        ranks = stats.rankdata(recon_values) - 1
        # Generate a normal distribution with the same mean and stddev
        perfect_normal = np.random.normal(mean, stddev, len(recon_values))
        perfect_normal = np.clip(perfect_normal, min_age, max_age)
        perfect_normal.sort()
        # Replace the values with corresponding perfect normal values based on rank
        new_values = np.zeros_like(recon_values)
        for i, rank in enumerate(ranks):
            new_values[i] = perfect_normal[int(rank * len(perfect_normal) / len(ranks))]
        # Put the new values back
        approximated_ages[reconstructed_mask] = new_values

    return approximated_ages


# Step 5: Evaluate error and distribution analysis
def evaluate_error(real_data, approximated_data):
    errors = np.abs(real_data - approximated_data)
    max_error = np.max(errors)
    min_error = np.min(errors[approximated_data > 0]) if np.any(approximated_data > 0) else 0  # Exclude zeros
    global_error_rate = np.mean(errors)

    # Error analysis
    print("\n Error Analysis:")
    print(f"  Average error: {global_error_rate:.2f} years")
    print(f"  Maximum error: {max_error:.2f} years")
    print(f"  Minimum error: {min_error:.2f} years")

    # Error distribution
    error_ranges = [(0, 1), (1, 3), (3, 5), (5, 10), (10, float('inf'))]
    error_counts = []

    for low, high in error_ranges:
        count = np.sum((errors >= low) & (errors < high))
        percent = (count / len(errors)) * 100
        error_counts.append([f"{low}-{high if high != float('inf') else '∞'}", count, f"{percent:.1f}%"])

    print("\n  Error Distribution:")
    headers = ["Error Range (years)", "Count", "Percentage"]
    print(tabulate(error_counts, headers=headers, tablefmt="simple"))

    return global_error_rate


# Step 6: Visualization
def plot_distributions(real_data, approximated_data):
    plt.figure(figsize=(15, 10))

    # Histogram comparison
    plt.subplot(2, 2, 1)
    plt.hist(real_data, bins=15, alpha=0.7, label="Real Ages", color="blue")
    plt.hist(approximated_data, bins=15, alpha=0.7, label="Reconstructed Ages", color="red")
    plt.legend()
    plt.title("Age Distribution: Real vs. Reconstructed")
    plt.xlabel("Age")
    plt.ylabel("Frequency")

    # QQ Plot for real data
    plt.subplot(2, 2, 2)
    stats.probplot(real_data, plot=plt)
    plt.title("Q-Q Plot: Real Ages")

    # QQ Plot for approximated data
    plt.subplot(2, 2, 3)
    stats.probplot(approximated_data, plot=plt)
    plt.title("Q-Q Plot: Reconstructed Ages")

    plt.tight_layout()
    plt.savefig('age_reconstruction_analysis.png')
    print("\n Visualization saved as 'age_reconstruction_analysis.png'")
    plt.show()


# Main process
def main():
    print("\n" + "=" * 60)
    print("SECURE AGE DATA ANALYSIS & RECONSTRUCTION SIMULATION")
    print("=" * 60)

    num_rows = 100
    num_queries = 50
    enforce_normal = True

    print(f"\nConfiguration:")
    print(f"  • Dataset size: {num_rows} records")
    print(f"  • Number of queries: {num_queries}")

    # Same mean and stddev for both datasets
    mean = 40
    stddev = 10

    real_ages = create_age_dataset(num_rows, mean=mean, stddev=stddev, enforce_normal=enforce_normal)
    encrypted_ages = encrypt_dataset(real_ages)
    queries = simulate_queries(real_ages, num_queries)
    approximated_ages = reconstruct_data(queries, num_rows, enforce_normal=enforce_normal, mean=mean, stddev=stddev)
    global_error_rate = evaluate_error(real_ages, approximated_ages)

    plot_distributions(real_ages, approximated_ages)


# Run the script
if __name__ == "__main__":
    main()