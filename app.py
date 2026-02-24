from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event = request.form['event']
        return f'<h2>Thank you {name} for registering for {event}</h2><p>Confirmation sent to {email}</p>'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)