from flask import Flask, request

app	= Flask(__name__)

@app.route("/form", methods=['GET','POST'])
def form():
    formularz = """
    <form action="/form" method="POST" >
        <label>Pierwsza liczba</label>
        <input type="number" name="first"/>
        <label>Druga liczba</label>
        <input type="number" name="second"/>
        <label>Trzecia liczba</label>
        <input type="number" name="third"/>
        <button type="submit">Wyslij</button>
    </form>
    """
    if request.method == "GET":
        return formularz
    if request.method == "POST":
        wynik = max(int(request.form['first']), int(request.form['second']), int(request.form['third']))
        return "Największa liczba to {}".format(wynik)

app.run(debug=True)