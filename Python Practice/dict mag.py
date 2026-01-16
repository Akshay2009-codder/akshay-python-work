def matching (sentance1,sentance2):
    words1 = sentance1.split(" ")
    words2 = sentance2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
             if word1.lower() == word2.lower():
               score = score + 1
    return score

if __name__ == "__main__":
    sentance = ["i am a student", "i am studying in collage","my collage location is palanpur"]
    qury = input("please enter the qury string : \n")
    scores =( matching(sentance,qury) for sentance in sentance)
    sortedScore = (sentance for sentance in sorted(zip(scores,sentance), reverse=True))
    for score, item  in sortedScore:
        print(f" \"{score}\":with a score of score {item}")



