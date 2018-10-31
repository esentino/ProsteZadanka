def policz_kotki(text):
    text = text.lower()
    return text.count("kot")
print(policz_kotki('Kotara to nie kotek, ale kotkiem jest Filemon'))
# zwróci 3