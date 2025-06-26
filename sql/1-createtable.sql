CREATE TABLE IF NOT EXISTS complaints (
    unique_key TEXT PRIMARY KEY,
    created_date TIMESTAMP,
    agency TEXT,
    complaint_type TEXT,
    descriptor TEXT,
    location_type TEXT,
    incident_zip TEXT,
    borough TEXT
);

