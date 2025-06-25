/* DROP TABLE IF EXISTS complaints;*/

CREATE TABLE complaints (
    unique_key TEXT PRIMARY KEY,
    created_date TIMESTAMP,
    agency TEXT,
    agency_name TEXT,
    complaint_type TEXT,
    descriptor TEXT,
    location_type TEXT,
    incident_zip TEXT,
    incident_address TEXT,
    street_name TEXT,
    cross_street_1 TEXT,
    cross_street_2 TEXT,
    intersection_street_1 TEXT,
    intersection_street_2 TEXT,
    address_type TEXT,
    city TEXT,
    landmark TEXT,
    status TEXT,
    resolution_action_updated_date TIMESTAMP,
    community_board TEXT,
    bbl TEXT,
    borough TEXT,
    x_coordinate_state_plane TEXT,
    y_coordinate_state_plane TEXT,
    open_data_channel_type TEXT,
    park_facility_name TEXT,
    park_borough TEXT,
    latitude TEXT,
    longitude TEXT,
    ":@computed_region_efsh_h5xi" TEXT,
    ":@computed_region_f5dn_yrer" TEXT,
    ":@computed_region_yeji_bk3q" TEXT,
    ":@computed_region_92fq_4b7q" TEXT,
    ":@computed_region_sbqj_enih" TEXT,
    ":@computed_region_7mpf_4k6g" TEXT,
    "location.latitude" TEXT,
    "location.longitude" TEXT,
    "location.human_address" TEXT,
    closed_date TIMESTAMP,
    resolution_description TEXT
);

/*Added to columns 'vehicle_type' and 'complaint_type' (ALTER TABLE complaints ADD COLUMN vehicle_type TEXT;)
Dropping a few unwanted columnt*/

ALTER TABLE complaints
DROP COLUMN agency,
DROP COLUMN street_name,
DROP COLUMN cross_street_1,
DROP COLUMN cross_street_2,
DROP COLUMN intersection_street_1,
DROP COLUMN intersection_street_2,
DROP COLUMN address_type,
DROP COLUMN landmark,
DROP COLUMN community_board,
DROP COLUMN bbl,
DROP COLUMN x_coordinate_state_plane,
DROP COLUMN y_coordinate_state_plane,
DROP COLUMN open_data_channel_type,
DROP COLUMN park_facility_name,
DROP COLUMN park_borough,
DROP COLUMN borough,
DROP COLUMN latitude,
DROP COLUMN longitude,
DROP COLUMN ":@computed_region_efsh_h5xi",
DROP COLUMN ":@computed_region_f5dn_yrer",
DROP COLUMN ":@computed_region_yeji_bk3q",
DROP COLUMN ":@computed_region_92fq_4b7q",
DROP COLUMN ":@computed_region_sbqj_enih",
DROP COLUMN ":@computed_region_7mpf_4k6g",
DROP COLUMN "location.latitude",
DROP COLUMN "location.longitude",
DROP COLUMN "location.human_address",
DROP COLUMN facility_type,
DROP COLUMN vehicle_type;

ALTER TABLE complaints /*dropping rest unwanted -column*/
DROP COLUMN borough,
DROP COLUMN latitude,
DROP COLUMN longitude;



