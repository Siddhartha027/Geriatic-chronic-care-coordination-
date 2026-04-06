from flask import Flask, render_template, request, redirect, url_for
from models import db, Patient, Medicine, Alert, MedicalRecord
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()
    if not Patient.query.first():
        patient = Patient(name="John Doe", age=70, medical_history="Hypertension diagnosed 5 years ago", diseases="Diabetes, Hypertension")
        db.session.add(patient)
        db.session.commit()

@app.route('/')
def dashboard():
    patient = Patient.query.first()
    medicines = Medicine.query.filter_by(patient_id=patient.id).all()
    alerts = Alert.query.filter_by(patient_id=patient.id).order_by(Alert.date.desc()).limit(5).all()
    # Check for reminders
    now = datetime.datetime.now().time()
    reminders = [m for m in medicines if m.time.hour == now.hour and m.time.minute == now.minute]
    return render_template('index.html', patient=patient, medicines=medicines, alerts=alerts, reminders=reminders)

@app.route('/patient', methods=['GET', 'POST'])
def patient_details():
    patient = Patient.query.first()
    if request.method == 'POST':
        patient.name = request.form['name']
        patient.age = int(request.form['age'])
        patient.medical_history = request.form['history']
        patient.diseases = request.form['diseases']
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('patient_details.html', patient=patient)

@app.route('/add_medicine', methods=['GET', 'POST'])
def add_medicine():
    if request.method == 'POST':
        name = request.form['name']
        dosage = request.form['dosage']
        time_str = request.form['time']
        time = datetime.datetime.strptime(time_str, '%H:%M').time()
        patient_id = Patient.query.first().id
        medicine = Medicine(name=name, dosage=dosage, time=time, patient_id=patient_id)
        db.session.add(medicine)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_medicine.html')

@app.route('/add_alert', methods=['GET', 'POST'])
def add_alert():
    alert_msg = ""
    if request.method == 'POST':
        bp_s = int(request.form['bp_s'])
        bp_d = int(request.form['bp_d'])
        sugar = float(request.form['sugar'])
        patient_id = Patient.query.first().id
        alert = Alert(bp_systolic=bp_s, bp_diastolic=bp_d, sugar=sugar, patient_id=patient_id)
        db.session.add(alert)
        db.session.commit()
        # Check for alerts
        if bp_s > 140 or bp_d > 90:
            alert_msg = "BP is HIGH"
        elif bp_s < 90 or bp_d < 60:
            alert_msg = "BP is LOW"
        if sugar > 180:
            alert_msg += " Sugar is HIGH"
        elif sugar < 70:
            alert_msg += " Sugar is LOW"
    return render_template('add_alert.html', alert_msg=alert_msg)

@app.route('/caregiver')
def caregiver():
    patient = Patient.query.first()
    medicines = Medicine.query.filter_by(patient_id=patient.id).all()
    alerts = Alert.query.filter_by(patient_id=patient.id).all()
    records = MedicalRecord.query.filter_by(patient_id=patient.id).all()
    return render_template('caregiver.html', patient=patient, medicines=medicines, alerts=alerts, records=records)

@app.route('/records')
def records():
    records = MedicalRecord.query.filter_by(patient_id=Patient.query.first().id).all()
    return render_template('records.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)