def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            total = 0
            employees_count = 0
            
            for line in file:
                try:
                    _, salary = line.strip().split(',', 1)
                    total += int(salary)
                    employees_count += 1
                except ValueError:
                    print(f"Skipping line due to ValueError: {line.strip()}")
                    continue
            
            if employees_count == 0:
                return (0, 0)  
            
            average = total / employees_count
            return (total, average)
    
    except FileNotFoundError:
        print(f"File {path} not found.")
        return (0, 0)
    except Exception as e:
        print(f"Get error: {e}")
        return (0, 0)
    
# total, average = total_salary("data/salary.txt")
# print(f"Total salary: {total}, Average salary: {average}")