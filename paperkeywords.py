#!/usr/bin/env python3

import sys
import argparse
import re


PAPERKEYLINE = re.compile(r'^[ ]*[0-9]+:')
HEXBLOCK = re.compile(r'[a-fA-F0-9]{2}')
WORDS = [["aardvark", "absurd", "accrue", "acme", "adrift", "adult", "afflict", "ahead", "aimless", "Algol", "allow", "alone", "ammo", "ancient", "apple", "artist", "assume", "Athens", "atlas", "Aztec", "baboon", "backfield", "backward", "banjo", "beaming", "bedlamp", "beehive", "beeswax", "befriend", "Belfast", "berserk", "billiard", "bison", "blackjack", "blockade", "blowtorch", "bluebird", "bombast", "bookshelf", "brackish", "breadline", "breakup", "brickyard", "briefcase", "Burbank", "button", "buzzard", "cement", "chairlift", "chatter", "checkup", "chisel", "choking", "chopper", "Christmas", "clamshell", "classic", "classroom", "cleanup", "clockwork", "cobra", "commence", "concert", "cowbell", "crackdown", "cranky", "crowfoot", "crucial", "crumpled", "crusade", "cubic", "dashboard", "deadbolt", "deckhand", "dogsled", "dragnet", "drainage", "dreadful", "drifter", "dropper", "drumbeat", "drunken", "Dupont", "dwelling", "eating", "edict", "egghead", "eightball", "endorse", "endow", "enlist", "erase", "escape", "exceed", "eyeglass", "eyetooth", "facial", "fallout", "flagpole", "flatfoot", "flytrap", "fracture", "framework", "freedom", "frighten", "gazelle", "Geiger", "glitter", "glucose", "goggles", "goldfish", "gremlin", "guidance", "hamlet", "highchair", "hockey", "indoors", "indulge", "inverse", "involve", "island", "jawbone", "keyboard", "kickoff", "kiwi", "klaxon", "locale", "lockup", "merit", "minnow", "miser", "Mohawk", "mural", "music", "necklace", "Neptune", "newborn", "nightbird", "Oakland", "obtuse", "offload", "optic", "orca", "payday", "peachy", "pheasant", "physique", "playhouse", "Pluto", "preclude", "prefer", "preshrunk", "printer", "prowler", "pupil", "puppy", "python", "quadrant", "quiver", "quota", "ragtime", "ratchet", "rebirth", "reform", "regain", "reindeer", "rematch", "repay", "retouch", "revenge", "reward", "rhythm", "ribcage", "ringbolt", "robust", "rocker", "ruffled", "sailboat", "sawdust", "scallion", "scenic", "scorecard", "Scotland", "seabird", "select", "sentence", "shadow", "shamrock", "showgirl", "skullcap", "skydive", "slingshot", "slowdown", "snapline", "snapshot", "snowcap", "snowslide", "solo", "southward", "soybean", "spaniel", "spearhead", "spellbind", "spheroid", "spigot", "spindle", "spyglass", "stagehand", "stagnate", "stairway", "standard", "stapler", "steamship", "sterling", "stockman", "stopwatch", "stormy", "sugar", "surmount", "suspense", "sweatband", "swelter", "tactics", "talon", "tapeworm", "tempest", "tiger", "tissue", "tonic", "topmost", "tracker", "transit", "trauma", "treadmill", "Trojan", "trouble", "tumor", "tunnel", "tycoon", "uncut", "unearth", "unwind", "uproot", "upset", "upshot", "vapor", "village", "virus", "Vulcan", "waffle", "wallet", "watchword", "wayside", "willow", "woodlark", "Zulu"],
         ["adroitness", "adviser", "aftermath", "aggregate", "alkali", "almighty", "amulet", "amusement", "antenna", "applicant", "Apollo", "armistice", "article", "asteroid", "Atlantic", "atmosphere", "autopsy", "Babylon", "backwater", "barbecue", "belowground", "bifocals", "bodyguard", "bookseller", "borderline", "bottomless", "Bradbury", "bravado", "Brazilian", "breakaway", "Burlington", "businessman", "butterfat", "Camelot", "candidate", "cannonball", "Capricorn", "caravan", "caretaker", "celebrate", "cellulose", "certify", "chambermaid", "Cherokee", "Chicago", "clergyman", "coherence", "combustion", "commando", "company", "component", "concurrent", "confidence", "conformist", "congregate", "consensus", "consulting", "corporate", "corrosion", "councilman", "crossover", "crucifix", "cumbersome", "customer", "Dakota", "decadence", "December", "decimal", "designing", "detector", "detergent", "determine", "dictator", "dinosaur", "direction", "disable", "disbelief", "disruptive", "distortion", "document", "embezzle", "enchanting", "enrollment", "enterprise", "equation", "equipment", "escapade", "Eskimo", "everyday", "examine", "existence", "exodus", "fascinate", "filament", "finicky", "forever", "fortitude", "frequency", "gadgetry", "Galveston", "getaway", "glossary", "gossamer", "graduate", "gravity", "guitarist", "hamburger", "Hamilton", "handiwork", "hazardous", "headwaters", "hemisphere", "hesitate", "hideaway", "holiness", "hurricane", "hydraulic", "impartial", "impetus", "inception", "indigo", "inertia", "infancy", "inferno", "informant", "insincere", "insurgent", "integrate", "intention", "inventive", "Istanbul", "Jamaica", "Jupiter", "leprosy", "letterhead", "liberty", "maritime", "matchmaker", "maverick", "Medusa", "megaton", "microscope", "microwave", "midsummer", "millionaire", "miracle", "misnomer", "molasses", "molecule", "Montana", "monument", "mosquito", "narrative", "nebula", "newsletter", "Norwegian", "October", "Ohio", "onlooker", "opulent", "Orlando", "outfielder", "Pacific", "pandemic", "Pandora", "paperweight", "paragon", "paragraph", "paramount", "passenger", "pedigree", "Pegasus", "penetrate", "perceptive", "performance", "pharmacy", "phonetic", "photograph", "pioneer", "pocketful", "politeness", "positive", "potato", "processor", "provincial", "proximate", "puberty", "publisher", "pyramid", "quantity", "racketeer", "rebellion", "recipe", "recover", "repellent", "replica", "reproduce", "resistor", "responsive", "retraction", "retrieval", "retrospect", "revenue", "revival", "revolver", "sandalwood", "sardonic", "Saturday", "savagery", "scavenger", "sensation", "sociable", "souvenir", "specialist", "speculate", "stethoscope", "stupendous", "supportive", "surrender", "suspicious", "sympathy", "tambourine", "telephone", "therapist", "tobacco", "tolerance", "tomorrow", "torpedo", "tradition", "travesty", "trombonist", "truncated", "typewriter", "ultimate", "undaunted", "underfoot", "unicorn", "unify", "universe", "unravel", "upcoming", "vacancy", "vagabond", "vertigo", "Virginia", "visitor", "vocalist", "voyager", "warranty", "Waterloo", "whimsical", "Wichita", "Wilmington", "Wyoming", "yesteryear", "Yucatan"]]
WORD_INDECES = [{}, {}]


def build_word_indeces():
    global WORD_INDECES
    for i in range(256):
        WORD_INDECES[0][WORDS[0][i].upper()] = i
        WORD_INDECES[1][WORDS[1][i].upper()] = i


def codes_to_words(codes):
    nr = 0
    for code in codes:
        if not HEXBLOCK.match(code):
            yield code
            continue
        index = int(code, 16)
        word = WORDS[nr%2][index]
        nr += 1
        yield word


def words_to_codes(words):
    for nr, word in enumerate([w for w in words if len(w) > 0]):
        word_index = WORD_INDECES[nr%2]
        if word.upper() in WORD_INDECES[(nr+1)%2]:
            raise ValueError(f'Parity error for word nr {nr+1} "{word}".')
        if word.upper() not in word_index:
            raise ValueError(f'Word nr {nr+1} "{word}" unknown')
        value = word_index[word.upper()]
        yield '{:02X}'.format(value)


def encode(fdin, fdout):
    for line in fdin:
        if not PAPERKEYLINE.match(line):
            fdout.write(line)
            continue
        prefix, codes = line.split(':', 1)
        codes, checksum = codes.rsplit(' ', 1)
        words = ' '.join(codes_to_words(codes.split(' ')))
        fdout.write(f'{prefix}: {words} {checksum}')


def decode(fdin, fdout):
    for line in fdin:
        if not PAPERKEYLINE.match(line):
            fdout.write(line)
            continue
        prefix, words = line.split(':', 1)
        words, checksum = words.rsplit(' ', 1)
        codes = ' '.join(words_to_codes(words.split(' ')))
        fdout.write(f'{prefix}: {codes} {checksum}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encode', action='store_true', help='Encode the input (this is the default)')
    parser.add_argument('-d', '--decode', action='store_true', help='Decode the input')
    parser.add_argument('-i', '--input', type=str, default=None, help='Input file, if not provided read from stdin')
    parser.add_argument('-o', '--output', type=str, default=None, help='Input file, if not provided read from stdin')
    args = parser.parse_args(sys.argv[1:])

    fdin = sys.stdin
    fdout = sys.stdout

    if args.input is not None:
        fdin = open(args.input, 'rt')
    if args.output is not None:
        fdout = open(args.output, 'wt')

    if args.decode:
        build_word_indeces()
        decode(fdin, fdout)
    else:
        encode(fdin, fdout)

    fdin.close()
    fdout.close()


if __name__ == '__main__':
    main()
