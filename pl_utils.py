import polars as pl
from typing import Optional


def _bytes_to_human(n: int) -> str:
    # simple human-readable bytes
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024.0:
            return f"{n:3.1f}{unit}"
        n /= 1024.0
    return f"{n:.1f}PB"


def pl_info(
    df: pl.DataFrame,
    show_memory: bool = True,
    show_unique: bool = True,
    col_width: Optional[int] = None,
):
    """
    Print a pandas-like DataFrame.info() for a Polars DataFrame.

    Parameters
    ----------
    df : pl.DataFrame
        The Polars DataFrame.
    show_memory : bool
        Show an estimated memory usage (in human-readable form).
    show_unique : bool
        Compute and show the number of unique values per column (may be slower).
    col_width : Optional[int]
        Force column name column width; if None auto-sizes to longest column name.
    """
    n_rows, n_cols = df.shape
    print(f"Polars DataFrame info — shape: ({n_rows}, {n_cols})")

    if show_memory:
        try:
            size_bytes = df.estimated_size()
            print(f"Estimated memory usage: {_bytes_to_human(size_bytes)}")
        except Exception:
            # fallback if method not present
            print("Estimated memory usage: (unavailable)")

    # prepare column widths
    names = list(df.schema.keys())
    max_name_len = max((len(n) for n in names), default=4)
    name_col_w = col_width if col_width is not None else max(10, max_name_len + 2)

    header = f"{'Column':{name_col_w}} {'Dtype':12} {'Non-Null':>9} {'Nulls':>7}"
    if show_unique:
        header += "  Unique"
    print("\n" + header)
    print("-" * len(header))

    for name, dtype in df.schema.items():
        nulls = df[name].null_count()
        non_null = n_rows - nulls
        dtype_str = str(dtype)
        line = f"{name:{name_col_w}} {dtype_str:12} {non_null:9d} {nulls:7d}"
        if show_unique:
            # n_unique can be somewhat expensive for large columns
            try:
                unique_count = int(df[name].n_unique())
            except Exception:
                unique_count = -1
            line += f"  {unique_count if unique_count >= 0 else 'N/A':>6}"
        print(line)

    # final summary similar to pandas
    print("\ndtypes:")
    # count dtypes
    dtype_counts = {}
    for dtype in df.schema.values():
        s = str(dtype)
        dtype_counts[s] = dtype_counts.get(s, 0) + 1
    for dt_name, cnt in dtype_counts.items():
        print(f"  {dt_name}: {cnt}")
