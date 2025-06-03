from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def load_data(path: str) -> pd.DataFrame:
    """Load heart disease data from a CSV file."""
    df = pd.read_csv(path, na_values="?", skipinitialspace=True)
    df.columns = df.columns.str.strip()
    """Load biomedical data from a CSV file."""
    df = pd.read_csv(path)

    return df


def show_summary(df: pd.DataFrame) -> None:
    """Print basic statistics from the dataset."""
    print("Summary statistics:\n")
    print(df.describe())


def plot_data(df: pd.DataFrame, output_path: Path) -> None:
    """Plot cholesterol versus age with diagnosis color coding."""
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(
        df["age"],
        df["chol"],
        c=df["diagnosis"],
        cmap="viridis",
        s=40,
        edgecolor="k",
    )
    plt.title("Cholesterol vs Age")
    plt.xlabel("Age")
    plt.ylabel("Cholesterol")
    cbar = plt.colorbar(scatter)
    cbar.set_label("Diagnosis")
    """Plot heart rate vs age scatter plot and save it as an image."""
    plt.figure(figsize=(8, 6))
    plt.scatter(df["Age"], df["HeartRate"], c="blue")
    plt.title("Heart Rate vs Age")
    plt.xlabel("Age")
    plt.ylabel("Heart Rate")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")


def main():
    base_dir = Path(__file__).resolve().parent
    data_path = base_dir / "data" / "heart_disease.csv"
    df = load_data(data_path)
    show_summary(df)
    output_plot = base_dir / "chol_vs_age.png"
    data_path = base_dir / "data" / "sample_biomed.csv"
    df = load_data(data_path)
    show_summary(df)
    output_plot = base_dir / "heart_rate_vs_age.png"
    plot_data(df, output_plot)


if __name__ == "__main__":
    main()
