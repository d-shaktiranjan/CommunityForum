from turtle import home


from home.models import Students, Teachers


def generateSalt(mail):
    salt = "@"
    salt += mail[::2]+"#"
    salt += mail[-3:]+"&"
    return salt


def isNewUser(id, isStudent):
    if isStudent:
        user = Students.objects.filter(regNumber=id).first()
    else:
        user = Teachers.objects.filter(mailId=id).first()
    return user == None
