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
        noun = random.choice(self.nouns)
        noun, plural = noun
        modifier = random.choice(self.modifiers)
        adjective = random.choice(self.adjectives)
        a = 'a ' if not plural else ''

        return 'I think you have {}{} {} {}'.format(a, modifier, adjective, noun)

    def generate_is(self):
        goodat = random.choice(self.goodats)
        modifier = random.choice(self.modifiers)
        talent = random.choice(self.talents)
        return 'I think you are {} {} {}'.format(modifier, goodat, talent)

    def generate_does(self):
        verb = random.choice(self.verbs)
        modifier = random.choice(self.modifiers)
        adverb = random.choice(self.adverbs)
        return 'I think you {} {} {}.'.format(verb, modifier, adverb)


comgen = ComGen()
print comgen.generate_has()
print comgen.generate_is()
print comgen.generate_does()
