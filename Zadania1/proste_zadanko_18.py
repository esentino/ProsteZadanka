from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def trzy_liczby():
    formularz = """
    <form action="/" method="POST"
        <label>Podaj pierwszą liczbę</label>
        <input type="number" name="first"><br>
        <label>Podaj drugą liczbę</label>
        <input type="number" name="second"><br>
        <label>Podaj trzecią liczbę</label>
        <input type="number" name="third"><br>
        <button type="submit">Wyślij</button>
    </form>
    """
    if request.method == 'POST':
        try:
            first = float(request.form['first'])
            second = float(request.form['second'])
            third = float(request.form['third'])
        except ValueError:
            return "Podaj liczby" + formularz
        maximal = first
        if second > maximal:
            maximal = second
        if third > maximal:
            maximal = third
        return "Największa z podanych liczb to " + str(maximal)
    else:
        return formularz


app.run(debug=True)
