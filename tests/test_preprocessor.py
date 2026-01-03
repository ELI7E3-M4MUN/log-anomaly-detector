from preprocessor import Preprocessor

def test_preprocessor():
    pre = Preprocessor()
    df = pre.to_dataframe(["test line"])
    assert "length" in df.columns
