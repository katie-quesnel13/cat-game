import random


def describe(genes):
    description = ""
    genes_in = genes.split()
    gene_dict = {i: gene for i, gene in enumerate(genes_in)}

    fur = gene_dict[0]  # fur length
    gender = gene_dict[1]  # gender + red tortie black
    colour = gene_dict[2]  # black/chocolate/cinnamon
    dilute = gene_dict[3]  # dilution
    solid = gene_dict[4]  # is it solid
    mackerel = gene_dict[5]  # tabby patterns
    spotted = gene_dict[6]
    ticked = gene_dict[7]
    pointed = gene_dict[8]  # is it pointed
    white = gene_dict[9]  # white spotting and dominant white
    refraction = gene_dict[10]  # eye refraction
    pigment = gene_dict[11]  # eye pigment

    if contains_string(white, "Wd"):
        if fur == "LL" or fur == "Ll" or fur == "lL":
            description += "short-haired "
        else:
            description += "long-haired "
        description += "dominant white "
        if gender == "XOY" or gender == "XoY":
            description += "tom"
        else:
            description += "molly"
        description += " with"
        description += desc_eyes(refraction, pigment, white, pointed)
        return description

    if fur == "LL" or fur == "Ll" or fur == "lL":
        description += "short-haired "
    else:
        description += "long-haired "

    if gender == "XOY" or gender == "XoY":
        if dilute == "dd":
            if gender == "XOY":
                description += "cream "
            else:
                if colour == "blbl":
                    description += "fawn "
                elif colour == "blb" or colour == "bb":
                    description += "lilac "
                else:
                    description += "blue "
        else:
            if gender == "XOY":
                description += "red "
            else:
                if colour == "blbl":
                    description += "cinnamon "
                elif colour == "blb" or colour == "bb":
                    description += "chocolate "
                else:
                    description += "black "
    else:
        if gender == "XOXo" or gender == "XoXO":
            if dilute == "dd":
                if colour == "blbl":
                    description += "fawn and cream tortie "
                elif colour == "blb" or colour == "bb":
                    description += "lilac and cream tortie "
                else:
                    description += "blue and cream tortie "
            else:
                if colour == "blbl":
                    description += "cinnamon and red tortie "
                elif colour == "blb" or colour == "bb":
                    description += "chocolate and red tortie "
                else:
                    description += "black and red tortie "
        else:
            if dilute == "dd":
                if gender == "XOXO":
                    description += "cream "
                else:
                    if colour == "blbl":
                        description += "fawn "
                    elif colour == "blb" or colour == "bb":
                        description += "lilac "
                    else:
                        description += "blue "
            else:
                if gender == "XOXO":
                    description += "red "
                else:
                    if colour == "blbl":
                        description += "cinnamon "
                    elif colour == "blb" or colour == "bb":
                        description += "chocolate "
                    else:
                        description += "black "

    if solid == "aa":
        if gender == "XOXo" or gender == "XoXO":
            description += "solid showing "
            if contains_string(ticked, "Ta"):
                description += "ticked tabby "
            else:
                if mackerel == "mcmc":
                    description += "classic tabby "
                else:
                    if spotted == "SpSp":
                        description += "spotted tabby "
                    elif spotted == "Spsp" or spotted == "spSp":
                        description += "broken mackerel tabby "
                    else:
                        description += "mackerel tabby "
        else:
            description += ""
    else:
        if contains_string(ticked, "Ta"):
            description += "ticked tabby "
        else:
            if mackerel == "mcmc":
                description += "classic tabby "
            else:
                if spotted == "SpSp":
                    description += "spotted tabby "
                elif spotted == "Spsp" or spotted == "spSp":
                    description += "broken mackerel tabby "
                else:
                    description += "mackerel tabby "

    if pointed == "cscs":
        description += "pointed "

    if gender == "XOY" or gender == "XoY":
        description += "tom"
    else:
        description += "molly"

    if white == "WsWs":
        description += " with high white spotting"
    elif white == "Wsw":
        description += " with low white spotting"

    if white == "WsWs" or white == "Wsw":
        description += " and"
    else:
        description += " with"

    description += desc_eyes(refraction, pigment, white, pointed)
    return description


def desc_eyes(refraction, pigment, white, pointed):
    refraction = str(refraction)
    pigment = str(pigment)
    blue_chance = 0
    het_chance = 1
    if white == "WsWs" or contains_string(white, "Wd"):
        blue_chance = 40
        het_chance = 7
    if white == "Wsw":
        blue_chance = 20
        het_chance = 5
    if pointed == 'cscs':
        blue_chance = 100
        het_chance = 0

    ran = random.uniform(0, 100)
    blue = ran < blue_chance
    ran = random.uniform(0, 100)
    het = ran < het_chance
    eyes = ""
    blue_eyes = ""

    if refraction == "1":
        if pigment == "1":
            eyes = " yellow"
        if pigment == "2":
            eyes = " gold"
        if pigment == "3":
            eyes = " orange"
        if pigment == "4":
            eyes = " copper"
    if refraction == "2":
        if pigment == "1":
            eyes = " pale green"
        if pigment == "2":
            eyes = " leaf green"
        if pigment == "3":
            eyes = " amber"
        if pigment == "4":
            eyes = " bronze"
    if refraction == "3":
        if pigment == "1":
            eyes = " aqua"
        if pigment == "2":
            eyes = " green"
        if pigment == "3":
            eyes = " hazel"
        if pigment == "4":
            eyes = " brown"
    if refraction == "4":
        if pigment == "1":
            eyes = " blue-green"
        if pigment == "2":
            eyes = " deep green"
        if pigment == "3":
            eyes = " moss green"
        if pigment == "4":
            eyes = " dark green"

    if refraction == "1":
        blue_eyes = " ice blue"
    if refraction == "2":
        blue_eyes = " sky blue"
    if refraction == "3":
        blue_eyes = " blue"
    if refraction == "4":
        blue_eyes = " dark blue"

    if het:
        eyes = " one" + eyes + " eye and one"
        if refraction == "1":
            eyes += " ice blue eye"
        if refraction == "2":
            eyes += " sky blue eye"
        if refraction == "3":
            eyes += " blue eye"
        if refraction == "4":
            eyes += " dark blue eye"
        return eyes
    else:
        if blue:
            blue_eyes += " eyes"
            return blue_eyes
        else:
            eyes += " eyes"
            return eyes


def contains_string(g, target):
    it = iter(g)
    return all(char in it for char in target)
