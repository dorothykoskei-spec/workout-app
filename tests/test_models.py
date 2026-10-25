from server.config import app
from server.models import Workout, Exercise, WorkoutExercise


def test_exercise_exists():
    with app.app_context():
        assert Exercise.query.count() >= 10


def test_workout_exists():
    with app.app_context():
        assert Workout.query.count() >= 10


def test_workout_exercise_relationship():
    with app.app_context():
        workout = Workout.query.first()

        assert workout is not None
        assert hasattr(workout, "exercises")
        assert len(workout.exercises) > 0


def test_workout_model_has_id():
    assert hasattr(Workout, "id")


def test_exercise_model_has_id():
    assert hasattr(Exercise, "id")


def test_workout_exercise_model_exists():
    assert WorkoutExercise is not None


def test_workout_exercise_foreign_keys():
    assert hasattr(WorkoutExercise, "workout_id")
    assert hasattr(WorkoutExercise, "exercise_id")

