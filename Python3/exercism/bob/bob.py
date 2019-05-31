def response(hey_bob):
    # Strips trailing whitespace.
    phrase = hey_bob.strip()
    
    if phrase == "":
        return "Fine. Be that way!"
    elif phrase.isupper():
        if phrase.endswith("?"):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    elif phrase.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
