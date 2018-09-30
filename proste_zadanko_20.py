from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def nazwisko():
    formularz = """
    <form action="/" method="POST"
        <label>Podaj nazwisko:</label><br>
        <input type="text" name="surname"><br>
        <button type="submit">Wyślij</button>
    </form>
    """

    if request.method == 'POST':
        nazwisko = request.form['surname']
        if nazwisko[0].isupper() and len(nazwisko) >= 3 and (' ' not in nazwisko):
            return str(True) + "<br><a href='/'>Ponownie</a>"
        else:
            raise ValueError

    else:
        return formularz


app.run(debug=True)
