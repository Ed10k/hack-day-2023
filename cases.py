#import statements
import openai
import os 
import random
import boto3


##########################
# Keyword Search Function
##########################
def keywordSearch(keyword, caseDescriptions):
    similarCases = []
    # Iterate through each case description
    for caseDescription in caseDescriptions:
        # Convert both keyword and case description to lowercase cus keyword search is case sensitive :(
        if keyword.lower() in caseDescription.lower():
            similarCases.append(caseDescription)
    return similarCases


# caseDescriptions = ["Testing", "no testing", "bee"]
# keyword = "tes"



#Aws stuff 
s3_client = boto3.client('s3')


class Casey:
    def __init__(self, apikey):
        self.model = "gpt-3.5-turbo"
        self.apiKey = apikey
        api = openai_key = os.getenv(apikey)
    

    def getdescription(self,content):
        response = openai.Completion.create(
            model = self.model,
            messages = [{"role" : "user", "contetnt": content}],
            function = [
                {

                }
            ]

            
        )
        



class Case:
    def __init__(self, name, subject):
        self.caseOwner = name
        self.subject = subject
        self.caseNum
        self.status
        self.priority
        self.description

    #Setters
    #function to set up the case number 
    def setCaseNum(self):
        self.CaseNum = int(random.random(0,1000))
        return self.CaseNum
    
    #function to set the case description 
    def setCaseDesc(self, description):
        self.descripton = description


    #function to set priority 
    def setPriority(self, priority):
        self.priority = priority

    #function to 







