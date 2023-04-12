from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)

app.secret_key = 'secret'

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def name():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')
    
@app.route('/results')
def render():
    return render_template('submit.html')


if __name__ =="__main__":
    app.run(debug=True, port=5001)