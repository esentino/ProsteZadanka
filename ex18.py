from flask import Flask,request

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def form():
    formularz="""
    <form action="/" method="POST">
        <label>Liczba1: </label>
        <input type="number" name="l1"/>
        <label>Liczba2: </label>
        <input type="number" name="l2"/>
        <label>Liczba3: </label>
        <input type="number" name="l3"/>
        <button type="submit">Pokaż największą</button>
    </form>
    """
    if request.method=="POST":
        lista=[]
        lista.append(int(request.form['l1']))
        lista.append(int(request.form['l2']))
        lista.append(int(request.form['l3']))
        max=0
        for i in lista:
            if i>max:
                max=i

        return "Największa liczba: {}".format(max)
    else:
        return formularz

app.run(debug=True)