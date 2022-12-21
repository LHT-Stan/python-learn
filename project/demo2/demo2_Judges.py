

def outPut(teachers=0, scores=None, students=0, s_list=None):
    # 第二个参数给了默认值，当第一次打印信息时，未录入成绩所以不显示
    if teachers != 0:
        print(f"信息：本次比赛的评委人数为：{teachers}")
    if scores is not None:
        print(f"共{teachers}位评委，评分依次为：{scores}")
    if students != 0:
        print(f"学生人数为：{students}")
    if s_list is not None:
        print("成绩录入结束")
        print(s_list)


# 循环录入评委的打分，并排序,或者学生的成绩
def inputScores(teachers=0, students=0):
    t_list = []
    s_list = dict()
    if teachers != 0:
        for i in range(teachers):
            t_list.append(int(input(f"请输入第{i + 1}位评委的评分：")))
        t_list.sort(reverse=True)
        return t_list
    if students != 0:
        for i in range(students):
            s_name = input("请输入学生姓名：")
            s_score = int(input("请输入学生成绩："))
            s_dict = {s_name: s_score}
            # 判断字典中是否已有此学生
            if inSList(s_name, s_list):
                s_list.update(s_dict)
            else:
                print("错误....已输入该学生的成绩，请重试....")
                students += 1
                continue
        return s_list


# 判断学生字典中的键是否重复
def inSList(s_name, s_list):
    if s_list.get(s_name, -1) == -1:
        return True
    else:
        return False


# 查找学生成绩并排序
def selectSList(s_list):
    y_n = input("是否要查找某位同学的统计(yes或no)？")
    if y_n.upper() == 'YES':
        name = input("请输入你要查找的学生姓名：")
        if not inSList(name, s_list):
            print(f"{name}的成绩为：{s_list.get(name)}")
        else:
            print("无该学生")
        new_dict = sorted(s_list.items(), key=lambda x: x[1], reverse=True)
        max_name = new_dict[0][0]
        print(f"{max_name}同学成绩最高,分数为{s_list[max_name]}")
        s_list = new_dict
        print(f"排序后的学生名单及成绩为：{s_list}")
    elif y_n.upper() == 'NO':
        new_dict = sorted(s_list, key=lambda x: x[1], reverse=False)
        max_name = new_dict[0]
        print(f"{max_name}同学成绩最高,分数为{s_list[max_name]}")
        print(f"排序后的学生名单及成绩为：{new_dict}")


# 计算选手最终得分
def scoreAvg(score_lists):
    sum_s = 0
    score_lists.sort(reverse=True)
    print(f"去掉最高分{score_lists.pop(0)}，去掉最低分{score_lists.pop()}", end=", ")
    for i in range(len(score_lists)):
        sum_s += score_lists[i]
    print(f"本场比赛该选手最终得分为：{sum_s/len(score_lists)}")
    return sum_s/len(score_lists)


if __name__ == "__main__":
    TorS = input("请输入T或者S选择需要进入的系统：")
    if TorS.upper() == 'T':
        # 录入评委人数
        people = int(input("请输入评委人数:"))
        # 输出打印信息
        outPut(people)
        # 循环输入分数并排序
        score_list = inputScores(people)
        # 再次输出
        outPut(people, score_list)
        # 计算平均分
        scoreAvg(score_list)
    elif TorS.upper() == 'S':
        # 录入学生人数
        student = int(input("请输入学生人数:"))
        # 输出打印信息
        outPut(students=student)
        # 循环输入学生及成绩
        s_lists = inputScores(students=student)
        # 输出所有成绩
        outPut(s_list=s_lists)
        # 排序并输出最高
        selectSList(s_lists)
    else:
        print("输入错误，请稍后重试")

