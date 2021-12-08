from home.models import Students, Teachers


def isReacted(isStudent, userID, isQuestion, contentID):
    if isStudent:
        user = Students.objects.filter(sID=userID).first()
    else:
        user = Teachers.objects.filter(tID=userID).first()

    if isQuestion:
        records = user.questionRecord
    else:
        records = user.answerRecord
    if contentID in records.keys():
        return True
    return False
