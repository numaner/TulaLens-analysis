import re
from questions import SHORT_QUESTIONS, QUANTITATIVE

class Analyzer:
    def __init__(self, data):
        self.facets = SHORT_QUESTIONS.values()
        self.data = data
        
    def group_by(self, facet):
        if facet:
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
            #holds the number of people that answered the question
            facet_count = 0
            #holds the unique answers mapped to their occurence
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
        
        return answers_count
        
    def find_mean(self, facet, answers_count):
        if facet:
            if facet in QUANTITATIVE:
                print("Finding the mean for quantifiable facet: %s" % facet)
            else:
                print("Not a quantitative facet: %s" % facet)
        else:
            print("No facet selected.")
            return
        
        #to find the sum of all the answers, we have to first multiply a unique
        #answer by how many times it was given. along the way we keep a running
        #total of number of answers
        sum = 0
        total_answers = 0
        for answer, count in answers_count.items():
            total_answers += count
            sum += int(answer) * int(count)
            
        mean = sum / total_answers
        
        print("Sum / Total answers = mean")
        print("%s / %s = %s" % (sum, total_answers, mean))
        
        return mean