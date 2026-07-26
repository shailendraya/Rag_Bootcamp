import time
from datetime import datetime
from collections import defaultdict


class MetricsCollector:

    def __init__(self):
        self.reset()

    def reset(self):
        self._timers = {}
        self.metrics = {}
        self.metadata = {}
        self.counters = defaultdict(int)

    # -----------------------------
    # Timer Methods
    # -----------------------------

    def start(self, name: str):
        self._timers[name] = time.perf_counter()

    def stop(self, name: str):

        if name not in self._timers:
            raise ValueError(f"Timer '{name}' was never started.")

        elapsed = time.perf_counter() - self._timers[name]

        self.metrics[name] = elapsed

        del self._timers[name]

        return elapsed

    # -----------------------------
    # Metadata
    # -----------------------------

    def set(self, key, value):
        self.metadata[key] = value

    def get(self, key, default=None):
        return self.metadata.get(key, default)

    # -----------------------------
    # Counter
    # -----------------------------

    def increment(self, key, amount=1):
        self.counters[key] += amount

    # -----------------------------
    # Report
    # -----------------------------

    def report(self):

        print("=" * 70)
        print("RAG METRICS REPORT")
        print("=" * 70)

        print("\nMetadata")

        for k, v in self.metadata.items():
            print(f"{k:<25}: {v}")

        print("\nTimers")

        for k, v in self.metrics.items():

            if v < 1:
                print(f"{k:<25}: {v*1000:.2f} ms")
            else:
                print(f"{k:<25}: {v:.2f} sec")

        print("\nCounters")

        for k, v in self.counters.items():
            print(f"{k:<25}: {v}")

        print("=" * 70)

    # -----------------------------
    # Dictionary
    # -----------------------------

    def to_dict(self):

        return {
            "metadata": self.metadata,
            "metrics": self.metrics,
            "counters": dict(self.counters),
            "created_at": datetime.utcnow().isoformat()
        }