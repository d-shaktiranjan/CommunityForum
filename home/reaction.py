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
    records = getRecord(isStudent, userID, isQuestion)
    if records is None:
        return False
    if contentID in records.keys():
        return True
    return False


def giveReaction(isStudent, userID, isQuestion, contentID, isLiked):
    if isReacted(isStudent, userID, isQuestion, contentID):
        return False

    if isStudent:
        user = Students.objects.filter(sID=userID).first()
    else:
        user = Teachers.objects.filter(tID=userID).first()

    if isQuestion:
        about = Quentions.objects.filter(qID=contentID).first()
        if isLiked:
            about.likeCount += 1
            oldData = user.questionRecord
            if oldData is None:
                user.questionRecord = {
                    contentID: True
                }
            user.questionRecord[contentID] = True
        else:
            about.disLikeCount += 1
            oldData = user.questionRecord
            if oldData is None:
                user.questionRecord = {
                    contentID: False
                }
            user.questionRecord[contentID] = False
        user.save()
        about.save()
    else:
        about = Answers.objects.filter(aID=contentID).first()
    return True
