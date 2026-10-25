import server.app
from server.config import app


def test_app_exists():
    assert app is not None


def test_app_runs():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code in [200, 404]


def test_workouts_endpoint():
    with app.test_client() as client:
        response = client.get("/workouts")
        assert response.status_code == 200


def test_exercises_endpoint():
    with app.test_client() as client:
        response = client.get("/exercises")
        assert response.status_code == 200


def test_missing_workout():
    with app.test_client() as client:
        response = client.get("/workouts/999999")
        assert response.status_code == 404


def test_missing_exercise():
    with app.test_client() as client:
        response = client.get("/exercises/999999")
        assert response.status_code == 404
