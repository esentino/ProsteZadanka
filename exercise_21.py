from flask import Flask, request

app	= Flask(__name__)

@app.route("/form", methods=['GET','POST'])
def form():
    formularz = """
    <form action="/form" method="POST" >
        <label>Wpisz zdanie</label>
        <input type="text" name="first"/>
        <button type="submit">Wyslij</button>
    </form>
    """
    if request.method == "GET":
        return formularz
    if request.method == "POST":
        zdanie = str(request.form['first'])
        wyrazy = zdanie.split()
        wyrazy.sort()
        wynik = ' '.join(wyrazy)
        return wynik

app.run(debug=True)