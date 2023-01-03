import random


def get_lines(filename):
    with open (filename, 'r') as f:
        return f.readlines()


def get_all_adjectives():
    return get_lines("./text/sap_adjectives.txt")


def get_all_nouns():
    return get_lines("./text/sap_nouns.txt")


def get_random_adjective():
    adjectives = get_all_adjectives()
    return random.sample(adjectives, 1)[0]


def get_random_noun():
    nouns = get_all_nouns()
    return random.sample(nouns, 1)[0]


def get_random_sap_team():
    adjective = get_random_adjective()
    noun = get_random_noun()
    return f'{adjective} {noun}'


def get_random_sap_team_alliteration():
    adjective = get_random_adjective()
    first_letter = adjective[0]
    nouns = [noun for noun in get_all_nouns() if noun[0] == first_letter]
    if len(nouns) == 0:
        return get_random_sap_team_alliteration()
    noun = random.sample(nouns, 1)[0]
    return f'{adjective} {noun}'