from data import is_testing


def Stat_error(select_num):
    print("Please input a number from the list of rolled numbers")
    select_num = 0

def pick_stat(stat_list):
    print(stat_list)
    select = input("Please select a stat to set. ")
    select = select.upper()
    if select not in stat_list:
        print("not a valid stat")
        pick_stat(stat_list)
    return select

def pick_number(stats):
    select_num = 0
    print(stats[0:-1])
    while select_num == 0:
        select_num = input("what roll do you want to use ")
        try:
            select_num = int(select_num)
            if select_num not in stats:
                Stat_error(select_num)
                continue
        except ValueError:
            Stat_error(select_num)
            continue
        return select_num

def select_stats(stats, dicts, stat_list):
    select = pick_stat(stat_list)
    select_num = pick_number(stats)
    if dicts[select] == 0:
        dicts.update({select: select_num})
        stats.remove(select_num)
        testing = is_testing.is_testing()
        if testing == True:
            return dicts
    else:
        print("This stat has already been set.\n"
              "Please select another stat.")

def all_stats(stats, dicts):
    stat_list = list(dicts.keys())
    stats.append("END")
    while stats[0] != "END":
        select_stats(stats,dicts, stat_list)
    return dicts
