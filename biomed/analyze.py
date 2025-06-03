from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def load_data(path: str) -> pd.DataFrame:
    """Load biomedical data from a CSV file."""
    # The dataset from the UCL repository has no header, so we assign
    # column names on load.
    df = pd.read_csv(path, header=None, names=["Feature1", "Feature2"])
    return df


def show_summary(df: pd.DataFrame) -> None:
    """Print basic statistics from the dataset."""
    print("Summary statistics:\n")
    print(df.describe())


def plot_data(df: pd.DataFrame, output_path: Path) -> None:
    """Plot feature scatter plot and save it as an image."""
    plt.figure(figsize=(8, 6))
    plt.scatter(df["Feature1"], df["Feature2"], c="blue")
    plt.title("Feature2 vs Feature1")
    plt.xlabel("Feature1")
    plt.ylabel("Feature2")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")


def main():
    base_dir = Path(__file__).resolve().parent
    data_path = base_dir / "data" / "ucl_samples.csv"
    df = load_data(data_path)
    show_summary(df)
    output_plot = base_dir / "feature_scatter.png"
    plot_data(df, output_plot)


if __name__ == "__main__":
    main()
