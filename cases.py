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
