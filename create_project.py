import os

def create_structure_from_file(file_path):
    with open(file_path, 'r') as file:
        base_dir = None
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith('/'):
                base_dir = line.strip('/')
                os.makedirs(base_dir, exist_ok=True)
            elif base_dir:
                path = os.path.join(base_dir, line)
                if line.endswith('/'):
                    os.makedirs(path, exist_ok=True)
                else:
                    open(path, 'w').close()

if __name__ == "__main__":
    create_structure_from_file('project_structure.txt')