class STUDENT:


    def __init__(self):
        self.info = {}
        self.info["department"] = input("학과: ")
        self.info["hakbeon"] = input("학번: ")
        self.info["name"] = input("이름: ")
        self.info["gukeo"] = int(input("국어점수: "))
        self.info["english"] = int(input("영어점수: "))
        self.info["math"] = int(input("수학점수: "))
        self.info["sum"] = self.info["gukeo"] + self.info["english"] + self.info["math"]
        self.info["average"] = self.info["sum"] / 3
        if self.info["average"] >= 95:
            self.info["hakjeom"] = "A+"
        elif self.info["average"] >= 90:
            self.info["hakjeom"] = "A0"
        elif self.info["average"] >= 85:
            self.info["hakjeom"] = "B+"
        elif self.info["average"] >= 80:
            self.info["hakjeom"] = "B0"
        elif self.info["average"] >= 75:
            self.info["hakjeom"] = "C+"
        elif self.info["average"] >= 70:
            self.info["hakjeom"] = "C0"
        elif self.info["average"] >= 65:
            self.info["hakjeom"] = "D+"
        else:
            self.info["hakjeom"] = "F"

    def issame(self,search):
        if self.info["hakbeon"] == search or self.info["name"] == search:
            return 1
        else:
            return 0

    def printinfo(self):
        for j, k in self.info.items():
            print("{}: {}".format(j, k))

    def return_info(self,s):
        return self.info[s]






def print_menu():
    print("1.데이터 추가")
    print("2.데이터 검색")
    print("3.데이터 삭제")
    print("4.데이터 정렬")
    print("0.종료")

def add_data(std_list):
    std_list.append(STUDENT())

def search_data(std_list):
    search = input("찾을 이름 또는 학번 입력: ")
    for i in std_list:
        if i.issame(search):
            i.printinfo()

def del_data(std_list):
    search = input("지울 이름 또는 학번 입력: ")
    for i in student_list:
        if i.issame(search):
            std_list.remove(i)


def sort_data(std_list):
    num = input("정렬기준을 입력(1.학과,2.이름): ")
    temp = []

    if num == '1':
        sort_temp = [i.return_info("department") for i in student_list]
        sort_temp.sort()
        for i in sort_temp:
            for j in std_list:
                if j.return_info("department") == i:
                    temp.append(j)
                    std_list.remove(j)
                    break
        std_list = temp

    elif num == '2':
        sort_temp = [i.return_info("name") for i in std_list]
        sort_temp.sort()
        for i in sort_temp:
            for j in std_list:
                if j.return_info("name") == i:
                    temp.append(j)
                    std_list.remove(j)
                    break
        std_list = temp

    for i in std_list:
        print("=" * 20)
        i.printinfo()

    return std_list


#main

student_list=[]


while 1:
    print_menu()
    menu=input("입력: ")

    if menu == '1':
        add_data(student_list)

    elif menu == '2':
        search_data(student_list)

    elif menu == '3':
        del_data(student_list)

    elif menu =="4":
        student_list = sort_data(student_list)

    elif menu == '0':
        break