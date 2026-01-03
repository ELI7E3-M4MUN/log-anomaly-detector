import os

class LogLoader:
    def load(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Log file not found: {path}")

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.readlines()
