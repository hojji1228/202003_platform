

reg_num = input("주민등록번호:")
if reg_num[7] == "1" or reg_num[7] == "3":
    print ("남자")
elif reg_num[7] == "2" or reg_num[7] == "4":
    print ("여자")