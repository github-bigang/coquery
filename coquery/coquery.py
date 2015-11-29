#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the main module of Coquery.

Copyright (c) 2015 Gero Kunter

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

from __future__ import unicode_literals

import sys
import os.path
import time

import logging
import logging.handlers

from errors import *
import options

try:
    from session import *
except DependencyError as e:
    (str(e))
    sys.exit(1)
    
import __init__

def set_logger():
    logger = logging.getLogger(__init__.NAME)
    logger.setLevel(logging.INFO)
    file_handler = logging.handlers.RotatingFileHandler(os.path.join(os.path.expanduser("~"), "coquery.log"), maxBytes=1024*1024, backupCount=10)
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(message)s"))
    logger.addHandler(file_handler)
    logging.captureWarnings(True)
    return logger

def main():
    logger = set_logger()
    start_time = time.time()
    logger.info("--- Started (%s %s) ---" % (__init__.NAME, __init__.__version__))
    logger.info("{}".format(sys.version))
    try:
        options.process_options()
        options.cfg.log_file_path = os.path.join(os.path.expanduser("~"), "coquery.log")

        # Check if a valid corpus was specified, but only if no GUI is
        # requested (the GUI will handle corpus selection later):
        if not (options.cfg.gui):
            if not options.get_available_resources(options.cfg.current_server):
                raise NoCorpusError

            if not options.cfg.corpus:
                raise NoCorpusSpecifiedError

            if options.cfg.corpus not in options.get_available_resources(options.cfg.current_server):
                raise CorpusUnavailableError(options.cfg.corpus)
            
    except Exception as e:
        print_exception(e)
        sys.exit(1)

    # In verbose mode, debugging messages will be printed as well. Also, all
    # logging messages will be printed to the console, and not only to the 
    # log file.
    if options.cfg.verbose:
        logger.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(message)s"))
        logger.addHandler(stream_handler)
    
    if options.cfg.comment:
        logger.info(options.cfg.comment)
    
    # Run the Application GUI?
    if options.cfg.gui:
        sys.path.append(os.path.join(sys.path[0], "gui"))
        from pyqt_compat import QtGui, QtCore
        from app import CoqueryApp
        from app import GuiHandler

        options.cfg.gui_logger = GuiHandler()
        options.cfg.gui_logger.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(message)s"))
        logger.addHandler(options.cfg.gui_logger)

        options.cfg.app = QtGui.QApplication(sys.argv)
        Coq = CoqueryApp()
        options.cfg.gui = Coq
        options.cfg.gui_logger.setGui(Coq)
        Coq.logo = QtGui.QPixmap("{}/logo/title.png".format(sys.path[0]))
        Coq.show()
        Coq.setGUIDefaults()

        options.cfg.icon = QtGui.QIcon()
        options.cfg.icon.addPixmap(QtGui.QPixmap("{}/logo/logo_tiny.png".format(sys.path[0])))
        Coq.setWindowIcon(options.cfg.icon)
        if options.cfg.profile:
            import cProfile
            cProfile.runctx("options.cfg.app.exec_()", globals(), locals())
        else:
            options.cfg.app.exec_()
        logger.info("--- Finished program (after %.3f seconds) ---" % (time.time() - start_time))

    # Otherwise, run program as a command-line tool:
    else:
        # Choose the appropriate Session type instance:
        if options.cfg.MODE == QUERY_MODE_STATISTICS:
            Session = StatisticsSession()
        else:
            if options.cfg.input_path:
                Session = SessionInputFile()
            elif options.cfg.query_list:
                Session = SessionCommandLine()
            else:
                Session = SessionStdIn()
        
        # Catch keyboard interruptions:
        try:
            # Check if profiling is requested. If so, wrap the profiler 
            # around the query execution:
            if options.cfg.profile:
                import cProfile
                cProfile.runctx("Session.run_queries()", globals(), locals())
            # Otherwise, run queries normally:
            else:
                Session.run_queries()
        except KeyboardInterrupt:
            logger.error("Execution interrupted, exiting.")
        logger.info("--- Done (after %.3f seconds) ---" % (time.time() - start_time))

if __name__ == "__main__":
    for x in sys.argv[1:]:
        if x == "--benchmark":
            import timeit
            benchmark_time = timeit.timeit("main()", setup="from __main__ import main", number=10)
            print("Execution time (25 times): {}".format(benchmark_time))
            sys.exit(0)
    main()

    