from server.config import app, db
from server.models import Workout, Exercise, WorkoutExercise
from datetime import date, timedelta
import random

with app.app_context():
    print("Clearing old seeds...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()
    
    print("Planting new seeds...")
    exercise_data = [
        ("Pushup", "Strength", False),
        ("Squat", "Strength", False),
        ("Running", "Cardio", False),
        ("Plank", "Core", False),
        ("Pullup", "Strength", True),
        ("Bench Press", "Strength", True),
        ("Deadlift", "Strength", True),
        ("Cycling", "Cardio", True),
        ("Burpees", "Cardio", False),
        ("Lunges", "Strength", False),
        ("Situps", "Core", False),
        ("Jump Rope", "Cardio", True),
    ]
    exercises = [Exercise(name=n, category=c, equipment_needed=e) for n,c,e in exercise_data]
    db.session.add_all(exercises)
    db.session.commit()

    workouts = []
    for i in range(12):
        w = Workout(date=date(2024, 1, 10)+timedelta(days=i), duration_minutes=30+i, notes=f"Workout {i+1}")
        workouts.append(w)
    db.session.add_all(workouts)
    db.session.commit()

    for w in workouts[:10]:
        we = WorkoutExercise(workout_id=w.id, exercise_id=random.choice(exercises).id, reps=10, sets=3)
        db.session.add(we)
    db.session.commit()
    print("Done seeding!")
