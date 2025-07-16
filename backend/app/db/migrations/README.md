# Database Migrations

Place Alembic or SQL migration scripts here for schema setup and updates.

## 001_create_users_table.sql
- Creates the users table with fields: email, hashed_password, full_name, phone_number, age_group, gender, location, language, created_at.
- phone_number, age_group, gender, and location added for richer user profiling. 