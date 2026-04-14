import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# --- 1. Connect to PostgreSQL ---
engine = create_engine("postgresql+psycopg2://postgres:9890@localhost:5432/nyc_data")

# Set plot style
sns.set(style="whitegrid")

# --- 2. Load complaints from DB ---
query = """
SELECT 
    complaint_type, borough, city, status, created_date
FROM complaints
WHERE created_date >= CURRENT_DATE - INTERVAL '30 days';
"""

df = pd.read_sql(query, engine)

# --- 3. Complaints by Borough ---
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='borough', order=df['borough'].value_counts().index, palette='Blues_d')
plt.title("Complaints by Borough (Last 30 Days)")
plt.xlabel("Borough")
plt.ylabel("Number of Complaints")
plt.tight_layout()
plt.savefig("complaints_by_borough.png")
plt.close()

# --- 4. Top 10 Complaint Types ---
plt.figure(figsize=(12, 6))
top_types = df['complaint_type'].value_counts().head(10)
sns.barplot(x=top_types.values, y=top_types.index, palette='Reds_d')
plt.title("Top 10 Complaint Types (Last 30 Days)")
plt.xlabel("Number of Complaints")
plt.ylabel("Complaint Type")
plt.tight_layout()
plt.savefig("top_10_complaint_types.png")
plt.close()

# --- 5. Complaint Status Distribution ---
plt.figure(figsize=(7, 5))
status_counts = df['status'].value_counts()
sns.barplot(x=status_counts.index, y=status_counts.values, palette='Greens_d')
plt.title("Complaint Status Distribution")
plt.xlabel("Status")
plt.ylabel("Number of Complaints")
plt.tight_layout()
plt.savefig("complaint_status_distribution.png")
plt.close()

# --- 6. Complaints by City (Top 10) ---
plt.figure(figsize=(12, 6))
top_cities = df['city'].value_counts().head(10)
sns.barplot(x=top_cities.values, y=top_cities.index, palette='Purples_d')
plt.title("Complaints by City (Top 10, Last 30 Days)")
plt.xlabel("Number of Complaints")
plt.ylabel("City")
plt.tight_layout()
plt.savefig("complaints_by_city.png")
plt.close()

print("✅ Charts saved as PNG files!")
