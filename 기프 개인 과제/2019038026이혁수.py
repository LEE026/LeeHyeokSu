student_list=[]

while 1:
    print("1.데이터 추가")
    print("2.데이터 검색")
    print("3.데이터 삭제")
    print("4.데이터 정렬")
    print("0.종료")
    menu=input("입력: ")

    if menu == '1':
        temp={}
        temp["department"]=input("학과: ")
        temp["hakbeon"] = input("학번: ")
        temp["name"] = input("이름: ")
        temp["gukeo"] = int(input("국어점수: "))
        temp["english"] = int(input("영어점수: "))
        temp["math"] = int(input("수학점수: "))
        temp["sum"] =  temp["gukeo"]+temp["english"]+temp["math"]
        temp["average"]= temp["sum"]/3
        if temp["average"]>=95:
            temp["hakjeom"] ="A+"
        elif temp["average"]>=90:
            temp["hakjeom"] ="A0"
        elif temp["average"]>=85:
            temp["hakjeom"] ="B+"
        elif temp["average"]>=80:
            temp["hakjeom"] ="B0"
        elif temp["average"]>=75:
            temp["hakjeom"] ="C+"
        elif temp["average"]>=70:
            temp["hakjeom"] ="C0"
        elif temp["average"]>=65:
            temp["hakjeom"] ="D+"
        else:
            temp["hakjeom"]="F"

        student_list.append(temp)

    elif menu == '2':
        search=input("찾을 이름 또는 학번 입력: ")
        for i in student_list:
            if i["hakbeon"] == search or i["name"] ==search:
                for j,k in i.items():
                    print("{}: {}".format(j,k))

    elif menu == '3':
        search = input("지울 이름 또는 학번 입력: ")
        for i in student_list:
            if i["hakbeon"] == search or i["name"] == search:
                student_list.remove(i)

    elif menu =="4":
        num=input("정렬기준을 입력(1.학과,2.이름): ")
        temp=[]

        if num =='1':
            sort_temp=[i["department"] for i in student_list]
            sort_temp.sort()
            for i in sort_temp:
                for j in student_list:
                    if j["department"] == i:
                        temp.append(j)
                        student_list.remove(j)
                        break
            student_list=temp

        elif num =='2':
            sort_temp = [i["name"] for i in student_list]
            sort_temp.sort()
            for i in sort_temp:
                for j in student_list:
                    if j["name"] == i:
                        temp.append(j)
                        student_list.remove(j)
                        break
            student_list=temp

        for i in student_list:
            print("="*20)
            for j,k in i.items():
                print("{}: {}".format(j,k))
    elif menu == '0':
        break