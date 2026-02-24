
D= {
    "D1": "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza.",
    "D2": "Five pizza were ready, but 3 bourak burned!",
    "D3": "We only had 8 chamiyya, no pizza, and one tea.",
    "D4": "Is 6 too much? I ate nine bourak lol."
      }
def normalise(text):
   
    text = text.lower()

    punctuation = ".,!?;:\"'()"
    for p in punctuation:
        text = text.replace(p, "")

    mots = text.split()
   
    

    numero = {
        "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"
    }
    mots_normalises = []
   
    for mot in mots:
        if mot.isdigit():
            mots_normalises.append(numero.get(mot, mot))
        else:
            mots_normalises.append(mot)

    normalised_text = ' '.join(mots_normalises)
   
    return normalised_text

for key, value in D.items():
    print(f"{key} normalised: {normalise(value)}")
   
