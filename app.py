from flask import Flask, redirect, render_template, request, url_for
from connect import connect
from config import load_config
from voice import audio_to_speech
from textprocessing import process_text
from image import text_in_image
from video import video_to_text
import os

app = Flask(__name__)

def connect_to_db():
    config = load_config()
    try:
        return connect(config)
    except Exception as e:
        print(f"Database connection error: {e}")
        return None
    
conn = connect_to_db()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    user_text = request.form.get('userText')
    file = request.files.get('fileUpload')
    complaint_type = request.form.get('complaintType')  # Determines the type of complaint

    if user_text and complaint_type == 'text':
        processed_data = process_text(user_text).text
        cur = conn.cursor()
        cur.execute("INSERT INTO complaints (details, type) VALUES (%s, %s)", (processed_data, complaint_type))
        conn.commit()

    if file:
        if complaint_type == 'voice':
            processed_data = process_text(audio_to_speech(file)).text
        elif complaint_type == 'image':
            processed_data = process_text(text_in_image(file)).text
        elif complaint_type == 'video':
            processed_data = process_text(video_to_text(file)).text
        
        cur = conn.cursor()
        cur.execute("INSERT INTO complaints (details, type) VALUES (%s, %s)", (processed_data, complaint_type))
        conn.commit()

    return redirect(url_for('complaints'))

@app.route('/delete_complaint/<int:id>', methods=['POST'])
def delete_complaint(id):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM complaints WHERE id = %s", (id,))
        conn.commit()
        return redirect(url_for('complaints'))
    except Exception as e:
        print(f"Error deleting complaint: {e}")
        return redirect(url_for('complaints'))


@app.route('/complaints')
def complaints():
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaints")
    complaints = cur.fetchall()
    return render_template('complaints.html', complaints=complaints)

@app.route('/complaints/<int:id>')
def complaint(id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaints WHERE id = %s", (id,))
    complaint = cur.fetchone()
    return render_template('complaint.html', complaint=complaint)

if __name__ == '__main__':
    app.run(debug=True)
    conn = connect_to_db()
    if conn:
        print("Database connection successful")
    else:
        print("Database connection failed")

