import json

data = """
THUNDERCLAN
Leader: Firestar (1)
Deputy: Brambleclaw (2)
Medicine Cat: Jayfeather (3)
Warriors:
Graystripe (4)
Dustpelt (5)
Sandstorm (6)
Brackenfur (7)
Cloudtail (8)
Millie (9)
Thornclaw (10)
Squirrelflight (11)
Leafpool (12)
Spiderleg (13)
Birchfall (14)
Whitewing (15)
Berrynose (16)
Mousewhisker (17)
Hazeltail (18)
Cinderheart (19)
Lionblaze (20)
Foxleap (21)
Icecloud (22)
Toadstep (23)
Rosepetal (24)
Briarlight (25)
Blossomfall (26)
Bumblestripe (27)
Dovewing (28)
Ivypool (29)
Hollyleaf (30)
Poppyfrost (31)
Apprentices:
Molepaw (32)
Cherrypaw (33)
Queens:
Ferncloud (34)
Sorreltail (35)
Lilykit (36)
Seedkit (37)
Brightheart (38)
Dewkit (39)
Snowkit (40)
Amberkit (41)
Daisy (42)
Elders:
Mousefur (43)
Purdy (44)
SHADOWCLAN
Leader: Blackstar (45)
Deputy: Rowanclaw (46)
Medicine Cat: Littlecloud (47)
Warriors:
Oakfur (48)
Smokefoot (49)
Toadfoot (50)
Applefur (51)
Crowfrost (52)
Ratscar (53)
Snowbird (54)
Tawnypelt (55)
Olivenose (56)
Owlclaw (57)
Shrewfoot (58)
Scorchfur (59)
Redwillow (60)
Tigerheart (61)
Dawnpelt (62)
Ferretclaw (63)
Starlingwing (64)
Apprentices:
Stoatpaw (65)
Pouncepaw (66)
Queens:
Kinkfur (67)
Mistkit (68)
Sparrowkit (69)
Dewkit (70)
Pinenose (71)
Weaselkit (72)
Ivytail (73)
Grasskit (74)
Spikekit (75)
Elders:
Cedarheart (76)
Tallpoppy (77)
Snaketail (78)
Whitewater (79)
WINDCLAN
Leader: Onestar (80)
Deputy: Ashfoot (81)
Medicine Cat: Kestrelflight (82)
Warriors:
Crowfeather (83)
Owlwhisker (84)
Whitetail (85)
Nightcloud (86)
Gorsetail (87)
Weaselfur (88)
Harespring (89)
Leaftail (90)
Emberfoot (91)
Heathertail (92)
Breezepelt (93)
Sedgewhisker (94)
Swallowtail (95)
Sunstrike (96)
Whiskernose (97)
Furzepelt (98)
Boulderfur (99)
Apprentices:
Larkpaw (100)
Crouchpaw (101)
Elders:
Webfoot (102)
Tornear (103)
RIVERCLAN
Leader: Mistystar (104)
Deputy: Reedwhisker (105)
Medicine Cat: Mothwing (106)
Willowshine (107)
Warriors:
Mosspelt (108)
Mintfur (109)
Icewing (110)
Minnowtail (111)
Pebblefoot (112)
Mallownose (113)
Robinwing (114)
Beetlewhisker (115)
Petalfur (116)
Grasspelt (117)
Troutstream (118)
Mossyfoot (119)
Hollowflight (120)
Rushtail (121)
Apprentices:
Heronpaw (122)
Podpaw (123)
Curlpaw (124)
Queens:
Duskfur (125)
Lizardkit (126)
Havenkit (127)
Perchkit (128)
Elders:
Graymist (129)
Dapplenose (130)
"""

def parse_data(data):
    lines = data.strip().split('\n')
    clan = ""
    rank = ""
    warriors_data = []

    for line in lines:
        line = line.strip()
        if line.isupper():
            clan = line
        elif ':' in line:
            rank, rest = line.split(':', 1)
            rank = rank.strip()
            rest = rest.strip()
            if '(' in rest:
                name, number = rest.rsplit('(', 1)
                name = name.strip()
                number = number.strip(')')
                if name.endswith("kit"):
                    rank = "Kit"
                elif rank.endswith('s'):
                    rank = rank[:-1]  # Make rank singular
                warriors_data.append({
                    "name": name,
                    "rank": rank,
                    "clan": str.title(clan),
                    "id": int(number)
                })
        else:
            if line and '(' in line:
                name, number = line.rsplit('(', 1)
                name = name.strip()
                number = number.strip(')')
                if name.endswith("kit"):
                    rank = "Kit"
                elif rank.endswith('s'):
                    rank = rank[:-1]  # Make rank singular
                warriors_data.append({
                    "name": name,
                    "rank": rank,
                    "clan": str.title(clan),
                    "id": int(number)
                })

    return warriors_data

warriors_data = parse_data(data)

# Save to JSON file
with open('finalbattlelist.json', 'w') as json_file:
    json.dump(warriors_data, json_file, indent=4)

# Print the length of the warriors_data to verify
print(f"Total entries: {len(warriors_data)}")
