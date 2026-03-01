from dataclasses import dataclass
from typing import Any, Union



@dataclass
class Task:
    
    
    id: Union[int, str]
    payload: Any

    def __post_init__(self):
        """
        Валидация данных после инициализации
        """
        if self.id is None:
            raise ValueError("ID задачи не может быть None")
        
    def to_dict(self) -> dict:
        dict = {
            "id": self.id,
            "payload":  self.payload
        }
        return dict
    

