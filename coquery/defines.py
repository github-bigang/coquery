# -*- coding: utf-8 -*-
"""
defines.py is part of Coquery.

Copyright (c) 2015 Gero Kunter (gero.kunter@coquery.org)

Coquery is released under the terms of the GNU General Public License.
For details, see the file LICENSE that you should have received along 
with Coquery. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import unicode_literals
from __future__ import print_function

import sys
import math
import itertools
import re
import textwrap

DEFAULT_MISSING_VALUE = "<NA>"

# The following labels are used to refer to the different types of query 
# tokens, e.g. in corpusbuilder.py when mapping the different query item
# types to different fields in the data base:
QUERY_ITEM_WORD = "query_item_word"
QUERY_ITEM_LEMMA = "query_item_lemma"
QUERY_ITEM_TRANSCRIPT = "query_item_transcript"
QUERY_ITEM_POS = "query_item_pos"
QUERY_ITEM_GLOSS = "query_item_gloss"

QUERY_MODE_TOKENS = "TOKEN"
QUERY_MODE_FREQUENCIES = "FREQ"
QUERY_MODE_DISTINCT = "DISTINCT"
QUERY_MODE_STATISTICS = "STATS"
QUERY_MODE_COLLOCATIONS = "COLLOCATE"
QUERY_MODE_CONTINGENCY = "CONTINGENCY"

SORT_NONE = 0
SORT_INC = 1
SORT_DEC = 2
SORT_REV_INC = 3
SORT_REV_DEC = 4

CONTEXT_NONE = "None"
CONTEXT_KWIC = "KWIC"
CONTEXT_STRING = "String"
CONTEXT_COLUMNS = "Columns"
CONTEXT_SENTENCE = "Sentence"

# These labels are used in the corpus manager:
INSTALLER_DEFAULT = "Default corpus installers"
INSTALLER_CUSTOM = "Downloaded corpus installers"
INSTALLER_ADHOC = "User corpora"

COLUMN_NAMES = {
    # Labels that are used in the Collocations aggregation:
    "coq_context_left": "Left context",
    "coq_context_right": "Right context",
    "coq_context_string": "Context",
    "coq_collocate_label": "Collocate",
    #"coq_collocate_lemma_label": "Collocate lemma",
    "coq_collocate_frequency": "Collocate frequency",
    "coq_collocate_frequency_left": "Left context frequency",
    "coq_collocate_frequency_right": "Right context frequency",
    "coq_mutual_information": "Mutual information",
    "coq_conditional_probability": "Pcond",

    # Labels that are used in the Coquery special table:
    "coquery_query_token": "Query token",
    "coquery_expanded_query_string": "Matched query string",
    "coquery_query_string": "Query string",

    # Labels that are used in the Statistics special table:
    "statistics_frequency": "Frequency", 
    "statistics_overall_proportion": "Overall proportion",
    "statistics_overall_entropy": "Overall entropy",
    "statistics_query_proportion": "Query proportion",
    "statistics_per_million_words": "Frequency (pmw)",
    "statistics_query_entropy": "Query entropy",
    "statistics_column_total": "ALL",

    # Labels that are used when displaying the corpus statistics:
    "coq_statistics_table": "Table",
    "coq_statistics_column": "Column",
    "coq_statistics_entries": "Entries",
    "coq_statistics_uniques": "Uniques",
    "coq_statistics_uniquenessratio": "Uniqueness ratio",
    "coq_statistics_averagefrequency": "Average frequency",

        }

DEFAULT_CONFIGURATION = "Default"

SQL_MYSQL = "mysql"
SQL_SQLITE = "sqlite"

SQL_ENGINES = [SQL_MYSQL, SQL_SQLITE]

# for Python 3 compatibility:
try:
    unicode()
except NameError:
    # Python 3 does not have unicode and long, so define them here:
    unicode = str
    long = int

msg_invalid_filter = """
<p><b>The corpus filter '{}' is not valid.</b></p>
<p>One of your filters is not not valid for the currently selected corpus.
Please either disable using corpus filter from the Preferences menu, or 
delete the invalid filter from the filter list.</p>
"""
msg_clear_filters = """
<p><b>You have requested to reset the list of corpus filters.</b></p>
<p>Click <b>Yes</b> if you really want to delete all filters in the list,
or <b>No</b> if you want to leave the stop word list unchanged.</p>
"""
msg_clear_stopwords = """
<p><b>You have requested to reset the list of stop words.</b></p>
<p>Click <b>Yes</b> if you really want to delete all stop words in the list,
or <b>No</b> if you want to leave the stop word list unchanged.</p>
"""
msg_missing_modules = """
<p><b>Not all required Python modules could be found.</b></p>
<p>Some of the Python modules that are required to run and use Coquery could 
not be located on your system. The missing modules are:</p>
<p><code>\t{}</code></p>
<p>Please refer to <a href="http://coquery.org/documentation/">http://coquery.org/documentation</a>
for instructions on how to install the required modules.</p>
"""
msg_missing_seaborn_module = """
<p><b>One of the required Python module could not be loaded.</b></p>
<p>The Python module called 'seaborn' does not appear to be installed on this 
computer. Without this module, the visualization functions are not available.</p>
<p>Please visit the Seaborn website for installation instructions:
<a href="http://stanford.edu/~mwaskom/software/seaborn/index.html">http://stanford.edu/~mwaskom/software/seaborn/index.html</a>.
</p>
"""
msg_visualization_error = """
<p><b>An error occurred while plotting.</b></p>
<p>While plotting the visualization, the following error was encountered:</p>
<p><code>{}</code></p>
<p>The visualization may be incorrect. Please contact the Coquery maintainers.</p>
"""
msg_no_lemma_information = """
<p><b>The current resource does not provide lemma information.</b></p>
<p>Your last query makes use of the lemma search syntax by enclosing query 
tokens in square brackets <code>[...]</code>, but the current resource does 
not provide lemmatized word entries.</p>
<p>Please change your query, for example by removing the square brackets 
around the query token.</p>
"""
msg_corpus_path_not_valid = """
<p><b>The corpus data path does not seem to be valid.</b></p>
<p>{}</p>
<p>If you choose to <b>ignore</b> that the corpus data path is invalid, 
Coquery will start the corpus installation using this directiory. After the 
installation, you mioght still be able to use the corpus, but it might be 
incomplete.</p>
<p>If you choose to <b>discard</b> the invalid corpus data path, you can 
enter the correct data path in the previous dialog, or cancel the corpus 
installation altogether.</p>
<p>Do you wish to ignore or to discard the invalid corpus data path?</p>
"""
msg_mysql_no_configuration = """
<p><b>No database server configuration is available.</b></p>
<p>You haven't specified the configuration for your database server yet.
Please call 'Database servers...' from the Preferences menu, and set up a 
configuration for your MySQL database server.</p>
<p>If you need assistance setting up your database server, call 'MySQL
server help' from the Help menu.</p>
"""
msg_warning_statistics = """
<p><b>You have unsaved data in the results table.</b></p>
<p>The corpus statistics will discard the results table from your last 
query.</p>
<p>If you want to retrieve that results table later, you will have to 
run the query again.</p>
<p>Do you wish to continue?</p>
"""
msg_no_context_available = """
<p><b>Context information is not available.</b></p>
<p>There is no context information available for the item that you have 
selected.</p>"""
msg_corpus_no_documentation = """
<p><b>Corpus documentation for corpus '{corpus}' is not available.</b></p>
<p>The corpus module '{corpus}' does not provide a link to the corpus
documentation. You may find help on how the corpus is structured by using an
internet search engine.</p>"""
msg_install_abort = """
<p><b>You have requested to abort the installation.</b></p>
<p>The installation has not been completed yet. If you abort now, the data 
installed so far will be discarded, and the corpus will still not be 
available for queries.</p>"""
msg_invalid_installer = """
<p><b>The corpus installer '{name}' contains invalid code.</b></p>
<p>{code}</p>
<p>Please note that running an invalid corpus installer can potentially be 
a security risk. For this reason, the corpus installer was disabled.</p>
"""

msg_validated_install = """
<p><b>You have requested the installation of the corpus '{corpus}'.</b></p>
<p>The Coquery website stores validation codes for all corpus installers that 
have passed a security screening. During this screening, the installer code is 
manually scanned for instructions that may be harmful to your computer, 
software, or privacy.</p>
<p>The installer '{corpus}' has been validated. This means that the Coquery 
maintainers do not consider it to be a security risk, but please note that 
the Coquery maintainers cannot be held liable for damages arising out of the
use of this installer. See Section 16 of the 
<a href="http://www.gnu.org/licenses/gpl-3.0.en.html">GNU General Public License 
</a> for details.</p>
<p>Click <b>Yes</b> to proceed with the installation, or <b>No</b> to abort it.
</p>
"""

msg_failed_validation_install = """
<p><b>The validation of the corpus installer '{corpus}' failed.</b></p>
<p>The Coquery website stores validation codes for all corpus installers that 
have passed a security screening. During this screening, the installer code is 
manually scanned for instructions that may be harmful to your computer, 
software, or privacy.</p>
<p>The validation of the installer '{corpus}' failed. This means that your 
copy of the installer does not match any copy of the installer that has been 
validated by the Coquery maintainers. Please note that 
the Coquery maintainers cannot be held liable for damages arising out of the
use of this installer. See Section 16 of the 
<a href="http://www.gnu.org/licenses/gpl-3.0.en.html">GNU General Public License 
</a> for details.</p>
<p><b>You are advised to proceed with the installation only if you are certain 
that the installer is from a trustworthy source.</b></p>
<p>Click <b>Yes</b> to proceed with the installation, or <b>No</b> to abort it.
</p>
"""
msg_unvalidated_install = """
<p><b>The corpus installer '{corpus}' could not be validated.</b></p>
<p>The Coquery website stores validation codes for all corpus installers that 
have passed a security screening. During this screening, the installer code is 
manually scanned for instructions that may be harmful to your computer, 
software, or privacy.</p>
<p>For the installer '{corpus}', no validation code is available. This means 
either that the installer has not yet been submitted to the screening process, 
or that no validation code could be fetched from the Coquery website. Please 
note that the Coquery maintainers cannot be held liable for damages arising 
out of the use of this installer. See Section 16 of the 
<a href="http://www.gnu.org/licenses/gpl-3.0.en.html">GNU General Public License 
</a> for details.</p>
<p><b>You are advised to proceed with the installation only if you are certain 
that the installer is from a trustworthy source.</b></p>
<p>Click <b>Yes</b> to proceed with the installation, or <b>No</b> to abort it.
</p>
"""

msg_rejected_install = """
<p><b>The corpus installer '{corpus}' may be a security risk.</b></p>
<p>The Coquery website stores validation codes for all corpus installers that 
have passed a security screening. During this screening, the installer code is 
manually scanned for instructions that may be harmful to your computer, 
software, or privacy.</p>
<p>The corpus installer '{corpus}' has been <b>rejected</b> during this 
screening process. This means that the Coquery maintainers considered the 
installer to be potentially harmful. Please note that 
the Coquery maintainers cannot be held liable for damages arising out of the
use of this installer. See Section 16 of the 
<a href="http://www.gnu.org/licenses/gpl-3.0.en.html">GNU General Public License 
</a> for details.</p>
<p><b>You are strongly advised not to continue with the installation of this 
corpus.</b></p>
<p>If you with to ignore this warning, click <b>Yes</b> to continue with the 
istallation. Click <b>No</b> if you wish to abort the installation of this
corpus.</p>
"""

msg_corpus_broken = """
<p><b>An error occurred while reading the installer '{name}'</b></p>
<p>The corpus installer stored in the file {name} could not be read. Most 
likely, there is a programming error in the installer, or the file could 
not be read.</p>
<p>Please inform the maintainer of this corpus installer of your problem. 
When doing so, include the following information in your message:</p>
{type}
{code}"""
msg_disk_error = """
<p><b>An error occurred while accessing the disk storage.</b></p>
<p>The results have not been saved. Please try again. If the error persists, 
try saving to a different location</p>"""
msg_encoding_error = """
<p><b>An encoding error occurred while trying to save the results.</b></p>
<p><span color="darkred">The save file is probably incomplete.</span></p>
<p>At least one column contains special characters which could not be 
translated to a format that can be written to a file. You may try to work 
around this issue by reducing the number of output columns so that the 
offending character is not in the output anymore.</p>
<p>We apologize for this problem. Please do not hesitate to contact the 
authors about it so that the problem may be fixed in a future 
version.</p>"""
msg_query_running = """
<p><b>The last query is still running.</b></p>
<p>If you interrupt it, the results that have been retrieved so far will be discarded.</p>
<p>Do you really want to interrupt this query?</p>"""
msg_filename_error = """
<p><b>The file name is not valid.</b></p>
<p>You have chosen to read the query strings from a file, but the query file 
name that you have entered is not valid. Please enter a valid query file 
name, or select a file by pressing the Open button.</p>"""
msg_initialization_error = """
<p><b>An error occurred while initializing the database {code}.</b></p>
<p>Possible reasons include:
<ul><li>The database server is not running.</li>
<li>The host name or the server port are incorrect.</li>
<li>The user name or password are incorrect, or the user has insufficient
privileges.</li>
<li>You are trying to access a local database on a remote server, or vice
versa.</li>
</ul></p>
<p>Open <b>Database connections </b> in the Preferences menu to check whether 
the connection to the database server is working, and if the settings are 
correct.</p>"""
msg_corpus_remove = """
<p><b>You have requested to remove the corpus '{corpus}'.</b></p>
<p>This step cannot be reverted. If you proceed, the corpus will not be 
available for further queries before you install it again.</p>
<p>Removing '{corpus}' will free approximately {size:.1S} of disk space.</p>
<p>Do you really want to remove the corpus?</p>"""
msg_remove_corpus_error = """
<p><b>A database error occurred while deleting the corpus '{corpus}'.</b></p>
<p>The corpus was <b>not</b> removed.</p>
<p>The database connection returned the following error message:</p>
<p><code>{code}</code></p>
<p>Please verify that the MySQL privileges for the current user allow you to
delete databases.</p>
"""
msg_remove_corpus_disk_error = """
<p><b>A disk error occurred while deleting the corpus database.</b></p>
<p>Please try removing the corpus another time. If the problem persists, 
use your system tools to ensure that the storage device is fully
operational.</p>"""
msg_unsaved_data = """
<p><b>The last query results have not been saved.</b></p>
<p>If you quit now, they will be lost.</p>
<p>Do you really want to quit?</p>"""
msg_no_corpus = """
<p>Coquery could not find a corpus module. Without a corpus module, you cannot 
run any query.</p>"""
msg_details = """
<p>To build a new corpus module from a selection of text files, select 
<b>Build new corpus...</b> from the Corpus menu.</p>
<p>To install the corpus module for one of the corpora that are supported by
Coquery, select <b>Manage corpora...</b> from the Corpus menu.</p>"""

gui_label_query_button = "&Query"
gui_label_stop_button = "&Stop"

def printex(exc, *args, **kwargs):
    """
    Prints the exception string. XML tags are stripped.
    """
    l = [x.strip() for x in str(exc).split("</p>")]
    
    for par in [x.strip(" ") for x in str(exc).split("</p>") if x.strip(" ")]:
        par = par.replace("\n", " ").strip(" ")
        par = par.replace("  ", " ")
        print("\n".join(
            textwrap.wrap(re.sub('<[^>]*>', '', par), width=70, replace_whitespace=False)), 
            *args, **kwargs)
        print("")

class FileSize(long):
    """ Define a long class that can store file sizes, and which allows
    custom formatting by using the format specifier S, which displays a 
    human-readable file size with suffixes b, kb, Mb etc.
    Adapted from http://code.activestate.com/recipes/578321-human-readable-filememory-sizes/
    """
    def __format__(self, fmt):
        if self < 0:
            return "(unknown)"
        if fmt == "" or fmt[-1] != "S":
            if fmt[-1].tolower() in ['b','c','d','o','x','n','e','f','g','%']:
                # Numeric format.
                return long(self).__format__(fmt)
            else:
                return str(self).__format__(fmt)

        val, suffixes = float(self), ["b ","Kb","Mb","Gb","Tb","Pb"]
        if val < 1:
            # Can't take log(0) in any base.
            i, v = 0, 0
            exp = 0
        else:
            exp = int(math.log(val,1024))+1
            v = val / math.pow(1024, exp)
            # Move to the next bigger suffix when the value is large enough:
            v, exp = (v, exp) if v > 0.5 else (v * 1024, exp - 1)
        return ("{0:{1}f}" + suffixes[exp]).format(v, fmt[:-1])

def dict_product(d):
    """ Create a Cartesian product of the lists stored as values in the
    dictionary 'd'.
    
    This product is useful for example to create a table of all factor level
    combinations. The factor levels can be accessed by the column names. """
    
    cart_product = itertools.product(*d.itervalues())
    
    return (dict(itertools.izip(d, x)) for x in cart_product)


#resource_list = ResourceList()

def memory_dump():
    import gc
    x = 0
    for obj in gc.get_objects():
        i = id(obj)
        size = sys.getsizeof(obj, 0)
        # referrers = [id(o) for o in gc.get_referrers(obj)]
        try:
            cls = str(obj.__class__)
        except:
            cls = "<no class>"
        if size > 1024 * 50:
            referents = set([id(o) for o in gc.get_referents(obj)])
            x += 1
            print(x, {'id': i, 'class': cls, 'size': size, "ref": len(referents)})
            #if len(referents) < 2000:
                #print(obj)

