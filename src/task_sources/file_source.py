import json
from typing import Protocol, Any, List, Union
from src.task.task import Task

class Reader(Protocol):
    def read(self, file_path: str) -> Any:
        ...
        
class JsonReader:
    
    def get_tasks(self, file_path: str) -> List[Task]:
        tasks: List[Task] = []
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                tasks.append(Task(item["id"], item["payload"]))
                
                    
        
        return tasks
            

class TxtReader:
    def get_tasks(self, file_path: str) -> List[Task]:
        tasks: List[Task] = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    
                    # Пропускаем пустые строки
                    if not line:
                        continue
                    
                    # 1. Валидация наличия разделителя
                    if ':' not in line:
                        print(f"Ошибка в строке {line_num}: отсутствует разделитель ':'")
                        continue
                    task_id, payload = line.split(':', 1)
                    if not task_id.strip():
                        print(f"Ошибка в строке {line_num}: id не может быть пустым")
                        continue
                        
                    tasks.append(Task(task_id.strip(), payload.strip()))
        except FileNotFoundError:
            print("Ошибка. Файл не найден")
        
        return tasks
            
        
                
        
        

if __name__ == "__main__":
    obj = TxtReader()
    data = obj.read("example.txt")        
    print(data)