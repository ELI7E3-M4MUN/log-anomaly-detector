# log-anomaly-detector

log-anomaly-detector is a machine-learning–based anomaly detection tool designed for security analysts, SOC teams, and threat hunters. It analyzes system and application logs to identify unusual patterns, suspicious behavior, and potential security incidents.

The tool supports multiple log sources, applies unsupervised ML algorithms, and provides both a command-line interface and an optional web dashboard for visualization.

---

## Features

- Multi-source log ingestion (syslog, auth.log, nginx logs, custom formats)
- Unsupervised ML anomaly detection using Isolation Forest, LOF, and One-Class SVM
- Real-time or batch log analysis
- CLI interface for automation workflows
- Optional web dashboard for visualizing anomalies
- Security-focused insights such as suspicious login attempts, brute-force patterns, and unusual traffic behavior
- Lightweight, modular, and easy to extend

---

## Installation

```
git clone https://github.com/secwexen/log-anomaly-detector.git
cd log-anomaly-detector
pip install -r requirements.txt
```

---

## Usage

### CLI Mode

Analyze a log file:

```
python src/main.py --logfile data/sample_logs/syslog.log
```

Run continuous monitoring:

```
python src/main.py --logfile /var/log/auth.log --watch
```

Export results:

```
python src/main.py --logfile syslog.log --output report.json
```

---

## Web Dashboard

Start the web interface:

```
python src/webapp/app.py
```

Then open:

```
http://localhost:5000
```

---

## Project Structure

- `src/`  
  Core source code including log loader, preprocessing, ML models, and detection logic.

- `src/webapp/`  
  Lightweight Flask-based dashboard for visualizing anomalies.

- `data/`  
  Sample logs and processed datasets.

- `models/`  
  Serialized ML models.

- `tests/`  
  Unit tests for core components.

---

## Supported Algorithms

- Isolation Forest  
- Local Outlier Factor (LOF)  
- One-Class SVM  

These models allow anomaly detection without requiring labeled datasets.

---

## License

This project is licensed under the Apache License 2.0.
