from flask import Flask

app = Flask(__name__)

def hello():
    return "<br>Aadesh Lokhande"

@app.route('/')

def table():
    html = '<h1>Tables from 1 to 10</h1>'
    html += '<table border="1">'
    for i in range(1, 11):
        html += '<tr>'
        for j in range(1,11):
            html += f'<td>{i*j}</td>'
        html += '</tr>'
    html += '</table>'
    a = hello()
    html += a
    return html




if __name__ == '__main__':
    app.run(debug=True)
