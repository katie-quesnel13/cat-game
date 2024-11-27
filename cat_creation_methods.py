from name_lists import *
import random


def get_prefix(appearance):
    prefix_list = []
    prefix_list.extend(generic_names)
    eyesblue = True
    if " blue eyes" in appearance or " one blue eye" in appearance:
        applist = appearance.split()
        for i, w in enumerate(applist):
            if w == 'blue':
                if i + 1 < len(applist) and applist[i + 1] != 'eye' or applist[i + 1] != 'eyes':
                    eyesblue = False
                    break

    if " red " in appearance:
        prefix_list.extend(red_names)

    if "cream " in appearance:
        prefix_list.extend(cream_names)

    if "black " in appearance:
        prefix_list.extend(black_names)

    if "blue " in appearance and eyesblue is False:
        prefix_list.extend(blue_names)

    if "chocolate " in appearance:
        prefix_list.extend(chocolate_names)

    if "lilac " in appearance:
        prefix_list.extend(lilac_names)

    if "cinnamon " in appearance:
        prefix_list.extend(cinnamon_names)

    if "fawn " in appearance:
        prefix_list.extend(fawn_names)

    if " caramel " in appearance:
        prefix_list.extend(caramel_names)

    if " apricot " in appearance:
        prefix_list.extend(apricot_names)

    if " silver " in appearance:
        prefix_list.extend(silver_names)

    if " smoke " in appearance:
        prefix_list.extend(smoke_names)

    if "mackerel " in appearance:
        prefix_list.extend(mackerel_names)

    if "spotted " in appearance or "broken " in appearance:
        prefix_list.extend(spotted_names)

    if "classic " in appearance:
        prefix_list.extend(classic_names)

    if "tortie " in appearance:
        prefix_list.extend(tortie_names)

    if "dominant " in appearance:
        prefix_list.extend(white_names)

    if "pointed " in appearance:
        prefix_list.extend(pointed_names)

    if "tortie " in appearance and " spotting" in appearance:
        prefix_list.extend(calico_names)

    if "high white spotting" in appearance:
        prefix_list.extend(patched_names)
        prefix_list.extend(white_names)

    return random.choice(prefix_list)


def get_suffix(prefix, age):
    age = int(age)
    if age >= 12:
        suffix = prefix
        while str.lower(suffix) == str.lower(prefix):
            suffix = random.choice(name_list)
    elif 6 <= age < 12:
        suffix = 'paw'
    else:
        suffix = 'kit'

    return suffix


def random_genestring():
    fur = ["LL", "Ll", "ll"]
    gender = ["XOXO", "XOXo", "XoXo", "XOY", "XoY", "XOXO", "XOXo", "XoXo", "XOY", "XoY", "XOY", "XoY"]
    colour = ["BB", "Bb", "blB", "bb", "blb"]
    dilute = ["DD", "Dd", "dd", "Dd"]
    dilute_modifier = ["dmdm", "Dmdm", "dmDm", "DmDm", "dmdm", "dmdm", "dmdm", "dmdm"]
    solid = ['AA', 'Aa', 'aa', 'Aa']
    inhibitor = ["ii", "Ii", "iI", "II", "ii", "ii", "ii", "ii"]
    mackerel = ['McMc', 'Mcmc', 'mcmc', 'Mcmc']
    spotted = ['SpSp', 'Spsp', 'spsp']
    ticked = ['TaTa', 'Tata', 'tata', 'tata', 'tata', 'tata', 'tata', 'tata', 'tata', 'tata', 'tata', 'tata']
    pointed = ['CC', 'csC', 'cscs', 'CC']
    white = ['ww', 'Wsw', 'Wdw', 'WsWs', 'WdWs', 'WdWd', 'ww', 'Wsw', 'WsWs', 'ww', 'Wsw', 'WsWs', 'ww', 'Wsw',
             'WsWs', 'ww', 'Wsw', 'WsWs', 'ww', 'Wsw', 'WsWs', 'ww', 'Wsw', 'WsWs']
    eyes = ['1', '2', '3', '4']

    genes = random.choice(fur) + " "
    genes += random.choice(gender) + " "
    genes += random.choice(colour) + " "
    genes += random.choice(dilute) + " "
    genes += random.choice(dilute_modifier) + " "
    genes += random.choice(solid) + " "
    genes += random.choice(inhibitor) + " "
    genes += random.choice(mackerel) + " "
    genes += random.choice(spotted) + " "
    genes += random.choice(ticked) + " "
    genes += random.choice(pointed) + " "
    genes += random.choice(white) + " "
    genes += random.choice(eyes) + " "
    genes += random.choice(eyes)

    return genes


def format_months_to_years_and_months(total_months):
    years = total_months // 12
    months = total_months % 12
    return f"{years} year{'s' if years != 1 else ''}, {months} month{'s' if months != 1 else ''}"
