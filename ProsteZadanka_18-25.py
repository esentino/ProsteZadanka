
import statistics

# Zadanie 18 FLASK

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def form():
    formularz = """
    <form action ="/" method="POST">
        <label>Podaj pierwsza liczbe</label>
        <input type="number" name="first">
        <label>Podaj druga liczbe</label>
        <input type="number" name="second">
        <label>Podaj trzecia liczbe</label>
        <input type="number" name="third">
        <button type="submit">Wyslij</button>
    </form>
    
    """

    if request.method == "POST":
        result = max(int(request.form['first']), int(request.form['second']), int(request.form['third']))
        return f"Najwieksza z podanych liczb to {result}"
    else:
        return formularz

app.run(debug=True)


# Zadanie 19 FLASK




# Zadanie 20

def check_surname(nazwisko):
    if len(nazwisko) < 3:
        raise ValueError("Za krotkie nazwisko!")
    elif ' ' in nazwisko:
        raise ValueError("Spacja w nazwisku!")
    elif not nazwisko == nazwisko.title():
        raise ValueError("Nie zaczyna sie wielka litera!")
    else:
        return True

print(check_surname('Nowak'))

# Zadanie 21 FLASK



# Zadanie 22

def change_letters(text):
    empty = ''
    for i in text:
        if i.isupper():
            empty += i.lower()
        if i.islower():
            empty += i.upper()
        if i == ' ':
            empty += i
    return empty


tekst = 'heheh Jajaja '
print(change_letters(tekst))


# Zadanie 23

def small_letters(text):
    empty = ''
    for i in text:
        if i.islower() or i == ' ':
            empty += i
    return empty

print(small_letters(tekst))


# Zadanie 24
def medjana(lista):
    med = statistics.median(lista)
    return med

example = [2,4,4,2,5]

print(medjana(example))

# Zadanie 25

def diff_avg_medjana(lista):
    z = medjana(lista)
    o = statistics.mean(lista)
    return o - z

print(diff_avg_medjana(example))

