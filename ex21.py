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
        z=str(request.form['sentence'])
        words = z.split()
        words.sort()

        # # display the sorted words
        #
        # print("The sorted words are:")
        # for word in words:
        #     print(word)

        return "Wyrazy w kolejności alfabetycznej: {}".format(str(words))
    else:
        return formularz

app.run(debug=True)