import time, statistics, numpy as np, requests
from config.config import BASE_URL, TIMEOUT

def main():
    url = BASE_URL + "/users/1"
    times, failures, n = [], 0, 100
    for _ in range(n):
        start = time.perf_counter()
        try:
            r = requests.get(url, timeout=TIMEOUT)
            times.append(time.perf_counter()-start)
            if r.status_code != 200: failures += 1
        except requests.RequestException:
            failures += 1
    if not times: raise SystemExit("No measurements collected")
    total = sum(times)
    print("\n=== BENCHMARK RESULT ===")
    print(f"Requests:   {n}")
    print(f"Failures:   {failures}")
    print(f"Average:    {statistics.mean(times)*1000:.2f} ms")
    print(f"Minimum:    {min(times)*1000:.2f} ms")
    print(f"Maximum:    {max(times)*1000:.2f} ms")
    print(f"P50:        {np.percentile(times,50)*1000:.2f} ms")
    print(f"P95:        {np.percentile(times,95)*1000:.2f} ms")
    print(f"P99:        {np.percentile(times,99)*1000:.2f} ms")
    print(f"Throughput: {len(times)/total:.2f} req/s")
if __name__ == "__main__": main()
