CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE assets(
    id INTEGER PRIMARY KEY,
    asset_name VARCHAR(100),
    asset_tag VARCHAR(100) UNIQUE,
    asset_type VARCHAR(100),
    serial_number VARCHAR(100),
    status VARCHAR(50)
);

CREATE TABLE service_requests(
    id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    asset_id INTEGER,
    support_id INTEGER,
    issue_title VARCHAR(255),
    description TEXT,
    priority VARCHAR(50),
    status VARCHAR(50),
    resolution_date DATE
);
