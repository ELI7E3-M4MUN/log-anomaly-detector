import pandas as pd

class Preprocessor:
    def to_dataframe(self, lines):
        df = pd.DataFrame(lines, columns=["raw"])
        df["length"] = df["raw"].str.len()
        df["digits"] = df["raw"].str.count(r"\d")
        df["uppercase"] = df["raw"].str.count(r"[A-Z]")
        return df
