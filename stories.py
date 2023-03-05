"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text



story_options = [
    Story(["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""),
    Story(["adjective", "noun", "verb", "past_tense_verb", "plural_noun"],
    """Suddenly, a {adjective} {noun} came out of the {noun} and proceeded to {verb}. The audience was so shocked they {past_tense_verb} their {plural_noun}."""),
    Story(["intransitive_verb1","intransitive_verb2","intransitive_verb3","intransitive_verb4"],
    """Never gonna {intransitive_verb1} you up, 
    never gonna {intransitive_verb2} you down, 
    never gonna {intransitive_verb3} around and {intransitive_verb4} you."""), 

]
