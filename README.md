# Healthcare Management System for Elderly Patients

A simple Flask web application for managing healthcare information for elderly patients.

## Features

- **Dashboard**: View patient summary, medications, recent alerts, and reminders.
- **Patient Details**: Add or edit patient information.
- **Medicine Reminder**: Add medications with dosage and time, get reminders.
- **Health Alerts**: Manually input BP and sugar levels, receive alerts if out of range.
- **Caregiver View**: Special dashboard for caregivers to view all patient data.
- **Medical Records**: View prescriptions, reports, and doctor notes.
- **Emergency Buttons**: Quick access to call doctor or trigger SOS.

## Installation

1. Install Python 3.7 or higher.
2. Clone or download the project.
3. Navigate to the project directory.
4. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

## Running the Application

Run the application with:

```
python app.py
```

Open your browser and go to `http://127.0.0.1:5000/`

## Usage

- Start at the dashboard.
- Add patient details if needed.
- Add medicines for reminders.
- Input health data to check for alerts.
- Use caregiver view for comprehensive overview.
- Access emergency features as needed.

## Notes

- Designed for simplicity and ease of use for elderly users.
- Uses SQLite database.
- No authentication implemented (single patient assumed).
- Reminders check current time on page load or refresh.