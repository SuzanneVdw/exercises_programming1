def ranking_table(ranking):
    final_table = ""
    rank_width = len(str(len(ranking) + 1))
    name_width = 1
    # Find longest name
    for i in range(0,len(ranking)):     
        if len(ranking[i][0]) > name_width:
            name_width = len(ranking[i][0])
    for i in range(0,len(ranking)):
        final_table += str(i+1).rjust(rank_width)
        final_table += " "
        final_table += ranking[i][0].ljust(name_width)
        final_table += " "
        final_table += f"{float(ranking[i][1]):.2f}"
        if i != len(ranking)-1:
            final_table += "\n"
    return final_table