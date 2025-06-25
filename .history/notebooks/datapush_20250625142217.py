import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timedelta

# --- 1. Create the database engine ---
engine = create_engine("postgresql+psycopg2://postgres:9890@localhost:5432/nyc_data")

# --- 2. Calculate the date for past 7 days ---
seven_days_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%S')

# --- 3. Build the API URL ---
url = f"https://data.cityofnewyork.us/resource/erm2-nwe9.json?$limit=10000&$where=created_date >= \"{seven_days_ago}\""

# --- 4. Send the API request ---
response = requests.get(url)

if response.status_code == 200:
    print("✅ Data fetched successfully!")
    data = response.json()

    # --- 5. Normalize nested JSON (location is nested) ---
    df = pd.json_normalize(data)
    
    # --- 6.Getting 40 columns data from api. Defining relevant columns to keep rest drop ---
    relevant_columns = [
        'unique_key',
        'created_date',
        'agency_name',
        'complaint_type',
        'descriptor',
        'location_type',
        'incident_zip',
        'incident_address',
        'city',
        'status',
        'resolution_action_updated_date',
        'closed_date',
        'resolution_description',     
    ]

    # --- 7. Filter the DataFrame to only keep relevant columns ---
    # Some columns like 'latitude' and 'longitude' may not exist directly
    # So let's check which of them are available first
    existing_columns = [col for col in relevant_columns if col in df.columns]
    df_filtered = df[existing_columns]
    
    # --- 8. Store filtered data to PostgreSQL ---
    if not df_filtered.empty:
        df_filtered.to_sql("complaints", engine, if_exists="append", index=False)
        print(f"✅ Inserted {len(df_filtered)} records into PostgreSQL!")
    else:
        print("⚠️ No data to insert into PostgreSQL.")

else:
    print(f"❌ Failed to fetch data. Status code: {response.status_code}")























'''
### Couldn't figureout why below code didn't work.

import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timedelta

# --- 1. Create the database engine ---
engine = create_engine("postgresql+psycopg2://postgres:9890@localhost:5432/nyc_data")

# --- 2. Calculate the date for past 7 days ---
seven_days_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%S')
# --- 3. Build the API URL ---
url = f"https://data.cityofnewyork.us/resource/erm2-nwe9.json?$limit=2&$where=created_date >= '{seven_days_ago}'"

# --- 4. Send the API request ---
response = requests.get(url)

if response.status_code == 200:
    print("✅ Data fetched successfully!")
    data = response.json()

    # --- 5. Normalize nested JSON (location is nested) ---
    df = pd.json_normalize(data)
        # --- 10. Push the DataFrame to PostgreSQL ---
df.to_sql("complaints", engine, if_exists="append", index=False, method="multi")
print("✅ Data inserted into PostgreSQL successfully!")

else:print(f"❌ Failed to fetch data. Status code: {response.status_code}")


    # --- 6. Select and rename columns to match your database table ---
    final_columns = [
        "unique_key", "created_date", "agency", "agency_name", "complaint_type",
        "descriptor", "location_type", "incident_zip", "incident_address", "street_name",
        "cross_street_1", "cross_street_2", "intersection_street_1", "intersection_street_2",
        "address_type", "city", "landmark", "status", "resolution_action_updated_date",
        "community_board", "bbl", "borough", "x_coordinate_state_plane", "y_coordinate_state_plane",
        "open_data_channel_type", "park_facility_name", "park_borough", "latitude", "longitude",
        "location", ":@computed_region_efsh_h5xi", ":@computed_region_f5dn_yrer",
        ":@computed_region_yeji_bk3q", ":@computed_region_92fq_4b7q", ":@computed_region_sbqj_enih",
        ":@computed_region_7mpf_4k6g"
    ]

    # --- 7. Add missing columns if not returned in API (to avoid errors) ---
    for col in final_columns:
        if col not in df.columns:
            df[col] = None  # Fill missing with None

    # --- 8. Keep only those columns ---
    df = df[final_columns]

    # --- 9. Convert date columns to proper format ---
    df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")
    df["resolution_action_updated_date"] = pd.to_datetime(df["resolution_action_updated_date"], errors="coerce")

'''