from flask import Flask, render_template
from connect import connect
from config import load_config

app = Flask(__name__)

def connect_to_db():
    config = load_config()
    return connect(config)

conn = connect_to_db()


@app.route('/')
def index():
    return render_template('index.html')

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

