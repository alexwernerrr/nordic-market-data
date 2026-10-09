# Nordic Market Data Pipeline

An automated pipeline that collects Swedish market data every trading day, checks it, and stores it in a SQL database. It is the data foundation for a Value-at-Risk model and a SEK government yield curve model.

> **Status:** in progress (started October 2026).

## What it collects

| Source | Data | Why |
| --- | --- | --- |
| [Riksbank API](https://developer.api.riksbank.se/) | Policy rate, STIBOR, Swedish government bond yields, EUR/SEK and USD/SEK | Rates and FX inputs for the yield curve and risk models |
| Nasdaq Stockholm via [yfinance](https://github.com/ranaroussi/yfinance) | Daily closes for the OMXS30 stocks | Equity returns for the Value-at-Risk model |

## How it works

1. **Fetch:** a GitHub Actions workflow runs every weekday after Nasdaq Stockholm closes and downloads the latest data.
2. **Validate:** checks for missing values, duplicate dates and implausible prices, and fails loudly if something is wrong.
3. **Store:** appends the new rows to a SQLite database in `data/`.
4. **Report:** updates a short daily summary (returns, yield levels, a chart) in this README.

## Project structure

```
src/nordic_data/      pipeline code (fetch, validate, store)
tests/                unit tests (pytest)
data/                 SQLite database written by the pipeline
.github/workflows/    scheduled daily run
```

## Running it locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
python -m nordic_data
```

## Roadmap

- [ ] Fetch Riksbank interest rate series
- [ ] Fetch OMXS30 daily closes
- [ ] Data validation checks
- [ ] Store in SQLite with a small SQL query layer
- [ ] Daily GitHub Actions run
- [ ] Auto-generated daily summary
- [ ] Next projects built on this data: Value-at-Risk / Expected Shortfall model, SEK yield curve model
