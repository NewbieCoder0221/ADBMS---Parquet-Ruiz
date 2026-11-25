import time
import duckdb

# Benchmark CSV read
start = time.perf_counter()
# df = duckdb.read_csv("website_sessions.csv")
df = duckdb.read_parquet("output.parquet")
elapsed = time.perf_counter() - start
print(f"read_csv: {elapsed:.4f} seconds")

