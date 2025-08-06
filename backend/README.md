# Kipesa Backend

This directory contains the FastAPI backend for the Kipesa finance platform.

## Structure

- `app/` - Main application code (APIs, services, models, config)
- `tests/` - Unit and integration tests
- `alembic/` - Database migrations (if used for local dev)
- `.env.example` - Example environment variables
- `requirements.txt` - Python dependencies

## Initial Setup Plan

1. Modular FastAPI app with async support
2. Supabase (PostgreSQL) integration
3. JWT authentication, password hashing, rate limiting, CORS
4. Core API endpoints (auth, chatbot, calculators, finance, content)
5. Error handling, logging, and config management
6. Documentation and type hints throughout 

---

## Backend Documentation

### 1. Project Structure

- `app/` - Main FastAPI application code
  - `api/` - Modular API routers (auth, chatbot, calculators, finance, content)
  - `core/` - Core config, logging, error handling, rate limiting, caching
  - `db/` - Database models, migrations, Supabase integration, real-time
  - `schemas/` - Pydantic models for request/response validation
  - `services/` - Business logic (auth, chatbot, calculators, etc.)
  - `tasks/` - Background tasks (async jobs, heavy calculations)
  - `main.py` - FastAPI app entrypoint
- `tests/` - Unit and integration tests
- `alembic/` - (Optional) DB migrations if using Alembic
- `.env.example` - Example environment variables
- `requirements.txt` - Python dependencies

### 2. Environment Setup

1. **Install Python 3.9+**
2. **Install dependencies:**
   ```sh
   python3 -m pip install -r backend/requirements.txt
   ```
3. **Set up environment variables:**
   - Copy `.env.example` to `.env` and fill in:
     - `OPENAI_API_KEY` (your OpenAI API key from https://platform.openai.com/api-keys)
     - `SECRET_KEY` (generate a secure random string)
     - `SUPABASE_URL` (from Supabase project dashboard)
     - `SUPABASE_KEY` (service_role key from Supabase API settings)
     - `DATABASE_URL` (use `postgresql+asyncpg://...` for async SQLAlchemy)
     - `REDIS_URL` (Redis connection string for caching)

### 3. Running the Backend

- **Development:**
  ```sh
  cd backend
  uvicorn app.main:app --reload
  ```
- **Production:**
  - Use a production ASGI server (e.g., Uvicorn, Gunicorn with Uvicorn workers)

### 4. Testing

- **Run all tests:**
  ```sh
  python3 -m pytest backend/tests
  ```
- **Lint and format:**
  ```sh
  python3 -m black backend
  python3 -m isort backend
  python3 -m flake8 backend
  ```

### 5. Key Architecture Notes

- **Async/await** throughout for high performance
- **Modular routers** for separation of concerns
- **Supabase integration** for real-time, auth, and storage
- **Direct PostgreSQL access** via async SQLAlchemy for advanced queries and migrations
- **Security:** JWT auth, password hashing, input validation, rate limiting, CORS
- **Performance:** Caching, background tasks, optimized queries
- **Error handling:** Centralized, structured JSON errors, logging with Loguru
- **Localization:** Bilingual support (English/Swahili) and cultural adaptation

### 6. Troubleshooting

- Ensure all required environment variables are set in `.env`
- Use `postgresql+asyncpg://` for `DATABASE_URL` (not just `postgresql://`)
- Install all dependencies listed in `requirements.txt`
- For Pydantic V2 warnings, consider migrating to `@field_validator` and `ConfigDict` in the future

---

For further questions or to extend the backend, see the code comments and modular structure for guidance. 