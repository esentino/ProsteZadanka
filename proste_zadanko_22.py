from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def zamiana():
    formularz = """
    <form action="/" method="POST"
        <label>Wpisz dowolne zdanie:</label><br>
        <input type="text" name="zdanie"><br>
        <button type="submit">Wyślij</button>
    </form>
    """
    if request.method == 'POST':
        zdanko = request.form['zdanie']

        if not zdanko:
            return "Nic nie wpisałeś." + formularz

        zdanie = ""
        zdanko = list(zdanko)
        for i in range(len(zdanko)):
            if zdanko[i].isupper():
                zdanko[i] = zdanko[i].lower()
            elif zdanko[i].islower():
                zdanko[i] = zdanko[i].upper()
            zdanie += zdanko[i]

        return zdanie + "<br><a href='/'>Ponownie</a>"

    else:
        return formularz


app.run(debug=True)
