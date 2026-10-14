def report_summary(data):
    res = {}
    for emp in data:
        dept = emp["department"]
        if dept not in res:
            res[dept] = {"total_salary": 0, "total_emp": 0, "average_salary":0}

        res[dept]["total_salary"] += emp["salary"]
        res[dept]["total_emp"] += 1
        res[dept]["average_salary"] = res[dept]["total_salary"]//res[dept]["total_emp"]
    return res