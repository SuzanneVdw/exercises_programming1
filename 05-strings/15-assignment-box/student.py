def box(string):
    top_bottom = "+" + "-" * (len(string)+2) + "+"
    return top_bottom + "\n" + "| " + string + " |" + "\n" + top_bottom