import travelagencyDAO 

travelagency1 = {
    'ID': 12,
    'fullname': 'MartynasMakalis',
    'firmname': 'Vilnius-travelagency',
    'email': 'vilniusta@gmail.com'

}
travelagency2 = {
    'ID': 1,
    'fullname': 'kalis',
    'firmname': 'travelagency',
    'email': 'iusta@gmail.com'

}

#returnvalue = travelagencyDAO.create(travelagency)
returnValue =  travelagencyDAO.getAll()
print(returnValue)
returnValue =  travelagencyDAO.findById(travelagency2['ID'])
print("find By Id")
print(returnValue)
returnValue =  travelagencyDAO.update(travelagency2)
print(returnValue)
returnValue =  travelagencyDAO.findById(travelagency2['ID'])
print(returnValue)
returnValue =  travelagencyDAO.delete(travelagency2['ID'])
print(returnValue)
returnValue travelagencyDAO.getAll()
print(returnValue)
