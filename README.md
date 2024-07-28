# Warrior cats inspired real cat genetics tools + Name makers
all generated cats are stored in clan.json

makekittens - takes in either genetics strings or the id of existing cats and produces a litter of kittens

makecat - takes in a gene string and makes a cat, then you set values like rank and age

ageclan - takes a list of cats in the json, increasing ages and applying name changes as needed. also updates leaders, deputies, as needed, using standard wc rules. assigns mentors to apprentices who don't yet have one, prefering non-parents before parents

describecat - used by the other tools as a base to turn genetics into a readable string

name_lists - used to store prefixes and suffixes for naming cats randomly, which are done in cat_creation_methods. split
out into different lists so that names match with the colour of the cat being named.

ns-names - a specific tool to generate warrior names using a list of prefixes specific to the nature found in Nova Scotia.
namemaker would be able to be pointed at other prefix lists, if generated

10percentfinalbattle - weird tools made on a whim to make doing the below linked au repeatedly faster and easier.

tests - it's got weird connected python bits i made to figure stuff out, like a very flexible
random number generator and some graphs about litter sizes / math about them

eye colour chart source: https://sparrows-garden.com/eye-color-generator.html (note i'm using different logic for the eyes)

warriors but cats die: https://warriors-but-cats-die.tumblr.com/

10% survivors au: https://www.tumblr.com/10leftau/185132555587/myo-10-left
