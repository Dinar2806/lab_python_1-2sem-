import pytest
import json
import tempfile
import os
from src.Sources import FileSource
from src.Task import Task

@pytest.fixture
def valid_json_file():
    data = [
        {"id": 1, "payload": "задача 1"},
        {"id": 2, "payload": "задача 2"},
        {"id": 3, "payload": "задача 3"}
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(data, f)
        temp_path = f.name
    
    yield temp_path
    
    os.unlink(temp_path)

@pytest.fixture
def empty_json_file():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump([], f)
        temp_path = f.name
    
    yield temp_path
    
    os.unlink(temp_path)

@pytest.fixture
def invalid_json_file():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        f.write('{это не json')
        temp_path = f.name
    
    yield temp_path
    
    os.unlink(temp_path)

def test_file_source_reads_valid_json(valid_json_file):
    source = FileSource(valid_json_file)
    tasks = source.get_tasks()
    
    assert len(tasks) == 3
    assert all(isinstance(t, Task) for t in tasks)
    assert tasks[0].id == 1
    assert tasks[0].payload == "задача 1"
    assert tasks[1].id == 2
    assert tasks[2].id == 3

def test_file_source_empty_json(empty_json_file):
    source = FileSource(empty_json_file)
    tasks = source.get_tasks()
    
    assert len(tasks) == 0
    assert tasks == []

def test_file_source_file_not_found():
    source = FileSource("несуществующий_файл.json")
    
    with pytest.raises(Exception) as excinfo:
        source.get_tasks()
    assert "не найден" in str(excinfo.value)

def test_file_source_invalid_json(invalid_json_file):
    source = FileSource(invalid_json_file)
    
    with pytest.raises(Exception) as excinfo:
        source.get_tasks()
    assert "Ошибка формата JSON" in str(excinfo.value)

def test_file_source_with_custom_data():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump([
            {"id": "a1", "payload": {"name": "тест", "value": 123}},
            {"id": 999, "payload": [1, 2, 3]}
        ], f)
        temp_path = f.name
    
    try:
        source = FileSource(temp_path)
        tasks = source.get_tasks()
        
        assert len(tasks) == 2
        assert tasks[0].id == "a1"
        assert tasks[0].payload["name"] == "тест"
        assert tasks[1].id == 999
        assert tasks[1].payload == [1, 2, 3]
    finally:
        os.unlink(temp_path)