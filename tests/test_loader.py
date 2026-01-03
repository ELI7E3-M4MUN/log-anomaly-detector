from log_loader import LogLoader

def test_loader():
    loader = LogLoader()
    lines = loader.load("data/sample_logs/syslog.log")
    assert isinstance(lines, list)
