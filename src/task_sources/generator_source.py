import random
from typing import Any, Union, List
from src.task.task import Task


class GeneratorSource():
    
    def __init__(self, count: int = 5, id_start: int = 0, payload_type: str = "text"):
        """
            Инициализация генератора
        Args:
            count (int, optional): _description_. Defaults to 5.
            id_start (int, optional): _description_. Defaults to 0.
            payload_type (str, optional): _description_. Defaults to "text".
        """
        
        if count <= 0:
            raise ValueError("Количество задач должно быть положительным числом")
        
        if payload_type not in ["text", "number", "mixed"]:
            raise ValueError("payload_type должен быть 'text', 'number' или 'mixed'")
        
        self.count = count
        self.id_start = id_start
        self.payload_type = payload_type
        
    def get_tasks(self) -> List[Task]:
        """
        Генерация списка задач

        Returns:
            List[Task]: _description_
        """
        
        tasks = []
        
        for i in range(self.count):
            task_id = self.id_start + i
            
            if self.payload_type == "text":
                payload = self._generate_text_payload(i)
            elif self.payload_type == "number":
                payload = self._generate_number_payload(i)
            else:
                payload = self._combinate_payload(i)
                
            task = Task(id=task_id, payload=payload)
            tasks.append(task)
        
        return tasks
                
        
    
    def _generate_text_payload(self, index: int) -> str:
        """Генерация полезного содержания payload для Task

        Args:
            index (int): _description_

        Returns:
            str: _description_
        """
        
        texts = [
            f"Убрать мусор в комнате {random.randint(1,500)}",
            f"Вымыть полы в комнате {random.randint(1,500)}",
            f"Отправить отчет №{index}",
            f"Позвонить клиенту {index}",
            f"Написать письмо {index}",
            f"Проверить документы {index}",
            f"Сделать резервную копию {index}"
        ]
        
        return random.choice(texts)
    
    def _generate_number_payload(self) -> int:
        """Случайное чиисло в качестве payload

        Returns:
            int: _description_
        """
        
        return random.randint(1, 10000)
    
    def _combinate_payload(self, index: int) -> str:
        """Генерация комбинированных данных в качестве payload для Task

        Args:
            index (int): _description_

        Returns:
            str: _description_
        """
        
        result = ""
        for i in range(random.randint(1,10)):
            choice = random.randint(1, 2)
            if choice == 1:
                result += self._generate_text_payload(index=index)
            else:
                result += str(self._generate_number_payload())
            result += ", "
        return result
                
                

                
        