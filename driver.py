import getopt
import logging
import sys
import re
from help_me import usage, list
from questions import FULL_QUESTIONS
from csv_parse import CsvParse
from analysis import Analyzer

log = logging.getLogger(__name__)

def main(argv=None):
    #read in params
    if argv is None:
        argv = sys.argv[1:]
    
    file = 'tulalens_survey_sample.csv'
    facet = 'result id'
    
    #standard python parsing for command line options
    opts = []
    args = []

    try:
        opts, args = getopt.getopt(argv, "hl", ["help", "list", "file=", "facet="])
    except getopt.GetoptError as msg:
        print(sys.stderr, msg)
        print >>sys.stderr, "For help use --help"
        return 2
    
    if len(args):
        print >>sys.stderr, "Invalid arg(s) %s"%args
        usage()
        return 2

    for (opt, val) in opts:
        if opt in ("-h", "--help"):
            usage()
            return 0
        if opt in ("-l", "--list"):
            list()
            return 0
        elif opt in ("--file"):
            file = val
        elif opt in ("--facet"):
            facet = val.lower()
        else:
            usage()
            return 2
    
    print("facet: %s" % facet)
    #check if facet given is in the list of survey questions
    #ideally this allows for quick entries with just the 
    #question number, e.g. "--facet Q30"
    long_q = '' #keep track of the long form for later use
    valid_facet = False
    for long, short in FULL_QUESTIONS.items():
        #print("checking question: %s" % question)
        if facet in long:
            #turn the facet into easy to use question ids
            #p = "(^q\d\d?[.]).*"
            #m = re.match(p, long)
            facet = short
            long_q = long
            valid_facet = True
            break
    
    if not valid_facet:
        sys.exit("facet selected is not a survey question")
            
    #parse csv file
    parser = CsvParse(file)
    answers = parser.parse()
    
    #generate analysis based on options
    #print("number of answer rows after parse: %s" % len(answers))
    
    analyze = Analyzer(answers)
    #find the unique occurrence of each answer to the question
    answers_count = analyze.group_by(facet)
    
    
        
    sys.exit()
    
if __name__ == "__main__":
    sys.exit(main())
