- allegiances mode (take in clan.json and format it into clan order, using the present data)
    - this would make a decent core to the looping tool?
- modify ageclan to support assigning apprentices on aging?
- modify makecat to be able to randomly create a genestring if no input is provided
- modify namemaker to be able to take in different location packs for prefixes
- think of more prefixes and suffixes + add them in
- death triggers to ageclan
    - need to decide level of mortality (save file setting?)
    - would be interested in something along the lines of the tumblr blog 'warrior cats but cats die' as at least one
      to try, though that would want to be non-looping due to required file editing
- some sort of method of pairing cats + chance to have kittens on ageclan
- retirement chance to handle elders
- tool to pick an eligible deputy from the clan file (warrior rank, trained an apprentice to warrior)
    - consider the fun added rules of raising a kitten to adult as mother counting? (on rational of raising the young)
    - this needs checking the age of apprentice/kit listed - probably just take first in list as they'd be oldest?
- maybe swap off of the names by coat method? or change it so duplicates are removed after merging the lists
- some sort of looping access system which means i can launch one program and access the others repeatedly
    - maybe change with this to have "save files" rather than always using clan.json
- refactor the existing code to make more sense, especially splitting methods into more generic files
    - this would probably also involve using more efficient solutions than chained if statements, as they're a lot to read
- consider refactoring the gene strings to support more genes? silver, dilute modifier, other types of pointing? albinos?
 don't think i want fur mutations or ear/tail mutations, but maybe polydactyl? that would involve storing presentation of 
 maybe genes, though
- adjust the data system to have access to determined blue and het as part of the cat data, rather than needing to check
 descriptions for specific wording (currently blue and singular eye)
- add converting the moons ages into years to something. math is hard and computer is good at it