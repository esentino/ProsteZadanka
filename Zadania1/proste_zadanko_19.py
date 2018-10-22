from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def zdanie():
    formularz = """
    <form action="/" method="POST"
        <label>Wpisz dowolne zdanie:</label><br>
        <input type="text" name="zdanie"><br>
        <button type="submit">Wyślij</button>
    </form>
    """
    if request.method == 'POST':
        zdanko = request.form['zdanie']
        return "Twoje zdanie ma " + str(len(zdanko.split(' '))) + " słów."

    else:
        return formularz


app.run(debug=True)
