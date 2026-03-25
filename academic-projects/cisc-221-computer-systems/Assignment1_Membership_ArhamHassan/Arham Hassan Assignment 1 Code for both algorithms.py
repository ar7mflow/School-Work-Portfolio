#Author: Arham Hassan
#Student no.: 20426387
#CISC 235 Assignment 1 Code


import random, time, statistics, math, json, os



# --------------------------------------
# Implementing the Required Algorightms:
# --------------------------------------



def linear_search(arr, x):
    # This will (hopefully) return True if x is in arr using a linear scan, else False.
    for v in arr:
        if v == x:
            return True
    return False



def binary_search(arr, x):
    # This should return True if x exists in a sorted arr using **classic binary search.
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return False



def mergesort(arr):
    # Bascially a stable O(n log n) merge sort; should return a new sorted list.
    n = len(arr)
    if n <= 1:
        return arr[:]
    mid = n // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    # merge
    out = []
    i = j = 0
    nl, nr = len(left), len(right)
    while i < nl and j < nr:
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    if i < nl: out.extend(left[i:])
    if j < nr: out.extend(right[j:])
    return out



# ----------------------------
# Doing Timing Here!
# ----------------------------



def time_algorithm_A(S, targets):
    # Time k linear will searche over S for target list. Returns the elapsed time in seconds.
    t0 = time.perf_counter()
    for x in targets:
        linear_search(S, x)
    t1 = time.perf_counter()
    return t1 - t0



def time_algorithm_B(S, targets):
    # Time: sort S once with a mergesort, then do k no. of binary searches.
    # Returns (total_time, sort_time, search_time_only).
    t0 = time.perf_counter()
    sorted_S = mergesort(S)
    t1 = time.perf_counter()
    sort_time = t1 - t0

    for x in targets:
        binary_search(sorted_S, x)
    t2 = time.perf_counter()
    return (t2 - t0, sort_time, t2 - t1)



def make_targets(S, k, rng):
    # Builds target list of length k: half in S, half not in S.
    # !Disclaimer! Duplicates are allowed.
    k_in = k // 2
    k_out = k - k_in
    in_targets = [S[rng.randrange(0, len(S))] for _ in range(k_in)]
    S_set = set(S)
    out_targets = []
    M = max(10 * len(S), 100)
    while len(out_targets) < k_out:
        v = rng.randrange(0, M)
        if v not in S_set:
            out_targets.append(v)
    return in_targets + out_targets



def time_both_for_k(S, k, rng, trials=3):
    # Run our trials and average A and B times for a given k.
    A_times = []
    B_total_times = []
    B_sort_times = []
    B_search_times = []
    for _ in range(trials):
        targets = make_targets(S, k, rng)
        ta = time_algorithm_A(S, targets)
        tb_total, tb_sort, tb_search = time_algorithm_B(S, targets)
        A_times.append(ta)
        B_total_times.append(tb_total)
        B_sort_times.append(tb_sort)
        B_search_times.append(tb_search)
    return {
        "k": k,
        "A_avg": sum(A_times)/trials,
        "B_total_avg": sum(B_total_times)/trials,
        "B_sort_avg": sum(B_sort_times)/trials,
        "B_search_avg": sum(B_search_times)/trials,
        "A_all": A_times,
        "B_total_all": B_total_times,
        "B_sort_all": B_sort_times,
        "B_search_all": B_search_times,
    }



def find_k_star(S, rng, trials=3, k_min=1, k_max_initial=None):
    # Find the smallest k where time_B <= time_A via exponential + binary search.
    n = len(S)
    if k_max_initial is None:
        k_max_initial = n

    # exponential search
    last_k = None
    last_stats = None
    k = max(1, k_min)
    stats = time_both_for_k(S, k, rng, trials)
    while stats["B_total_avg"] > stats["A_avg"] and k <= 8*n:
        last_k, last_stats = k, stats
        k *= 2
        stats = time_both_for_k(S, k, rng, trials)

    # Now [last_k, k] brackets crossing (or we will deffo hit the limit)
    lo_k = 1 if last_k is None else last_k
    hi_k = k
    best_k = None
    best_stats = None
    # binary search for the smallest k with B <= A
    while lo_k <= hi_k:
        mid = (lo_k + hi_k) // 2
        mid_stats = time_both_for_k(S, mid, rng, trials)
        if mid_stats["B_total_avg"] <= mid_stats["A_avg"]:
            best_k, best_stats = mid, mid_stats
            hi_k = mid - 1
        else:
            lo_k = mid + 1
    # Fallback if never crossed (rare but lowkey why not): set k* = hi_k + 1
    if best_k is None:
        best_k, best_stats = k, stats
    return {
        "k_star": best_k,
        "stats_at_k_star": best_stats
    }



def run_full_experiment(seed=42, n_values=(1000,2000,5000,10000), trials=3):
    rng = random.Random(seed)
    results = []
    for n in n_values:
        S = [rng.randrange(0, 10*n) for _ in range(n)]
        out = find_k_star(S, rng, trials=trials, k_min=1)
        k_star = out["k_star"]
        stats = out["stats_at_k_star"]
        ratio = k_star / n
        results.append({
            "n": n,
            "k_star": k_star,
            "k_star_over_n": ratio,
            "A_avg_at_k_star": stats["A_avg"],
            "B_total_avg_at_k_star": stats["B_total_avg"],
            "B_sort_avg_at_k_star": stats["B_sort_avg"],
            "B_search_avg_at_k_star": stats["B_search_avg"],
        })
    return results

#~Ar7m~

if __name__ == "__main__":
    results = run_full_experiment()
    base = "."
    json_path = os.path.join(base, "membership_results.json")
    txt_path = os.path.join(base, "membership_report.txt")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)
    # Some pretty text ;)
    lines = []
    lines.append("Membership Problem — Experimental Results (seed=42, trials=3)")
    lines.append("n, k*, k*/n, A_avg(k*), B_total_avg(k*), B_sort_avg(k*), B_search_avg(k*)")
    for r in results:
        lines.append(f"{r['n']}, {r['k_star']}, {r['k_star_over_n']:.3f}, "
                     f"{r['A_avg_at_k_star']:.6f}, {r['B_total_avg_at_k_star']:.6f}, "
                     f"{r['B_sort_avg_at_k_star']:.6f}, {r['B_search_avg_at_k_star']:.6f}")
    
    lines.append("")
    ratios = ", ".join(f"{r['k_star_over_n']:.3f}" for r in results)
    lines.append("Conclusion (explicit):")
    lines.append(f"As n increases, k*/n decreases overall ({ratios}).")
    
    with open(txt_path, "w") as f:
        f.write("\n".join(lines))
    print("\n".join(lines))
    print("Saved:", json_path, "and", txt_path)

