LOG_SOURCES = [
    "data/sample_logs/syslog.log",
    "data/sample_logs/auth.log",
    "data/sample_logs/nginx.log"
]

MODEL_PATHS = {
    "isolation_forest": "models/isolation_forest.pkl",
    "lof": "models/lof.pkl",
    "ocsvm": "models/oneclass_svm.pkl"
}

PROCESSED_DIR = "data/processed/"
