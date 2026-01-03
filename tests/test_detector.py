import pandas as pd
from detector import Detector

def test_detector():
    df = pd.DataFrame({"length": [10], "digits": [2], "uppercase": [1]})
    det = Detector()
    class DummyModel:
        def decision_function(self, X):
            return [0.5]
    result = det.detect(DummyModel(), df)
    assert "anomaly_score" in result.columns
