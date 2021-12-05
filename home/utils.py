def generateSalt(mail):
    mailList = mail.split("@")
    uIdList = list(mailList[0])
    finalList = []
    for index, item in enumerate(uIdList):
        if index % 2 == 0:
            finalList.append(item)
    salt = "".join(map(str, finalList))+mailList[0][::-1]+mailList[1]
    return salt
