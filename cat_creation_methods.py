from name_lists import *
import random


def get_prefix(appearance):
    prefix_list = []
    prefix_list.extend(generic_names)

    if " red " in appearance:
        prefix_list.extend(red_names)

    if "cream " in appearance:
        prefix_list.extend(cream_names)

    if "black " in appearance:
        prefix_list.extend(black_names)

    if "blue " in appearance:
        prefix_list.extend(blue_names)

    if "chocolate " in appearance:
        prefix_list.extend(chocolate_names)

    if "lilac " in appearance:
        prefix_list.extend(lilac_names)

    if "cinnamon " in appearance:
        prefix_list.extend(cinnamon_names)

    if "fawn " in appearance:
        prefix_list.extend(fawn_names)

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


def get_suffix(prefix):
    suffix = prefix
    while suffix == prefix:
        suffix = random.choice(name_list)
    return suffix
