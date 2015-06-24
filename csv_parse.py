import sys
import csv
import io
from questions import SHORT_QUESTIONS, MULTICHOICE

class CsvParse:
    def __init__(self, file=''):
        #the survey results as initially read from the csv
        self.results = None
        #an array of the survey rows, each row is a dictionary
        #of the questions and their answers for that person
        self.answers = []
        
        try:
            csv_file = io.open(file, 'r')
        except IOError as e:
            print("Error: %s" % e.strerror)
            sys.exit(2)
            
        self.results = csv.reader(csv_file, delimiter=',', quotechar='"')

    def parse(self):
        #first row should be the questions
        header = next(self.results)
        #print(header)

        #keep track of the questions and the range the answers should be in
        answer_ranges = {}

        #to keep track of where in the row each question and its answer(s) could be,
        #get the index of the question, and count its multi-choice answers if exist.
        #this provides a range to find the answer in for the answer rows.
        #print(header)
        for question in header:
            #print(question.lower())
            if question.lower() in SHORT_QUESTIONS.keys():
                short_q = SHORT_QUESTIONS[question.lower()]
                question_index = header.index(question)
                #print("'%s' is at index %s" % (question, question_index))
                answer_range = 0
                if short_q in MULTICHOICE:
                    answer_range = len(MULTICHOICE[short_q])
                #print("answer should be at index")
                if answer_range > 0:
                    for index in range(question_index, question_index + answer_range):
                        answer_ranges[index] = short_q
                        #print(index)
                else:
                    answer_ranges[question_index] = short_q
                    #print(question_index)
        #print(answer_ranges)

        #skipping the row with choices, but putting them in choices to use if needed
        choices = next(self.results)
        #print(choices)

        #print("compiling survey into answers map")
        count = 0
        for result in self.results:
            #skip blank rows
            if result[0] is "":
                #print("skipping blank row")
                continue
            #this dict keeps a 1:1 relationship of questions and answers and sidesteps
            #the multi-choice. each mapping should be at least { question : [answer] }
            survey_row = {}
            #print("at id %s" % result[0])
            count += 1
            for index, answer in enumerate(result):
                if answer is not "":
                    #print("index: %s" % index)
                    if index in answer_ranges:
                        curr_question = answer_ranges[index]
                        if curr_question not in survey_row:
                            survey_row[curr_question] = []
                        survey_row[curr_question].append(answer)
                        #print("at index %s: %s -> %s" % (index, curr_question, survey_row[curr_question]))
            self.answers.append(survey_row)

        print("Number of participants: %s" % count)
        #print("number of answer rows: %s" % len(self.answers))
        
        return self.answers
