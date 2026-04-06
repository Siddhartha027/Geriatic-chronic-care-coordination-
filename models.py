from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    medical_history = db.Column(db.Text)
    diseases = db.Column(db.String(200))

class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    dosage = db.Column(db.String(50))
    time = db.Column(db.Time)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bp_systolic = db.Column(db.Integer)
    bp_diastolic = db.Column(db.Integer)
    sugar = db.Column(db.Float)
    date = db.Column(db.DateTime, default=db.func.now())
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))  # prescription, report, note
    content = db.Column(db.Text)
    date = db.Column(db.DateTime, default=db.func.now())
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))