def ranking_table(ranking):
    ranks = [str(rank) for rank in range(1, len(ranking) + 1)]
    names = [str(row[0]) for row in ranking]
    times = [row[1] for row in ranking]
    longest_rank_length = max([len(rank) for rank in ranks])
    longest_name_length = max([len(name) for name in names])
    lines = [f'{rank.rjust(longest_rank_length)} {name.ljust(longest_name_length)} {time:.2f}' for rank, name, time in zip(ranks, names, times)]
    return "\n".join(lines)