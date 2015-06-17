import getopt
import logging
import sys
from questions import CSV_QUESTIONS
from csv_parse import CsvParse
from analysis import Analyzer

log = logging.getLogger(__name__)

def usage():
    print('''
    Tulalens project analysis script version 0.1
    by Nguyen Nguyen
    
    Command: python driver.py [options]
    Sample: python drive.py --file Tulalens_2015_0226-0312.csv --facet q30
    
    Options:
    -h       ==  Displays this help message.
    
    --file   ==  The name of the .csv file to be analyzed. The delimiter should
                 be a comma ',' and the quote character should be a double
                 quote '"'. If no file is provided the default name to use is
                 "tulalens_survey_sample.csv", which is the survey sample gathered
                 on February 27, 2015, included with the files for this script.
                 
    --facet  ==  The question to be used for analysis. At current version, the
                 script will count the number of people that provided an answer
                 for the given question, and provide how many times each answer
                 was given. If the facet is 'result id', the script will simply
                 show how many answers that person provided for the survey.
                 The option can be just part of a question, but it should still
                 be unique, so you can say "--facet q30" and the script will
                 know it is "Q30. When did you last go to the health center?".
                 If no facet is provided the default for the script to use will
                 be 'result id'.
    ''')
    
def main(argv=None):
    #read in params
    if argv is None:
        argv = sys.argv[1:]
    
    file = 'tulalens_survey.csv'
    facet = 'result id'
    
    #standard python parsing for command line options
    opts = []
    args = []

    try:
        opts, args = getopt.getopt(argv, "h", ["help", "file=", "facet="])
    except getopt.GetoptError as msg:
        print(sys.stderr, msg)
        print >>sys.stderr, "for help use --help"
        return 2
    
    if len(args):
        print >>sys.stderr, "Invalid arg(s) %s"%args
        usage()
        return 2

    for (opt, val) in opts:
        if opt in ("-h", "--help"):
            usage()
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
    facet_valid = False
    for question in sorted(CSV_QUESTIONS.keys()):
        #print("checking question: %s" % question)
        if facet in question:
            facet = question
            facet_valid = True
            break
    
    if not facet_valid:
        sys.exit("facet selected is not a survey question")
            
    #parse csv file
    parser = CsvParse(file)
    answers = parser.parse()
    
    #generate analysis based on options
    
    #print("number of answer rows after parse: %s" % len(answers))
    analyze = Analyzer(answers)
    
    analyze.group_by(facet)
        
    sys.exit()
    
if __name__ == "__main__":
    sys.exit(main())
