# Warrior cats inspired real genetics tools
all generated cats are stored in clan.json

makekittens - takes in either genetics strings or the id of existing cats and produces a litter of kittens

makecat - takes in a gene string and makes a cat, then you set values like rank and age

ageclan - takes a list of cats in the json, increasing ages and applying name changes as needed. does not handle leaders, 
deputies, or healers

describecat - used by the other tools as a base to turn genetics into a readable string

name_lists - used to store prefixes and suffixes for naming cats randomly, which are done in cat_creation_methods. split
out into different lists so that names match with the colour of the cat being named.

ns-names - a specific tool to generate warrior names using a list of prefixes specific to the nature found in Nova Scotia.
namemaker would be able to be pointed at other prefix lists, if generated

eye colour chart source: https://sparrows-garden.com/eye-color-generator.html (note i'm using different logic for the eyes)