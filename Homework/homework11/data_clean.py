def data_clean(salary):
    peace = str(salary).split('-')
    # print(peace)
    # 将数值与单位分离
    m = ''
    if (len(peace) > 1):
        peace[0] = float(peace[0])
        # unit 是薪资的单位
        unit = peace[1].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace(
            "5", "").replace("6", "").replace("7", "").replace("8", "").replace("8", "").replace("9", "").replace(".",
                                                                                                                  "")
        data1 = peace[1].replace("元", "").replace("千", "").replace("万", "").replace("/", "").replace("小时", "").replace(
            "天", "").replace("月", "").replace("年", "").replace("以上", "")
        num = float(data1)
        # 这里是将薪资的单位统一为 万/月
        if (unit == "元/小时"):
            salary_1 = str(round((data1 * 24 * 30 / 10000), 2))
            salary_2 = str(round((num * 24 * 30 / 10000), 2))
        elif (unit == "元/天"):
            salary_1 = str(round((peace[0] * 30 / 10000), 2))
            salary_2 = str(round((num * 30 / 10000), 2))
        elif (unit == "千/月"):
            salary_1 = str(round((peace[0] / 10), 2))
            salary_2 = str(round((num / 10), 2))
        elif (unit == "万/年"):
            salary_1 = str(round((peace[0] / 12), 2))
            salary_2 = str(round((num / 12), 2))
        else:
            salary_1 = str(peace[0])
            salary_2 = str(num)
        m = str(round((float(salary_1) + float(salary_2)) / 2, 2))

    elif (peace[0] == ""):
        m = ""
        # print(peace)
    else:
        # unit 是薪资的单位
        unit = peace[0].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace(
            "5", "").replace("6", "").replace("7", "").replace("8", "").replace("8", "").replace("9", "").replace(".",
                                                                                                                  "")
        data2 = peace[0].replace("元", "").replace("千", "").replace("万", "").replace("/", "").replace("小时", "").replace(
            "天", "").replace("月", "").replace("年", "").replace("以上", "").replace("以下", "")
        # print(data2)
        num = float(data2)
        if (unit == "元/小时"):
            salary_3 = str(round((num * 24 * 30 / 10000), 2))

        elif (unit == "元/天"):
            salary_3 = str(round(num * 30 / 10000))
            # print(salary_3)

        elif (unit == "千/月" or unit == "千以下/月"):
            salary_3 = str(round(num / 10))

        elif (unit == "万/年" or unit == "万以上/年" or unit == "万以下/年"):
            salary_3 = str(round(num / 12))

        elif (unit == "万/月" or unit == "万以上/月" or unit == "万以下/月"):
            salary_3 = str(num)
        # 如果提供的单位不是这几个中的一个，输出标记可自行查看！哈哈哈哈
        else:
            salary_3 = str(num)
            # print(peace[0])
        m = salary_3
        # print(peace)
    return m