# -*- coding: utf-8 -*-
"""
FILENAME: session.py -- part of Coquery corpus query tool

This module defines the Session class.

LICENSE:
Copyright (c) 2015 Gero Kunter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from __future__ import print_function
import sys
import csv
import copy
import time
import fileinput

import __init__
import options
from errors import *
from corpus import *
from defines import *

import queries
import tokens
import imp

import logging


class ConsoleCSV (object):
    def writerow (self, Row):
        L = []
        for x in Row:
            S = str (x)
            if options.cfg.output_separator in S:
                L.append ("'%s'" % S)
            elif "'" in S:
                L.append ('"%s"' % S)
            else:
                L.append (S)
                
        if options.cfg.output_separator == "\\t":
            options.cfg.output_separator = "\t"
        print(options.cfg.output_separator.join (L))

class Session(object):
    def __init__(self):
        self.header = None
        self.max_number_of_input_columns = 0
        self.max_number_of_tokens = 0
        self.query_list = []
        self.query_column_number = 0
        
        # load current corpus module depending on the value of options.cfg.corpus,
        # i.e. the corpus specified as an argumment:        
        current_corpus = options.cfg.corpora[options.cfg.corpus]
        corpus_name, ext = os.path.splitext(os.path.basename(current_corpus))
        module = imp.load_source(corpus_name, current_corpus)
        current_resource = module.Resource()
        self.Corpus = module.Corpus(module.Lexicon(current_resource), current_resource)
        #self.Corpus = module.Corpus(module.Lexicon(module.Resource), module.Resource)

        self.show_header = options.cfg.show_header

        # select the query class depending on the value of options.cfg.MODE, i.e.
        # which mode has been specified in the options:
        if options.cfg.MODE == QUERY_MODE_FREQUENCIES:
            self.query_type = queries.FrequencyQuery
        elif options.cfg.MODE == QUERY_MODE_TOKENS:
            self.query_type = queries.TokenQuery
        elif options.cfg.MODE == QUERY_MODE_DISTINCT:
            self.query_type = queries.DistinctQuery
            

        logger.info("Using corpus %s" % options.cfg.corpus)
        self.output_file = None

    def expand_header(self):
        """
        Session.expand_header() ensures that the list Session.header 
        contains all column labels that are required for the current 
        session. The set of labels depends on the command line flags. For 
        example, -p adds one or more numbered part-of-speech labels to the 
        header. The number of labels depends on the maximum number of query 
        tokens in this session. """
    
        ColumnNumbers = range (self.max_number_of_input_columns)
        
        if not self.header:
            # If there is no header yet (e.g. because the input file did not
            # contain headsers, create a new header with column labels 'Inputx'
            # for the maximum number of input columns available, with x 
            # corresponding to the number of the column.
            # The column containing the query string is labelled 'Query'.
            self.header = ["Input%s" % (x+1) for x in ColumnNumbers]
            if options.cfg.show_query:
                self.header.insert (options.cfg.query_column_number - 1, "Query")
        
        if options.cfg.show_parameters:
            self.header.append ("Parameters")
            
        if options.cfg.source_filter:
            self.header.append ("Filter")
        
        if options.cfg.show_id:
            self.header.append("ID")
            
        if options.cfg.show_orth:
            self.header += ["W%s" % (x+1) for x in range(self.max_number_of_tokens)]

        if options.cfg.show_phon and self.Corpus.provides_feature(LEX_PHON):
            self.header += ["W_Phon%s" % (x+1) for x in range(self.max_number_of_tokens)]
            
        if options.cfg.show_lemma and self.Corpus.provides_feature(LEX_LEMMA):
            self.header += ["L%s" % (x + 1) for x in range(self.max_number_of_tokens)]
            
        if options.cfg.show_pos and self.Corpus.provides_feature(LEX_POS):
            self.header += ["PoS%s" % (x + 1) for x in range(self.max_number_of_tokens)]
        
        if options.cfg.show_text and self.Corpus.provides_feature(CORP_SOURCE):
            self.header += self.Corpus.get_source_info_headers()
        if options.cfg.show_speaker and self.Corpus.provides_feature(CORP_SPEAKER):
            self.header += self.Corpus.get_speaker_info_headers()
        if options.cfg.show_filename and self.Corpus.provides_feature(CORP_FILENAME):
            self.header += self.Corpus.get_file_info_headers()
        if options.cfg.show_time and self.Corpus.provides_feature(CORP_TIMING):
            self.header += self.Corpus.get_time_info_headers()
            
        if options.cfg.context_span and self.Corpus.provides_feature(CORP_CONTEXT):
            self.header += self.Corpus.get_context_headers(options.cfg.context_span, self.max_number_of_tokens, options.cfg.separate_columns)

        if options.cfg.MODE == QUERY_MODE_FREQUENCIES:
            self.header.append (options.cfg.freq_label)

    def open_output_file(self):
        if self.output_file:
            return
        if not options.cfg.output_path:
            self.output_file = ConsoleCSV ()
        else:
            if options.cfg.append:
                FileMode = "at"
            else:
                FileMode = "wt"
            self.output_file = csv.writer(open(options.cfg.output_path, FileMode), delimiter=options.cfg.output_separator)
        if not options.cfg.append and self.show_header:
            self.expand_header()
            self.output_file.writerow (self.header)
        
    def run_queries(self):
        for current_query in self.query_list:
            start_time = time.time()
            if current_query.tokens:
                self.Corpus.run_query(current_query)
            logger.info("Query executed (%.3f seconds)" % (time.time() - start_time))

            # output result of current query:
            if not options.cfg.dry_run:
                if not self.output_file:
                    self.open_output_file()
                start_time = time.time()
                current_query.write_results(self.output_file, self.max_number_of_tokens)
                logger.info("Results written (%.3f seconds)" % (time.time() - start_time))

class StatisticsSession(Session):
    def __init__(self):
        super(StatisticsSession, self).__init__()
        if self.Corpus.provides_feature(CORP_STATISTICS):
            self.query_list.append(queries.StatisticsQuery(self.Corpus))
            self.show_header = False
        else:
            raise QueryModeError(options.cfg.corpus, options.cfg.MODE)

class SessionCommandLine(Session):
    def __init__(self):
        super(SessionCommandLine, self).__init__()
        if len(options.cfg.query_list) == 1:
            S = "Query"
        else:
            S = "%s queries" % len(options.cfg.query_list)
        logger.info("%s provided at command line (%s)" % (S, ", ".join(options.cfg.query_list)))
        for query_string in options.cfg.query_list:
            if self.query_type:
                new_query = self.query_type(query_string, self.Corpus, tokens.COCAToken, options.cfg.source_filter)
            else: 
                raise CorpusUnavailableQueryTypeError(options.cfg.corpus, options.cfg.MODE)
            self.query_list.append(new_query)
            self.max_number_of_tokens = max(new_query.number_of_tokens, self.max_number_of_tokens)
        self.max_number_of_input_columns = 0
        self.query_column_number = 1

class SessionInputFile(Session):
    def __init__(self):
        super(SessionInputFile, self).__init__()

        if options.cfg.skip_lines:
            S = "query" if options.cfg.skip_lines == 1 else "queries"
            logger.info("Skipping first %s %s." % (options.cfg.skip_lines, S))
            
        with open(options.cfg.input_path, "rt") as InputFile:
            read_lines = 0
            for CurrentLine in csv.reader(InputFile, delimiter=options.cfg.input_separator):
                if CurrentLine:
                    if options.cfg.query_column_number > len(CurrentLine):
                        raise IllegalArgumentError("Column number for queries too big (-n %s)" % options.cfg.query_column_number)
                    if options.cfg.file_has_headers and not self.header:
                        self.header = CurrentLine
                        if not options.cfg.show_query:
                            self.header.pop(options.cfg.query_column_number - 1)
                    else:
                        if read_lines >= options.cfg.skip_lines:
                            query_string = CurrentLine.pop(options.cfg.query_column_number - 1)
                            new_query = self.query_type(
                                    query_string, self.Corpus,
                                    tokens.COCAToken,
                                    options.cfg.source_filter)
                            new_query.InputLine = copy.copy(CurrentLine)
                            self.query_list.append(new_query)
                            self.max_number_of_tokens = max(new_query.number_of_tokens, self.max_number_of_tokens)
                    self.max_number_of_input_columns = max(len(CurrentLine), self.max_number_of_input_columns)
                read_lines += 1
        logger.info("Input file scanned, %s queries" % len (self.query_list))

class SessionStdIn(Session):
    def __init__(self):
        super(SessionStdIn, self).__init__()

        if options.cfg.skip_lines:
            S = "query" if options.cfg.skip_lines == 1 else "queries"
            logger.info("Skipping first %s %s." % (options.cfg.skip_lines, S))
            
        for current_string in fileinput.input("-"):
            read_lines = 0
            current_line = [x.strip() for x in current_string.split(options.cfg.input_separator)]
            if current_line:
                if options.cfg.file_has_headers and not self.header:
                    self.header = current_line
                else:
                    if read_lines >= options.cfg.skip_lines:
                        query_string = current_line.pop(options.cfg.query_column_number - 1)
                        new_query = self.query_type(
                                query_string, self.Corpus, tokens.COCAToken, options.cfg.source_filter)
                        
                        new_query.InputLine = copy.copy(current_line)
                        self.query_list.append(new_query)
                        self.max_number_of_tokens = max(new_query.number_of_tokens, self.max_number_of_tokens)
                self.max_number_of_input_columns = max(len(current_line), self.max_number_of_input_columns)
            read_lines += 1
        logger.info("Command line scanned, %s queries" % len (self.query_list))
    

logger = logging.getLogger(__init__.NAME)

