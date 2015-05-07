# -*- coding: utf-8 -*-
"""
FILENAME: tokens.py -- part of Coquery corpus query tool

This module defines classes that represent tokens in a query string.

"""

# tokens.py contains classes that represent a query token from a query 
# string. For instance, the COCA query [n*] has [v*] consists of the three
# tokens [n*], 'has', and [v*]. 
#
# The syntax used for the tokens is corpus-specific, and different classes
# can be used to represent different syntaxes.
#
# Each QueryToken should be parseable into four pieces of information:
#    
# word_specifiers     a list of strings that specify word-forms
# lemma_specifiers    a list of strings that specifies lemmas
# class_specifiers    a list of strings that specifies part-of-speech
# negated             a boolean flag that indicates negation
#
# The method parse() is used to translate the token string into these
# structures.

import unittest

import string
import re

from defines import *
from errors import *

class QueryToken(object):
    """ 
A QueryToken is one element in a corpus query. The syntax is 
corpus-specific. 
    """
    bracket_open = "("
    bracket_close = ")"
    transcript_open = "/"
    transcript_close = "/"
    or_character = "|"
    
    def __init__(self, S, lexicon):
        self.lexicon = lexicon
        self.S = S.strip()
        self.replace_wildcards()
        self.word_specifiers = []
        self.class_specifiers = []
        self.lemma_specifiers = []
        self.transcript_specifiers = []
        self.negated = False
        self.transcript = False
        self.parse()
        
    def __eq__(self, S):
        return self.S == S
    
    def __ne__(self, S):
        return self.S != S
    
    def __repr__(self):
        return self.S
    
    def replace_wildcards(self):
        """
replace_wildcards() replaces the characters from self.lexicon.wildcards by
the appropriate SQL correspondents.
        """
        if self.lexicon and len(self.S) > 1:
            for old, new in zip(["*", "?"], self.lexicon.resource.wildcards):
                self.S = self.S.replace(old, new)
        
    def get_parse(self):
        if self.word_specifiers:
            assert not self.lemma_specifiers
        return self.word_specifiers, self.lemma_specifiers, self.class_specifiers, self.negated

    def check_brackets(self, S):
        """ 
check_brackets(S) returns True if S starts and ends with exactly one 
matching bracket, and does not contain any other brackets. The type of 
brackets is class-specific, it defaults to ( and ), but the COCA classes 
use [ and ]. 
        """        
        if self.bracket_open in S or self.bracket_close in S:
            if S.count(self.bracket_open) != S.count(self.bracket_close):
                raise TokenParseError(self)
            if not S.startswith(self.bracket_open) or not S.endswith(self.bracket_close):
                raise TokenParseError(self)
            if S.count (self.bracket_open) > 1:
                raise TokenParseError(self)
            if S.count (self.bracket_close) > 1:
                raise TokenParseError(self)
            return True
        else:
            return False
    
    def check_transcript(self, S):
        """ return True if S starts and ends with the transcription markers"""
        return S.startswith(self.transcript_open) and S.endswith(self.transcript_close)
    
    def parse (self):
        """ parse() is the function that derives word, lemma, and class
        specificiations from the token string. The syntax is 
        corpus-specific. """
        self.lemma_specifiers = []
        self.class_specifiers = []
        self.word_specifiers = self.S.split(",")

class COCAToken(QueryToken):
    """ Valid token string formats:
        entity_specifier
        [class_specifier]
        entity_specifier.[class_specifier]
        
        both specifiers are of the form:
        spec1 | spec2 | ... | spec_n
        
        A token string may be preceded by a negation sign.
    """
    bracket_open = "["
    bracket_close = "]"
    transcript_open = "/"
    transcript_close = "/"
    NegationChar = "#"
    
    # use the corpus to determine whether a token string like [xx] contains
    # a part-of-speech tag:
    check_part_of_speech = True
    
    def __init__(self, S, Corpus):
        super(COCAToken, self).__init__(S, Corpus)

    def __repr__(self):
        return self.S

    def get_parse(self):
        return self.word_specifiers, self.lemma_specifiers, self.class_specifiers, self.negated

    def parse (self):
        self.word_specifiers = []
        self.class_specifiers = []
        self.lemma_specifiers = []        
        self.transcript_specifiers = []
        
        if self.S.startswith(self.NegationChar) and len(self.S) > 1:
            self.negated = True
            ConstituentList = self.S.strip(self.NegationChar).split(".")
        else:
            self.negated = False
            ConstituentList = self.S.split(".")
            
        # Parse and process second constituent, i.e. xxx.[XXX]
        # (if existing):
        if len(ConstituentList) == 2:
            S = ConstituentList[1]
            if self.check_brackets(S):
                self.class_specifiers = [x.strip() for x in S[1:-1].split("|")]
                if self.check_part_of_speech:
                    if self.lexicon.check_pos_list(self.class_specifiers) < len(self.class_specifiers):
                        raise TokenPartOfSpeechError(self)
        # Parse and process first constituent:
        S = ConstituentList[0]
        if S and self.check_brackets(S):
            element_list = [x.strip() for x in S[1:-1].split("|")]
            if self.check_part_of_speech:
                # check if all elements pass as part-of-speech-tags:
                if len(element_list) == self.lexicon.check_pos_list(element_list):
                    # if so, interpret elements as part-of-speech tags:
                    self.class_specifiers = element_list
                else:
                    # if not, interpret elements as lemmas:
                    self.lemma_specifiers = element_list
            else:
                self.lemma_specifiers = element_list
        else:
            for current_word in S.split("|"):
                current_word = current_word.strip()
                if current_word:
                    if self.check_transcript(current_word):
                        current_word = current_word.translate(
                            string.maketrans("", "", ), 
                            "".join([self.transcript_open, self.transcript_close]))
                        self.transcript_specifiers.append(current_word.strip())
                    else:
                        self.word_specifiers.append(current_word)

class COCARegExpToken(COCAToken):
    def parse (self):
        self.word_specifiers = []
        self.class_specifiers = []
        self.lemma_specifiers = []        
        self.transcript_specifiers = []

        match = re.match("(\[(?P<lemma>.*)\]|/(?P<trans>.*)/|(?P<word>.*)){1}(\.\[(?P<class>.*)\]){1}", self.S)
        if not match:
            match = re.match("(\[(?P<lemma>.*)\]|/(?P<trans>.*)/|(?P<word>.*)){1}", self.S)

        word_specification = match.groupdict()["word"]
        lemma_specification = match.groupdict()["lemma"]
        transcript_specification = match.groupdict()["trans"]
        try:
            class_specification = match.groupdict()["class"]
        except KeyError:
            class_specification = None

        if word_specification:
            self.word_specifiers = [x.strip() for x in word_specification.split("|") if x.strip()]
        if transcript_specification:
            self.transcript_specifiers = [x.strip() for x in transcript_specification.split("|") if x.strip()]
        if lemma_specification:
            self.lemma_specifiers = [x.strip() for x in lemma_specification.split("|") if x.strip()]
        if class_specification:
            self.class_specifiers = [x.strip() for x in class_specification.split("|") if x.strip()]
        
        if lemma_specification and not class_specification:
            if self.check_part_of_speech:
                # check if all elements pass as part-of-speech-tags:
                if len(self.lemma_specifiers) == self.lexicon.check_pos_list(self.lemma_specifiers):
                    # if so, interpret elements as part-of-speech tags:
                    self.class_specifiers = self.lemma_specifiers
                    self.lemma_specifiers = []

class COCAWord(COCAToken):
    """ A class that is simply parsed as a single word. """
    def parse(self):
        self.lemma_specifiers = []
        self.class_specifiers = []
        self.word_specifiers = [self.S]

class COCATextToken(COCAToken):
    # do not use the corpus to determine whether a token string like 
    # [xx] contains a part-of-speech tag:
    check_part_of_speech = False

    def get_parse(self):
        return self.word_specifiers, self.class_specifiers, self.negated
    
    def parse(self):
        """ 
Syntax:     GENRE.[YEAR], with alternatives separated by '|'.
            Negation is possible by preceding the filter with '-'
Examples:   FIC (equivalent to FIC.[*])
            -FIC (equivalent to ACAD|NEWS|MAG)
            FIC|ACAD 
            FIC.[2003]
            FIC|ACAD.[2003|2004]
            FIC|ACAD.[2003-2007]
            [2003-2007] (equivalent to *.[2003-2007])
        """
        super(COCATextToken, self).parse()
        # Special case that allows '.[*]' as a year specifier:
        if len(self.class_specifiers) == 1 and self.class_specifiers[0] in self.lexicon.resource.wildcards:
            self.class_specifiers = []
        # Special case that allows the use of '[2003]' format (i.e. 
        # specification of year, but not of genre:
        if self.lemma_specifiers:
            self.class_specifiers = self.lemma_specifiers
            self.lemma_specifiers = []

def parse_query_string(S, token_type):
    ST_NORMAL = 0
    ST_IN_BRACKET = 1
    ST_IN_TRANSCRIPT = 2
    
    tokens = []
    state = ST_NORMAL
    current_word = ""
    negated = False
    
    t2 = []
    for current_char in S:
        if state == ST_NORMAL:
            if current_char == " ":
                if current_word:
                    tokens.append(current_word)
                    current_word = ""
            else:
                current_char = current_char.strip()
                if current_char:
                    current_word = "%s%s" % (current_word, current_char)
            if current_char == token_type.transcript_open:
                state = ST_IN_TRANSCRIPT
            elif current_char == token_type.bracket_open:
                state = ST_IN_BRACKET
            elif current_char == token_type.NegationChar:
                negated = not negated
                    
        elif state == ST_IN_BRACKET:
            if current_char == token_type.bracket_close:
                current_word = "%s%s" % (current_word, token_type.bracket_close)
                state = ST_NORMAL
            elif current_char not in [token_type.bracket_open, token_type.transcript_open, token_type.transcript_close]:
                current_word = "%s%s" % (current_word, current_char)
            else:
                raise TokenParseError(S)
            
        elif state == ST_IN_TRANSCRIPT:
            if current_char == token_type.transcript_close:
                current_word = "%s%s" % (current_word, token_type.transcript_close)
                state = ST_NORMAL
            elif current_char != token_type.or_character:
                current_word = "%s%s" % (current_word, current_char)
            else:
                raise TokenParseError(S)
                
    if state != ST_NORMAL:
        raise TokenParseError(S)
    if current_word:
        tokens.append(current_word)
    return tokens
    
    return S.split()

class TestQueryToken(unittest.TestCase):
    token_type = QueryToken
    
    def runTest(self):
        super(TestQueryToken, self).runTest()
    
    def setUp(self):
        import corpus
        self.lexicon = corpus.TestLexicon(corpus.BaseResource())
    
    def test_word_only(self):
        token = self.token_type("word", self.lexicon)
        token.parse()
        self.assertEqual(token.lemma_specifiers, [])
        self.assertEqual(token.transcript_specifiers, [])
        self.assertEqual(token.class_specifiers, [])
        self.assertEqual(token.word_specifiers, ["word"])

    def test_several_words(self):
        token = self.token_type("word1|word2", self.lexicon)
        token.parse()
        self.assertEqual(token.lemma_specifiers, [])
        self.assertEqual(token.transcript_specifiers, [])
        self.assertEqual(token.class_specifiers, [])
        self.assertEqual(token.word_specifiers, ["word1", "word2"])

    def test_lemma_only(self):
        token = self.token_type("[lemma]", self.lexicon)
        token.parse()
        self.assertEqual(token.lemma_specifiers, ["lemma"])
        self.assertEqual(token.transcript_specifiers, [])
        self.assertEqual(token.class_specifiers, [])
        self.assertEqual(token.word_specifiers, [])

    def test_several_lemmas(self):
        token = self.token_type("[lemma1|lemma2]", self.lexicon)
        token.parse()
        self.assertEqual(token.lemma_specifiers, ["lemma1", "lemma2"])
        self.assertEqual(token.transcript_specifiers, [])
        self.assertEqual(token.class_specifiers, [])
        self.assertEqual(token.word_specifiers, [])

    def test_words_and_pos(self):
        token = self.token_type("word1|word2.[N]", self.lexicon)
        token.parse()
        self.assertEqual(token.lemma_specifiers, [])
        self.assertEqual(token.transcript_specifiers, [])
        self.assertEqual(token.class_specifiers, ["N"])
        self.assertEqual(token.word_specifiers, ["word1", "word2"])
        
    def test_words_and_several_pos(self):
        token = self.token_type("word1|word2.[N|V]", self.lexicon)
        token.parse()
        self.assertEqual(token.lemma_specifiers, [])
        self.assertEqual(token.transcript_specifiers, [])
        self.assertEqual(token.class_specifiers, ["N", "V"])
        self.assertEqual(token.word_specifiers, ["word1", "word2"])

    def test_lemmas_and_pos(self):
        token = self.token_type("[lemma1|lemma2].[N]", self.lexicon)
        token.parse()
        self.assertEqual(token.lemma_specifiers, ["lemma1", "lemma2"])
        self.assertEqual(token.transcript_specifiers, [])
        self.assertEqual(token.class_specifiers, ["N"])
        self.assertEqual(token.word_specifiers, [])
        
    def test_lemmas_and_several_pos(self):
        token = self.token_type("[lemma1|lemma2].[N|V]", self.lexicon)
        token.parse()
        self.assertEqual(token.lemma_specifiers, ["lemma1", "lemma2"])
        self.assertEqual(token.transcript_specifiers, [])
        self.assertEqual(token.class_specifiers, ["N", "V"])
        self.assertEqual(token.word_specifiers, [])
        
    def test_only_pos(self):
        token = self.token_type("[N|V]", self.lexicon)
        token.parse()
        self.assertEqual(token.lemma_specifiers, [])
        self.assertEqual(token.transcript_specifiers, [])
        self.assertEqual(token.class_specifiers, ["N", "V"])
        self.assertEqual(token.word_specifiers, [])        
        
    def test_transcripts(self):
        token = self.token_type("/trans1|trans2/", self.lexicon)
        token.parse()
        self.assertEqual(token.lemma_specifiers, [])
        self.assertEqual(token.transcript_specifiers, ["trans1", "trans2"])
        self.assertEqual(token.class_specifiers, [])
        self.assertEqual(token.word_specifiers, [])

    def test_transcripts_and_several_pos(self):
        token = self.token_type("/trans1|trans2/.[N|V]", self.lexicon)
        token.parse()
        self.assertEqual(token.lemma_specifiers, [])
        self.assertEqual(token.transcript_specifiers, ["trans1", "trans2"])
        self.assertEqual(token.class_specifiers, ["N", "V"])
        self.assertEqual(token.word_specifiers, [])

    def test_transcripts_multiple_slashes(self):
        token = self.token_type("/trans1/|/trans2/", self.lexicon)
        token.parse()
        self.assertEqual(token.lemma_specifiers, [])
        self.assertEqual(token.transcript_specifiers, ["trans1/", "/trans2"])
        self.assertEqual(token.class_specifiers, [])
        self.assertEqual(token.word_specifiers, [])

class TestCOCARegExpToken(TestQueryToken):
    token_type = COCARegExpToken

class TestCOCAToken(TestQueryToken):
    token_type = COCAToken
    
if __name__ == '__main__':
    
    import timeit
    
    t1 = timeit.Timer("""
        import unittest
        from tokens import *
        import corpus
        lexicon = corpus.TestLexicon(corpus.BaseResource())
        test = COCARegExpToken("[lemma1|lemma2].[N|V]", lexicon)
        test.parse()
        test = COCARegExpToken("[N|V]", lexicon)
        test.parse()
        """)
    t2 = timeit.Timer("""
        import unittest
        import corpus
        from tokens import *
        lexicon = corpus.TestLexicon(corpus.BaseResource())
        test = COCAToken("[lemma1|lemma2].[N|V]", lexicon)
        test.parse()
        test = COCAToken("[N|V]", lexicon)
        test.parse()
        """)
    
    print(t1.timeit(10000))
    print(t2.timeit(10000))

    
    
    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(TestCOCAToken),
        unittest.TestLoader().loadTestsFromTestCase(TestCOCARegExpToken)])
    unittest.TextTestRunner().run(suite)
