import numpy as np

class Detector:
    def detect(self, model, df):
        features = df[["length", "digits", "uppercase"]]
        scores = model.decision_function(features)
        df["anomaly_score"] = scores
        df["is_anomaly"] = scores < np.percentile(scores, 5)
        return df
