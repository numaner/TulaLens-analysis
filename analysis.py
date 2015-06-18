import re
from questions import FULL_QUESTIONS

class Analyzer:
    def __init__(self, data):
        self.facets = FULL_QUESTIONS.keys()
        self.data = data
        
    def group_by(self, facet):
        if facet is not None:
            print("Grouping by facet: %s" % facet)
        else:
            print("No facet selected.")
            return
        #print("first row: %s" % self.data[0])
        #for faceting with result id, we just show how many answers
        #that person has for the survey
        if facet in 'result id':
            for row in self.data:
                print("looking at ID: %s" % row['result id'])
                answer_count = 0
                for question, reply in row.items():
                    if reply is not "":
                        answer_count += 1
                print("questions answered: %s" % answer_count)
        #for other facets, we dig through all answers and find the number
        #of times that question was answered and how many each answer
        #was given
        else:
            #find the full question based on facet given
            for f in self.facets:
                if facet in f:
                    facet = f
                    break
                    
            facet_count = 0
            answers_count = {}
            for row in self.data:
                #print("row: %s" % row)
                if facet in row.keys():
                    #print("id %s has facet %s, answer: %s" % (row['result id'], facet, row[facet]))
                    facet_count += 1
                    #go through the answer array and add each to total counts
                    for answer in row[facet]:
                        if answer not in answers_count:
                            answers_count[answer] = 1
                        else:
                            answers_count[answer] += 1
            print("number of people answered this question: %s" % facet_count)
            for reply, count in answers_count.items():
                print("%s: %s" % (reply, count))
