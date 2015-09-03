from __future__ import unicode_literals

from corpusbuilder import *
import codecs

class CMUdictBuilder(BaseCorpusBuilder):
    encoding = "latin-1"
    
    def __init__(self):
        # all corpus builders have to call the inherited __init__ function:
        super(CMUdictBuilder, self).__init__()
        
        # Add table descriptions for the table used in this database.
        #
        # Every table has a primary key that uniquely identifies each entry
        # in the table. This primary key is used to link an entry from one
        # table to an entry from another table. The name of the primary key
        # stored in a string is given as the second argument to the function
        # add_table_description().
        #
        # A table description is a dictionary with at least a 'CREATE' key
        # which takes a list of strings as its value. Each of these strings
        # represents a MySQL instruction that is used to create the table.
        # Typically, this instruction is a column specification, but you can
        # also add other table options for this table. Note that the primary
        # key cannot be set manually.
        # 
        # Add the dictionary table. Each row in this table represents a 
        # dictionary entry. Internally, it double-functions both as the
        # corpus table (which is required to run queries in the first place)
        # and the lexicon table (which is required for word look-up). It
        # has the following columns:
        # 
        # WordId
        # An int value containing the unique identifier of the lexicon
        # entry associated with this token.
        #
        # Text
        # A string value containing the orthographic form of the token.
        # Transcript
        # A string value containing the phonological transcription using
        # ARPAbet.

        
        self.corpus_table = "dict"
        self.corpus_id = "WordId"
        self.corpus_word_id = "WordId"
        self.word_table = "dict"
        self.word_id = "WordId"
        self.word_label = "Text"
        self.word_transcript = "Transcript"
        
        self.create_table_description(self.word_table,
            [Primary(self.corpus_id, "MEDIUMINT(6) UNSIGNED NOT NULL"),
             Column(self.word_label, "VARCHAR(50) NOT NULL"),
             Column(self.word_transcript, "VARCHAR(100) NOT NULL")])

    def build_load_files(self):
        with codecs.open(self.arguments.path, "r", encoding = self.arguments.encoding) as input_file:
            for word_id, current_line in enumerate(input_file):
                current_line = current_line.strip()
                if current_line and not current_line.startswith (";;;"):
                    word, transcript = current_line.split ("  ")
                    self.table_add(self.word_table, 
                        {self.word_id: word_id,
                         self.word_label: word, 
                         self.word_transcript: transcript})
        self.Con.commit()

    def get_title(self):
        return "Carnegie Mellon Pronouncing Dictionary (CMUdict)"

    def get_url(self):
        return 'http://www.speech.cs.cmu.edu/cgi-bin/cmudict'
                    
    def get_description(self):
        return ["The Carnegie Mellon Pronouncing Dictionary (CMUdict) is a dictionary containing approximately 135.000 English word-forms and their phonemic transcriptions, using a variant of the Arpabet transcription system.", "CMUdict is freely available under a BSD license."]

if __name__ == "__main__":
    CMUdictBuilder().build()
    