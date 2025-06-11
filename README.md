# 🛍️ AI Developer | Fake Store Analyzer

This Python project fetches product data from the [Fake Store API](https://fakestoreapi.com/) and performs various analyses, including price statistics, category breakdowns, and rating summaries. It also provides a lightweight Flask web interface for accessing live analysis results at configurable intervals.

## 🚀 Video Showcase

https://github.com/user-attachments/assets/44769b51-805f-4145-8c41-8ead188fc350

## 🔍 Features

* Fetches live product data from Fake Store API.
* Analyzes:

  * Total product count
  * Average price
  * Most expensive and cheapest products
  * Product distribution by category
  * Products with high and low ratings
* Outputs JSON reports (saved with timestamps).
* Flask server exposes analysis results via RESTful endpoints.
* Automatically refreshes data at a configurable interval.

## 📁 Project Structure

```
.
├── app.py                  # Flask web service
├── fake_store_analyzer.py # Core data fetching and analysis logic
├── product_analysis_*.json# Output files (timestamped)
└── README.md               # Project documentation
```

## 🔧 Requirements

* Python 3.7+
* pip

### Install dependencies:

```bash
pip install requests flask
```

## 🚀 Usage

### Run the Analyzer (Standalone CLI Mode)

```bash
python fake_store_analyzer.py
```

This will:

* Fetch data from Fake Store API
* Analyze and print the results
* Save results to a `product_analysis_YYYYMMDD_HHMMSS.json` file

### Run the Web Service

```bash
python app.py
```

The Flask app starts and serves live analysis updates via:

#### Endpoints:

* `GET /results` – Returns the latest product analysis
* `POST /start` – Starts/resumes the analyzer loop
* `POST /stop` – Stops the analyzer loop
* `POST /set_interval` – Sets refresh interval in minutes
  Example payload:

  ```json
  { "interval": 1 }
  ```
### CURL Commands:

* `curl http://localhost:5000/results` – Returns the latest product analysis
* `curl -X POST http://localhost:5000/start` – Starts/resumes the analyzer loop
* `curl -X POST http://localhost:5000/stop` – Stops the analyzer loop
* `curl -X POST http://localhost:5000/set_interval -H "Content-Type: application/json" -d "{\"interval\":1.0}"` – Sets refresh interval in minutes

## ⚙️ Customization

* Default analysis interval is **0.5 minutes** (30 seconds).
* Modify `interval_minutes` in `app.py` to change the default.

## 📝 Notes

* Results are updated in the background using a thread.
* High-rated products are those with a rating > 4.1.
* Low-rated products are those with a rating < 3.

## 🧑‍💻 Author

*Created by Pantelis.*
