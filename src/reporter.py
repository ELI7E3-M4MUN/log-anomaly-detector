import json
import os

class Reporter:
    def save(self, df, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_json(output_path, orient="records", indent=2)
