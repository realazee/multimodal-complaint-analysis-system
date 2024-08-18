-- Connect to the default database
\c postgres

-- Create the database
CREATE DATABASE aggregator;

-- Connect to the new database
\c aggregator

-- Drop the table if it exists
DROP TABLE IF EXISTS complaints CASCADE;

-- Create the table
CREATE TABLE complaints (
    id SERIAL PRIMARY KEY,
    input BYTEA,
    details TEXT NOT NULL,
    type VARCHAR(50) NOT NULL CHECK (type IN ('text', 'voice', 'image', 'video')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
