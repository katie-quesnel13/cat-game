import random


def describe(genes):
    description = ""
    genes_in = genes.split()
    gene_dict = {i: gene for i, gene in enumerate(genes_in)}

    fur = gene_dict[0]  # fur length
    gender = gene_dict[1]  # gender + red tortie black
    colour = gene_dict[2]  # black/chocolate/cinnamon
    dilute = gene_dict[3]  # dilution
    dilute_modifier = gene_dict[4]  # dilution modifier - makes colours warmer w/ diff name
    solid = gene_dict[5]  # is it solid
    inhibitor = gene_dict[6]  # is this cat silver or smoke? silver tabby smoke solid
    mackerel = gene_dict[7]  # tabby patterns
    spotted = gene_dict[8]
    ticked = gene_dict[9]
    pointed = gene_dict[10]  # is it pointed
    white = gene_dict[11]  # white spotting and dominant white
    refraction = gene_dict[12]  # eye refraction
    pigment = gene_dict[13]  # eye pigment

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
                if dilute_modifier != "dmdm":
                    description += "apricot "
                else:
                    description += "cream "
            else:
                if dilute_modifier != "dmdm":
                    if colour == "blbl":
                        description += "fawn "
                    elif colour == "blb" or colour == "bb":
                        description += "lilac "
                    else:
                        description += "blue "
                else:
                    description += "caramel "
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
                if dilute_modifier == "dmdm":
                    if colour == "blbl":
                        description += "fawn and cream tortie "
                    elif colour == "blb" or colour == "bb":
                        description += "lilac and cream tortie "
                    else:
                        description += "blue and cream tortie "
                else:
                    description += "caramel and apricot tortie "
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
                    if dilute_modifier != "dmdm":
                        description += "apricot "
                    else:
                        description += "cream "
                else:
                    if dilute_modifier != "dmdm":
                        if colour == "blbl":
                            description += "fawn "
                        elif colour == "blb" or colour == "bb":
                            description += "lilac "
                        else:
                            description += "blue "
                    else:
                        description += "caramel "
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
            if inhibitor != "ii":
                description += "smoke showing "
            else:
                description += "solid showing "
            if contains_string(ticked, "Ta"):
                description += "ticked tabby "
            else:
                if mackerel == "mcmc":
                    description += "blotched tabby "
                else:
                    if spotted == "SpSp":
                        description += "spotted tabby "
                    elif spotted == "Spsp" or spotted == "spSp":
                        description += "broken mackerel tabby "
                    else:
                        description += "mackerel tabby "
        else:
            if inhibitor != "ii":
                description += "smoke "
            else:
                description += ""
    else:
        if inhibitor != "ii":
            description += "silver "
        if contains_string(ticked, "Ta"):
            description += "ticked tabby "
        else:
            if mackerel == "mcmc":
                description += "blotched tabby "
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
    bg_chance = 10
    if white == "WsWs" or contains_string(white, "Wd"):
        blue_chance = 40
        bg_chance = 10
        het_chance = 7
    if white == "Wsw":
        blue_chance = 20
        bg_chance = 10
        het_chance = 5
    if pointed == 'cscs':
        blue_chance = 100
        bg_chance = 10
        het_chance = 0

    ran = random.uniform(0, 100)
    blue = ran < blue_chance
    ran = random.uniform(0, 100)
    het = ran < het_chance
    ran = random.uniform(0, 100)
    bg = ran < bg_chance
    eyes = ""
    blue_eyes = ""

    if refraction == "1":
        if pigment == "1":
            eyes = " canary"
        if pigment == "2":
            eyes = " yellow"
        if pigment == "3":
            eyes = " gold"
        if pigment == "4":
            eyes = " saffron"
        if pigment == "5":
            eyes = " orange"
        if pigment == "6":
            eyes = " ochre"
        if pigment == "7":
            eyes = " copper"
    if refraction == "2":
        if pigment == "1":
            eyes = " chiffon"
        if pigment == "2":
            eyes = " chartreuse"
        if pigment == "3":
            eyes = " citron"
        if pigment == "4":
            eyes = " butterscotch"
        if pigment == "5":
            eyes = " amber"
        if pigment == "6":
            eyes = " caramel"
        if pigment == "7":
            eyes = " chestnut"
    if refraction == "3":
        if pigment == "1":
            eyes = " honeydew"
        if pigment == "2":
            eyes = " sprout"
        if pigment == "3":
            eyes = " pear"
        if pigment == "4":
            eyes = " shrub"
        if pigment == "5":
            eyes = " brass"
        if pigment == "6":
            eyes = " bronze"
        if pigment == "7":
            eyes = " umber"
    if refraction == "4":
        if pigment == "1":
            eyes = " sage"
        if pigment == "2":
            eyes = " laurel"
        if pigment == "3":
            eyes = " lime"
        if pigment == "4":
            eyes = " spring"
        if pigment == "5":
            eyes = " peridot"
        if pigment == "6":
            eyes = " serpentine"
        if pigment == "7":
            eyes = " walnut"
    if refraction == "5":
        if pigment == "1":
            eyes = " celadon"
        if pigment == "2":
            eyes = " mint"
        if pigment == "3":
            eyes = " mantis"
        if pigment == "4":
            eyes = " jade"
        if pigment == "5":
            eyes = " avocado"
        if pigment == "6":
            eyes = " artichoke"
        if pigment == "7":
            eyes = " earthen"
    if refraction == "6":
        if pigment == "1":
            eyes = " aqua"
        if pigment == "2":
            eyes = " turquoise"
        if pigment == "3":
            eyes = " grass"
        if pigment == "4":
            eyes = " pine"
        if pigment == "5":
            eyes = " clover"
        if pigment == "6":
            eyes = " fern"
        if pigment == "7":
            eyes = " olive"
    if refraction == "7":
        if pigment == "1":
            eyes = " cerulean"
        if pigment == "2":
            eyes = " teal"
        if pigment == "3":
            eyes = " viridian"
        if pigment == "4":
            eyes = " emerald"
        if pigment == "5":
            eyes = " malachite"
        if pigment == "6":
            eyes = " forest"
        if pigment == "7":
            eyes = " moss"

    if refraction == "1":
        if bg:
            blue_eyes = " frost"
        else:
            blue_eyes = " ice"
    if refraction == "2":
        if bg:
            blue_eyes = " opal"
        else:
            blue_eyes = " powder"
    if refraction == "3":
        if bg:
            blue_eyes = " flint"
        else:
            blue_eyes = " celeste"
    if refraction == "4":
        if bg:
            blue_eyes = " storm"
        else:
            blue_eyes = " sky"
    if refraction == "5":
        if bg:
            blue_eyes = " steel"
        else:
            blue_eyes = " azure"
    if refraction == "6":
        if bg:
            blue_eyes = " slate"
        else:
            blue_eyes = " lapis"
    if refraction == "7":
        if bg:
            blue_eyes = " cadet"
        else:
            blue_eyes = " cobalt"

    if het:
        eyes = " one" + eyes + " eye and one" + blue_eyes + " eye"
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
