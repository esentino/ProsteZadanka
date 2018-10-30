from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def slowa():
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

        zdanko = zdanko.replace(",", '')    # zamiana przecinków na nic
        zdanko = zdanko.replace('.', '')    # zamiana kropek na nic
        zdanko = zdanko.split(' ')          # podział stringa na listę słów
        zdanko.sort()                       # sortowanie listy
        return "<br>".join(zdanko) + "<br><a href='/'>Ponownie</a>"

    else:
        return formularz


app.run(debug=True)
