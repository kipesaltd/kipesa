CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    phone_number VARCHAR(32) UNIQUE,
    age_group VARCHAR(32),
    gender VARCHAR(32),
    location VARCHAR(255),
    language VARCHAR(8) DEFAULT 'en',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 