from marshmallow import Schema, fields, validates, ValidationError

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool()

    @validates('name')
    def validate_name(self, value):
        if not value or not value.strip():
            raise ValidationError('Name cannot be empty.')
    
    @validates('category')
    def validate_category(self, value):
        if len(value) < 3:
            raise ValidationError('Category must be at least 3 characters.')

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    exercise = fields.Nested(ExerciseSchema, dump_only=True)

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()
    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema), dump_only=True)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)