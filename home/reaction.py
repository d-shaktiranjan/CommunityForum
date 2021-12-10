from home.models import *


def getRecord(isStudent, userID, isQuestion):
    if isStudent:
        user = Students.objects.filter(sID=userID).first()
    else:
        user = Teachers.objects.filter(tID=userID).first()

    if isQuestion:
        records = user.questionRecord
    else:
        records = user.answerRecord
    return records


def isReacted(isStudent, userID, isQuestion, contentID):
    records = getRecord(isStudent, userID, isQuestion, contentID)
    if contentID in records.keys():
        return True
    return False


def giveReaction(isStudent, userID, isQuestion, contentID, isLiked):
    if isReacted(isStudent, userID, isQuestion, contentID):
        return False
    try:
        records = getRecord(isStudent, userID, isQuestion, contentID)
        if isQuestion:
            about = Quentions.objects.filter(qID=contentID).first()
        else:
            about = Answers.objects.filter(aID=contentID).first()
        if isLiked:
            records[contentID] = True
            about.likeCount += 1
        else:
            records[contentID] = False
            about.disLikeCount += 1
        return True
    except:
        return False
