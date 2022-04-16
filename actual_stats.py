def stats_save_to_file():
    file = open('saves/stats.txt', 'w')
    for stat in stats.keys():
        file.write(str(stats[stat]) + '\n')
    file.close()

def stats_load_from_file():
    saved = open('saves/stats.txt')
    lst = list(saved)
    stats['wins'] = int(lst[0][:-1])
    stats['kills'] = int(lst[1][:-1])
    stats['playtime'] = int(lst[2][:-1])
    saved.close()

stats = dict(wins = 0, kills = 0, playtime = 0)
