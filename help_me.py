
def usage():
    print('''
    Tulalens project analysis script version 0.1
    by Nguyen Nguyen
    
    Command: python driver.py [options]
    Sample: python drive.py --file Tulalens_2015_0226-0312.csv --facet q30
    
    Options:
    -h, --help  ==  Displays this help message.
    
    -l, --list  ==  Displays the list of the shortcuts for each question and
                    the longer form associated with it.
                 
    --file      ==  The name of the .csv file to be analyzed. The delimiter 
                    should be a comma ',' and the quote character should be a
                    double quote '"'. If no file is provided the default name
                    to use is "tulalens_survey_sample.csv", which is the survey
                    sample gathered on February 27, 2015, included with the
                    files for this script.
                 
    --facet     ==  The question to be used for analysis. At current version,
                    the script will count the number of people that provided an
                    answer for the given question, and provide how many times
                    each answer was given. If the facet is 'result id', the
                    script will simply show how many answers that person
                    provided for the survey. The option can be just part of a
                    question, but it should still be unique, so you can say
                    "--facet q30" and the script will know it is "Q30. When did
                    you last go to the health center?". If no facet is provided
                    the default for the script to use will be 'result id'.
    ''')
    
def list():
    print("\"id\" : \"result id\",\n"+
    "\"device\" : \"device name\",\n"+
    "\"date\" : \"surveyed date\",\n"+
    "\"time\" : \"surveyed time\",\n"+
    "\"end\" : \"surveyed end date\",\n"+
    "\"q1\" : \"q1. please enter your house address and a landmark\",\n"+
    "\"q2\" : \"q2. please enter the name of the area\",\n"+
    "\"q3\" : \"q3. first name\",\n"+
    "\"q4\" : \"q4. last name\",\n"+
    "\"q5\" : \"q5. husband or father's name\",\n"+
    "\"q6\" : \"q6. age in complete years\",\n"+
    "\"q7\" : \"q7. marital status\",\n"+
    "\"q8\" : \"q8. occupation\",\n"+
    "\"q9\" : \"q9. highest level of education\",\n"+
    "\"q10\" : \"q10. woman's religion\",\n"+
    "\"q11\" : \"q11. what languages do you speak?\",\n"+
    "\"q12\" : \"q12. can you read and write?\",\n"+
    "\"q13\" : \"q13. do you own a mobile phone?\",\n"+
    "\"q14\" : \"q14. does someone in your household own a mobile phone?\",\n"+
    "\"q15\" : \"q15. who owns the mobile phone you use?\",\n"+
    "\"q16\" : \"q16. please share the mobile number\",\n"+
    "\"q17\" : \"q17. what is your individual income per day on average?\",\n"+
    "\"q18\" : \"q18. how many people live in your household right now?\",\n"+
    "\"q19\" : \"q19. what is your household income on average per day?\",\n"+
    "\"q20\" : \"q20. how many children do you have that are alive?\",\n"+
    "\"q21\" : \"q21. are you currently pregnant\",\n"+
    "\"q22\" : \"q22. how many months pregnant are you?\",\n"+
    "\"q23\" : \"q23. have you received prenatal care during this pregnancy at a facility?\",\n"+
    "\"q24\" : \"q24. how many prenatal care visits have you completed in total during this pregnancy?\",\n"+
    "\"q25\" : \"q25. how many months pregnant were you when you first received prenatal care?\",\n"+
    "\"q26\" : \"q26. how many months pregnant were you when you last received prenatal care?\",\n"+
    "\"q27\" : \"q27. what was the date on which you last received prenatal care?\",\n"+
    "\"q28\" : \"q28. which one of the following services did you last go to the facility for in the past two years?\",\n"+
    "\"q29\" : \"q29. if you did not go to the health center for either reason above, why did you last go the health center?\",\n"+
    "\"q30\" : \"q30. when did you last go to the health center?\",\n"+
    "\"q31\" : \"q31. when did the doctor ask you to return to the health center?\",\n"+
    "\"q32\" : \"q32. what was the name of the health facility you last went to?\",\n"+
    "\"q33\" : \"q33. what the address of this health center?\",\n"+
    "\"q34\" : \"q34. how far is this facility from your home in km?\",\n"+
    "\"q35\" : \"q35. what type of facility is this?\",\n"+
    "\"q36\" : \"q36. why did you decide to go to this health facility\",\n"+
    "\"q37\" : \"q37. was a provider present when you arrived at the facility?\",\n"+
    "\"q38\" : \"q38. how many minutes did you spend with the doctor?\",\n"+
    "\"q39\" : \"q39. how many minutes did you spend taking tests?\",\n"+
    "\"q40\" : \"q40. how many minutes did you wait in total?\",\n"+
    "\"q41\" : \"q41. was this waiting time:\",\n"+
    "\"q42\" : \"q42. what type of provider did you see for the consultation?\",\n"+
    "\"q43\" : \"q43. what was the provider's gender?\",\n"+
    "\"q44\" : \"q44. how did the provider treat you?\",\n"+
    "\"q45\" : \"q45. did he/she address all of your issues?\",\n"+
    "\"q46\" : \"q46. did the provider explain what he/she was doing during the check up?\",\n"+
    "\"q47\" : \"q47. did you pay any fee for your services?\",\n"+
    "\"q48\" : \"q48. how much did you pay for the consultation?\",\n"+
    "\"q49\" : \"q49. did you receive diagnostic tests?\",\n"+
    "\"q50\" : \"q50. did you receive diagnostic tests at this facility?\",\n"+
    "\"q51\" : \"q51. how much did you pay for the diagnostic tests?\",\n"+
    "\"q52\" : \"q52. did you receive scanning?\",\n"+
    "\"q53\" : \"q53. did you receive scanning at this facility?\",\n"+
    "\"q54\" : \"q54. how much did you pay for scanning?\",\n"+
    "\"q55\" : \"q55. did you receive other services?\",\n"+
    "\"q56\" : \"q56. what service did you receive?\",\n"+
    "\"q57\" : \"q57. how much did you pay for the other service?\",\n"+
    "\"q58\" : \"q58. in total, how much did you pay for the services you received at this facility only?\",\n"+
    "\"q59\" : \"q59. was the cost:\",\n"+
    "\"q60\" : \"q60. how much did you pay in bribes for services you received?\",\n"+
    "\"q61\" : \"q61. did you have privacy during the exam?\",\n"+
    "\"q62\" : \"q62. were you satisfied with the cleanliness of the facility?\",\n"+
    "\"q63\" : \"q63. how would you rate your overall experience?\",\n"+
    "\"q64\" : \"q64. what did you like about the services?\",\n"+
    "\"q65\" : \"q65. what can be improved at this facility?\",\n"+
    "\"q66\" : \"q66. are you aware of facilities other than this one in your area?\",\n"+
    "\"q67\" : \"q67. how many other facilities?\",\n"+
    "\"q68\" : \"q68. do you have information on the quality of these facilities?\",\n"+
    "\"q69\" : \"q69. where did you get this information?\",\n"+
    "\"q70\" : \"q70. would you like more information on the different facilities and their quality in your area?\",\n"+
    "\"q71\" : \"q71. did the last facility you received care from ask you for your feedback on the quality of care you received?\"")
    
