from flask import request, make_response
from server.config import app, db
from server.models import Workout, Exercise, WorkoutExercise
from server.schema import workout_schema, workouts_schema, exercise_schema, exercises_schema, workout_exercise_schema
from marshmallow import ValidationError
from datetime import datetime

@app.route('/')
def home():
    return "Gym API is working!"

# GET method for all workouts
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return make_response(workouts_schema.dump(workouts), 200)

# GET workout by id
@app.route('/workouts/<int:id>', methods=['GET'])
def get_one_workout(id):
    workout = Workout.query.filter_by(id=id).first()
    if not workout:
        return make_response({"error": "Workout not found"}, 404)
    return make_response(workout_schema.dump(workout), 200)

# POST workouts
@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()
    try:
        
        validated_data = workout_schema.load(data)
        new_workout = Workout(**validated_data)
        db.session.add(new_workout)
        db.session.commit()
        return make_response(workout_schema.dump(new_workout), 201)
    except ValidationError as err:
        return make_response({"errors": err.messages}, 400)
    except Exception as e:
        return make_response({"errors": [str(e)]}, 400)

# DELETE workout by id
@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.filter_by(id=id).first()
    if not workout:
        return make_response({"error": "Workout not found"}, 404)
    db.session.delete(workout)
    db.session.commit()
    return make_response({"message": "Workout deleted"}, 200)

# GET all exercises
@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return make_response(exercises_schema.dump(exercises), 200)

# GET exercise by id
@app.route('/exercises/<int:id>', methods=['GET'])
def get_one_exercise(id):
    exercise = Exercise.query.filter_by(id=id).first()
    if not exercise:
        return make_response({"error": "Exercise not found"}, 404)
    return make_response(exercise_schema.dump(exercise), 200)

# POST exercise
@app.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()
    try:
  
        validated_data = exercise_schema.load(data)
        new_ex = Exercise(**validated_data)
        db.session.add(new_ex)
        db.session.commit()
        return make_response(exercise_schema.dump(new_ex), 201)
    except ValidationError as err:
       
        return make_response({"errors": err.messages}, 400)
    except Exception as e:
        return make_response({"errors": [str(e)]}, 400)

# DELETE exercise by id
@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.filter_by(id=id).first()
    if not exercise:
        return make_response({"error": "Exercise not found"}, 404)
    db.session.delete(exercise)
    db.session.commit()
    return make_response({"message": "Exercise deleted"}, 200)

# POST add exercise to workout
@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    workout = Workout.query.filter_by(id=workout_id).first()
    exercise = Exercise.query.filter_by(id=exercise_id).first()
    
    if not workout or not exercise:
        return make_response({"error": "Workout or Exercise not found"}, 404)
    
    data = request.get_json()
    try:
        validated_data = workout_exercise_schema.load({**data, "workout_id": workout_id, "exercise_id": exercise_id})
        we = WorkoutExercise(**validated_data)
        db.session.add(we)
        db.session.commit()
        return make_response(workout_exercise_schema.dump(we), 201)
    except ValidationError as err:
        return make_response({"errors": err.messages}, 400)
    except Exception as e:
        return make_response({"errors": [str(e)]}, 400)

if __name__ == '__main__':
    app.run(port=5555, debug=True)