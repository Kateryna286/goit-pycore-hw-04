import sys

def get_cats_info(path):
    try:
        with open(path, encoding='utf-8') as file:

            cats_info = []

            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',', 2)
                    cats_info.append({
                        'id': cat_id,
                        'name': name,
                        'age': age
                    })
                
                except ValueError:
                    print(f"Skipping line due to ValueError: {line.strip()}")
                    continue
            
            if len(cats_info) == 0:
                print(f"File is empty or no valid data found.")   
                return []  
            
            return cats_info
        
    except FileNotFoundError:
        print(f"File {path} not found.")
        return []
    except Exception as e:
        print(f"Get error: {e}")
        return []
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python <path_to_script> <path_to_file>")
        sys.exit(1)

    path = sys.argv[1]
    cats_info = get_cats_info(path)
    print(cats_info)

