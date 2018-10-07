import re

def policz_kotki(text):
    t=text.lower()
    k="kot"
    r=[m.start() for m in re.finditer(k, t)]
    return len(r)

print(policz_kotki('Kotara to nie kotek, ale kotkiem jest Filemon'))
# zwróci 3