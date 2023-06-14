caseDescriptions = ["Case description 1", "Case description 2", "Case description 3"]
keyword = "keyword"
def keywordSearch(keyword, caseDescriptions):
    similarCases = []
    # Iterate through each case description
    for caseDescription in caseDescriptions:
        # Convert both keyword and case description to lowercase cus keyword search is case sensitive :(
        if keyword.lower() in caseDescription.lower():
            similarCases.append(caseDescription)
    return similarCases

