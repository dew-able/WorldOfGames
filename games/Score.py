def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    try:
        with open('Scores.txt', 'r') as readfile:
            currentscore = readfile.read().strip()
            intcurrentscore = int(currentscore)
        with open('Scores.txt', 'w') as scorefile:
                    newscore = intcurrentscore + POINTS_OF_WINNING
                    scorefile.write(str(newscore))
    except:
        with open('Scores.txt', 'w') as newfile:
            newfile.write(str(POINTS_OF_WINNING))

