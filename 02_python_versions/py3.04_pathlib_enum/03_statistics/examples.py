"""statistics — Python 3.4+ (PEP 450); newer helpers noted per example."""
import statistics as st
import sys

MIN_VERSION = (3, 8)
latencies = [120, 135, 110, 400, 125, 130, 118]


def example_01_mean_median():
    print("mean", round(st.mean(latencies), 1), "| median", st.median(latencies))


def example_02_mode_and_multimode():
    votes = ["red", "blue", "red", "green", "blue"]
    print(st.mode(votes), st.multimode(votes))


def example_03_stdev_variance():
    print(round(st.stdev(latencies), 2), round(st.pvariance(latencies), 2))


def example_04_fmean_is_fast_float_mean():
    print(st.fmean([1, 2, 3, 4]))


def example_05_quantiles_percentiles():
    q = st.quantiles(latencies, n=4)
    print("quartiles:", q)


def example_06_median_low_high():
    data = [1, 3, 5, 7]
    print(st.median(data), st.median_low(data), st.median_high(data))


def example_07_normal_distribution():
    iq = st.NormalDist(mu=100, sigma=15)
    print(f"P(IQ < 130) = {iq.cdf(130):.3f}")


def example_08_geometric_harmonic_mean():
    growth = [1.10, 1.20, 0.95]
    print(round(st.geometric_mean(growth), 4), round(st.harmonic_mean([40, 60]), 2))


def example_09_correlation_and_regression_310():
    if sys.version_info >= (3, 10):
        hours = [1, 2, 3, 4, 5]
        score = [52, 58, 65, 70, 78]
        print("r =", round(st.correlation(hours, score), 3))
        slope, intercept = st.linear_regression(hours, score)
        print(f"score ≈ {slope:.1f}*hours + {intercept:.1f}")
    else:
        print("needs 3.10+")


def example_10_fractions_stay_exact():
    from fractions import Fraction
    print(st.mean([Fraction(1, 3), Fraction(1, 6)]))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
