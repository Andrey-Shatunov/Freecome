def entity_to_str(entity):
    str1=""
    for i,value in enumerate(entity,1):
        str1=str1+"\'"+str(i)+"\'"+''': '''+str(value)+''', '''

    str1=str1[0:(len(str1)-2)]
    str1='''{'''+str1+'''}'''
    return str1