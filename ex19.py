from flask import Flask,request

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def form():
    formularz="""
    <form action="/" method="POST">
        <label>Wpisz zdanie: </label>
        <input type="text" name="sentence"/>
        <button type="submit">Podaj długość</button>
    </form>
    """
    if request.method=="POST":
        z=request.form['sentence']
        l=len(z)

        return "Długość zdania: {}".format(str(l))
    else:
        return formularz

app.run(debug=True)