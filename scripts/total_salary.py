import sys

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

if __name__ == "__main__":    
    default_path = "data/salary.txt"

    path = sys.argv[1] if len(sys.argv) > 1 else default_path

    total, average = total_salary(path)
    print(f"Total salary: {total}, Average salary: {average}")