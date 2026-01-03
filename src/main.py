import argparse
from log_loader import LogLoader
from preprocessor import Preprocessor
from model import ModelLoader
from detector import Detector
from reporter import Reporter
from config import MODEL_PATHS

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--logfile", required=True)
    parser.add_argument("--output", default="data/processed/output.json")
    args = parser.parse_args()

    loader = LogLoader()
    pre = Preprocessor()
    ml = ModelLoader()
    det = Detector()
    rep = Reporter()

    lines = loader.load(args.logfile)
    df = pre.to_dataframe(lines)

    model = ml.load(MODEL_PATHS["isolation_forest"])
    result = det.detect(model, df)

    rep.save(result, args.output)
    print("Analysis complete.")

if __name__ == "__main__":
    main()
