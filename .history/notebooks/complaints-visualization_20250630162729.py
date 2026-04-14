import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from datetime import datetime, timedelta

# --- 1. Create a database connection ---
engine = create_engine("postgresql+psycopg2://postgres:9890@localhost:5432/nyc_data")

# --- 2. Define relevant columns to load ---
relevant_columns = [
    'unique_key', 'created_date', 'agency_name', 'complaint_type', 'descriptor',
    'location_type', 'incident_zip', 'incident_address', 'city', 'status',
    'resolution_action_updated_date', 'closed_date', 'resolution_description'
]

# --- 3. Define date filter to limit data (e.g., last 30 days only) ---
days_limit = 30
start_date = (datetime.now() - timedelta(days=days_limit)).strftime('%Y-%m-%d')

# --- 4. Build query ---
query = f"""
SELECT {', '.join(relevant_columns)}
FROM complaints
WHERE created_date >= '{start_date}'
"""

# --- 5. Load data into a DataFrame ---
df = pd.read_sql(query, engine)

# --- 6. Basic cleaning ---
df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
df['city'] = df['city'].fillna('UNKNOWN')
df['incident_zip'] = df['incident_zip'].fillna('00000')

# --- 7. Set plot style ---
sns.set(style="whitegrid")

# --- 8. Complaints by City ---
plt.figure(figsize=(12, 6))
top_cities = df['city'].value_counts().nlargest(10)
sns.barplot(x=top_cities.index, y=top_cities.values, palette="Blues_d")
plt.title("Top 10 Cities by Complaint Volume")
plt.ylabel("Number of Complaints")
plt.xlabel("City")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- 9. Complaints by ZIP Code ---
plt.figure(figsize=(12, 6))
top_zips = df['incident_zip'].value_counts().nlargest(10)
sns.barplot(x=top_zips.index, y=top_zips.values, palette="Greens_d")
plt.title("Top 10 ZIP Codes by Complaint Volume")
plt.ylabel("Number of Complaints")
plt.xlabel("ZIP Code")
plt.tight_layout()
plt.show()

# --- 10. Complaints by Type ---
plt.figure(figsize=(12, 6))
top_types = df['complaint_type'].value_counts().nlargest(10)
sns.barplot(x=top_types.index, y=top_types.values, palette="Reds_r")
plt.title("Top 10 Complaint Types")
plt.ylabel("Number of Complaints")
plt.xlabel("Complaint Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
