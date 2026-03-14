import pytest
from src.Sources import GeneratorSource
from src.Task import Task

def test_generator_default():
    source = GeneratorSource()
    tasks = source.get_tasks()
    
    assert len(tasks) == 5
    assert all(isinstance(t, Task) for t in tasks)
    assert tasks[0].id == 0
    assert tasks[4].id == 4

def test_generator_with_custom_count():
    source = GeneratorSource(count=10)
    tasks = source.get_tasks()
    
    assert len(tasks) == 10
    assert tasks[0].id == 0
    assert tasks[9].id == 9

def test_generator_with_id_start():
    source = GeneratorSource(count=3, id_start=100)
    tasks = source.get_tasks()
    
    assert len(tasks) == 3
    assert tasks[0].id == 100
    assert tasks[1].id == 101
    assert tasks[2].id == 102

def test_generator_payload_content():
    source = GeneratorSource(count=2)
    tasks = source.get_tasks()
    
    assert tasks[0].payload == "Сгенерированная задача #0"
    assert tasks[1].payload == "Сгенерированная задача #1"

def test_generator_zero_count():
    source = GeneratorSource(count=0)
    tasks = source.get_tasks()
    
    assert len(tasks) == 0
    assert tasks == []

def test_generator_negative_count():
    source = GeneratorSource(count=-5)
    tasks = source.get_tasks()
    
    assert len(tasks) == 0

def test_generator_consistency():
    source1 = GeneratorSource(count=3, id_start=10)
    source2 = GeneratorSource(count=3, id_start=10)
    
    tasks1 = source1.get_tasks()
    tasks2 = source2.get_tasks()
    
    for t1, t2 in zip(tasks1, tasks2):
        assert t1.id == t2.id
        assert t1.payload == t2.payload