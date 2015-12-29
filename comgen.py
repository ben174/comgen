import random


class ComGen:
    def __init__(self):
        self.adjectives = None
        self.nouns = None
        self.modifiers = None
        self.talents = None
        self.verbs = None
        self.adverbs = None
        self.load_dictionaries()

        # selections
        self.is_plural = None
        self.talent = None
        self.adjective = None
        self.noun = None
        self.modifier = None
        self.goodat = None
        self.plural = None
        self.verb = None
        self.adverb = None

        self.do_selection()


    def do_selection(self):
        self.noun = random.choice(self.nouns)
        self.noun, self.plural = self.noun
        self.talent = random.choice(self.talents)
        self.adjective = random.choice(self.adjectives)
        self.goodat = random.choice(self.goodats)
        self.verb = random.choice(self.verbs)
        self.modifier = random.choice(self.modifiers)
        self.adverb = random.choice(self.adverbs)


    def load_dictionaries(self):
        self.adverbs = [x for x in open('data/adverbs.txt').read().split('\n') if x]
        self.modifiers = [x for x in open('data/modifiers.txt').read().split('\n') if x]
        self.talents = [x for x in open('data/talents.txt').read().split('\n') if x]
        self.adjectives = [x for x in open('data/adjectives.txt').read().split('\n') if x]
        self.talents = [x for x in open('data/talents.txt').read().split('\n') if x]
        self.goodats = [x for x in open('data/goodats.txt').read().split('\n') if x]
        self.verbs = [x for x in open('data/verbs.txt').read().split('\n') if x]
        # noun|is_plural
        self.nouns = [x.split('|') for x in open('data/nouns.txt').read().split('\n') if x]

    def generate_has(self):
        a = 'a ' if not self.plural else ''
        return (
            'has {}{} {} {}.'.format(a, self.modifier, self.adjective, self.noun),
            (self.adjective, self.noun)
        )

    def generate_is(self):
        return (
            'is {} {} {}.'.format(self.modifier, self.goodat, self.talent),
            (self.goodat, self.talent),
        )


    def generate_does(self):
        return (
            '{} {} {}.'.format(self.verb, self.modifier, self.adverb),
            (self.verb, self.adverb),
        )

    def generate(self):
        methods = (self.generate_has, self.generate_is, self.generate_does)
        return random.choice(methods)()

