# Pharma AI — Database

## Overview

This directory contains the SQL schema and setup instructions for the Pharma AI project's database.

We use MariaDB/MySQL for storing application data. Every team member runs their own local database, while the database schema and connection code are shared through GitHub.

## Directory Structure

```text
database/
├── schema.sql
└── README.md
```

- `schema.sql` — Defines the database tables, columns, relationships, constraints, and indexes.
- `README.md` — Documents database setup and usage.

## Database Configuration

Database connection settings are stored in the project's root `.env` file.

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=pharma_ai
DB_USER=pharma_user
DB_PASSWORD=your_local_password
```

Each team member must configure these values according to their local database server.

The `.env.example` file in the project root provides a template for these settings. Never commit actual credentials to GitHub.

## Database Schema (needs to be done)

Write SQL commands for creating and modifying the project's database structure in `schema.sql`.

The schema will contain the tables required by the application, such as:

- Users
- Medicines
- Inventory
- Orders
- Prescriptions
- Purchase History
- Refill Alerts

Define primary keys, foreign keys, data types, constraints, and indexes as required.

## Python Database Connection (already done in src/backend/db.py just change the credintals like password and keep the table name and user same)

The Python connection code belongs in:

```text
src/Backend/db.py
```

The backend uses SQLAlchemy, PyMySQL, and python-dotenv to connect to the database using the settings in `.env`.

Python dependencies are managed through the project's root `requirements.txt`.

## Setup Instructions (mariadb i am using you can use mysql)

### 1. Install and start MariaDB or MySQL

Install a compatible database server and ensure it is running.

### 2. Create the database and application user

Open your database terminal and execute:

```sql
CREATE DATABASE pharma_ai;

CREATE USER 'pharma_user'@'localhost'
IDENTIFIED BY 'your_local_password';

GRANT ALL PRIVILEGES ON pharma_ai.*
TO 'pharma_user'@'localhost';
```

Use your own password and credentials.

### 3. Configure environment variables

From the project root:

```bash
cp .env.example .env
```

Update `.env` with your local database credentials.

### 4. Install Python dependencies

Activate your virtual environment and run:

```bash
pip install -r requirements.txt
```

### 5. Create the tables

From the project root, execute:

```bash
mariadb -u pharma_user -p pharma_ai < database/schema.sql
```

For MySQL, use the `mysql` command instead of `mariadb`.

Ensure `schema.sql` contains the table definitions for the project.

## Team Collaboration

The database schema and Python connection code are shared through GitHub. The actual database and credentials remain local to each team member.

When new tables or structural changes are introduced, update `schema.sql` or add database migrations and communicate the changes to the team.

Each team member must apply the required schema changes to their own database.

## Security

- Keep `.env` and the virtual environment out of GitHub.
- Commit `.env.example` with placeholder values.
- Never hardcode database credentials in Python source files.
- Never store user passwords as plain text.
