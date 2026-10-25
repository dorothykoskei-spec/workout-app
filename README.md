# Workout Tracker API

## 1. Project Description

The Workout Tracker API is a backend application built using Flask, Flask-SQLAlchemy, Flask-Migrate, and Marshmallow.

It allows personal trainers to manage workouts and exercises.

### Features

- Create, view, and delete workouts.
- Create, view, and delete exercises.
- Add existing exercises to workouts.
- Store workout and exercise information in a database.
- Validate incoming data using Marshmallow.
- Manage database changes using Flask-Migrate.
- Use relationships to connect workouts and exercises.

A workout can contain multiple exercises, and the same exercise can be reused in different workouts.

## 2. Technologies Used

- Python 3.11
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- SQLite
- Pytest
- Pipenv

## 3. Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/dorothykoskei-spec/workout-app.git
cd workout-app
```


### Step 2: Install dependencies

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

### Step 3: Set up the database

From the project root, run:

```bash
pipenv run flask --app server.app db upgrade
```

This applies the existing database migrations.

If your database has not been initialized with migrations yet, initialize and create the initial migration before running the upgrade command.

### Step 4: Seed the database

From the project root, run:

```bash
PYTHONPATH=. pipenv run python -m server.seed
```

This runs the seed script to add sample workouts and exercises.


## 4. Running the Application

From the project root, run:

```bash
PYTHONPATH=. pipenv run flask --app server.app run --port 5555
```

The API will be available at:

http://127.0.0.1:5555

Keep the terminal running while using the API.

You can test the endpoints using Postman.

## 5. API Endpoints

### Workouts

| Method | Endpoint | Description |
|---|---|---|
| GET | `/workouts` | Returns all workouts. |
| GET | `/workouts/<id>` | Returns one workout by ID. |
| POST | `/workouts` | Creates a new workout. |
| DELETE | `/workouts/<id>` | Deletes a workout by ID. |

### Exercises

| Method | Endpoint | Description |
|---|---|---|
| GET | `/exercises` | Returns all exercises. |
| GET | `/exercises/<id>` | Returns one exercise by ID. |
| POST | `/exercises` | Creates a new exercise. |
| DELETE | `/exercises/<id>` | Deletes an exercise by ID. |

### Workout and Exercise Relationship

| Method | Endpoint | Description |
|---|---|---|
| POST | `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` | Adds an existing exercise to an existing workout. |

## 6. Database and Migrations

The application uses SQLite to store workout and exercise records.

Flask-SQLAlchemy defines the database models and relationships.

Flask-Migrate manages database schema changes.

To apply existing migrations, run:

```bash
PYTHONPATH=. pipenv run flask --app server.app db upgrade
```

## 7. Testing

The project uses Pytest for automated testing.

### Test File Structure


tests/
├── test_app.py
├── test_models.py
└── test_schema.py


### What the Tests Cover

- **Application tests (`test_app.py`):** Check API endpoints, HTTP responses, and handling of missing workouts and exercises.
- **Model tests (`test_models.py`):** Check seeded records, model fields, foreign keys, and workout-exercise relationships.
- **Schema tests (`test_schema.py`):** Check that Marshmallow schemas exist and can be initialized.

### Run the Tests

From the project root, run:

```bash
PYTHONPATH=. pipenv run python -m pytest tests -v
```

So my  tests check only the behavior implemented in their assertions. Additional tests are needed to verify invalid input, successful creation and deletion, and Marshmallow validation rules.

## 8. Dependencies

The project uses Pipenv to manage dependencies.

Main dependencies:

- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow

## 9. Project Purpose

The purpose of the Workout Tracker API is to demonstrate:

- Flask REST API development.
- Database models and relationships.
- Data validation with Marshmallow.
- Database migrations.
- Automated testing with Pytest.
- CRUD operations for workouts and exercises.
