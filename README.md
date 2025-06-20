# NYC 311 Service Requests Analytics

## Problem Statement
New York City receives over 3 million service requests annually through its 311 system, from noise complaints and potholes to heating issues and illegal parking. This massive volume of citizen feedback contains valuable insights about city operations, service quality, and community needs, but remains largely untapped due to:

- **Data Fragmentation**: 24+ million records spread across multiple systems with inconsistent formats
- **Limited Visibility**: No centralized view of service patterns, response times, or agency performance  
- **Reactive Management**: City agencies lack predictive insights to proactively address recurring issues
- **Public Transparency Gap**: Citizens have limited visibility into how their requests are handled and resolved

## Dataset
- **Source**: [NYC Open Data - 311 Service Requests from 2010 to Present](https://dev.socrata.com/foundry/data.cityofnewyork.us/erm2-nwe9)
- **Scale**: 24+ million records, 41 columns, updated daily
- **Coverage**: All 5 boroughs, 200+ complaint types, 50+ agencies

## 📡 Data Upload — API Ingest to PostgreSQL

Fetching real-time data from a public API (NYC 311 Service Requests) and store it into a PostgreSQL database using Python.

## 🚀 Objective

To build a repeatable, automated pipeline that:
- Pulls complaint data from the NYC Open Data API (`erm2-nwe9`)
- Cleans and prepares the data
- Inserts it into a structured PostgreSQL table for further analysis or reporting

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core scripting language |
| Requests | Fetch data from REST API |
| Pandas | Handle JSON, clean and structure data |
| SQLAlchemy | Connect and push data into PostgreSQL |
| PostgreSQL | Data storage layer |

---

## 🔁 Process

1. **API Connection**
   - Used NYC Open Data’s Socrata endpoint
   - Applied a `$where=created_date >= [last 7 days]` filter to avoid pulling all historical data

2. **Data Cleaning**
   - Used `pandas.json_normalize()` to flatten nested fields like `location`
   - Handled missing columns by adding `None` values for expected fields

3. **Database Insert**
   - Connected to PostgreSQL using SQLAlchemy:
     ```python
     engine = create_engine("postgresql+psycopg2://postgres:9890@localhost:5432/nyc_data")
     ```
   - Used `df.to_sql(..., if_exists="append")` to push data without overwriting the table



