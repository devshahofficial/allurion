import pandas as pd


def convert_csv_to_string(csv_path: str, rows: int) -> list:
    """
    Converts the first row of a CSV file into a list of strings, where each string represents
    a single row entry with column names and their corresponding values.

    Args:
        csv_path (str): The file path of the CSV file to be processed.
        rows (int): Numbers of rows to be processed.

    Returns:
        list: A list of strings, where each string contains column names and their corresponding values.

    Raises:
        FileNotFoundError: If the specified CSV file path does not exist.
    """
    try:
        df = pd.read_csv(csv_path, nrows=rows)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {csv_path}") from e

    rows = []
    for index, row in df.iterrows():
        entry_string = ", ".join([f"{col} = {str(row[col])}" for col in df.columns])
        rows.append(entry_string)
    return rows
