# 计算Python开发工程师平均薪资 
sum_salary=0
count_num=0
avg_salary=0
def calculate_salary(salary):
    global sum_salary,count_num,avg_salary
    # 筛选出存在薪资的Python开发工程师并计算平均薪资
    if salary != "":
        count_num = count_num+1
        sum_salary = float(salary) +sum_salary
        avg_salary = round(sum_salary/count_num,2)
        return avg_salary
        
    
         
    

        

        

    
