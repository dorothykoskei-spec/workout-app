
from server.schema import (
    WorkoutSchema,
    ExerciseSchema,
    WorkoutExerciseSchema,
)


def test_workout_schema_exists():
    assert WorkoutSchema is not None


def test_exercise_schema_exists():
    assert ExerciseSchema is not None


def test_workout_exercise_schema_exists():
    assert WorkoutExerciseSchema is not None


def test_workout_schema_can_be_created():
    schema = WorkoutSchema()
    assert schema is not None


def test_exercise_schema_can_be_created():
    schema = ExerciseSchema()
    assert schema is not None


def test_workout_exercise_schema_can_be_created():
    schema = WorkoutExerciseSchema()
    assert schema is not None
