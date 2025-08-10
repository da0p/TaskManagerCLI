import task_manager

def test_add_task():
    manager = task_manager.TaskManager()
    id = manager.add_task("Dummy")
    tasks = manager.all_tasks()
    assert len(tasks) == 1
    assert tasks[id].get_status() == task_manager.TaskStatus.PENDING
    assert tasks[id].get_description() == "Dummy"

def test_delete_task():
    manager = task_manager.TaskManager()
    id = manager.add_task("Dummy")
    manager.delete_task(id)
    tasks = manager.all_tasks()
    assert len(tasks) == 0

def test_mark_task_in_progress():
    manager = task_manager.TaskManager()
    id = manager.add_task("Dummy")
    manager.mark_in_progress(id)
    tasks = manager.all_tasks()
    assert tasks[id].get_status() == task_manager.TaskStatus.IN_PROGRESS

def test_mark_task_completed():
    manager = task_manager.TaskManager()
    id = manager.add_task("Dummy")
    manager.mark_completed(id)
    tasks = manager.all_tasks()
    assert tasks[id].get_status() == task_manager.TaskStatus.COMPLETED

def test_add_multiple_tasks():
    manager = task_manager.TaskManager()
    ids = [manager.add_task(f"Task {i}") for i in range(5)]
    tasks = manager.all_tasks()
    assert len(tasks) == 5
    for i, id in enumerate(ids):
        assert tasks[id].get_description() == f"Task {i}"
        assert tasks[id].get_status() == task_manager.TaskStatus.PENDING

def test_existing_task():
    manager = task_manager.TaskManager()
    id = manager.add_task("Dummy")
    assert manager.is_existed(id) is True
    assert manager.is_existed(id + 1) is False

def test_update_task():
    manager = task_manager.TaskManager()
    id = manager.add_task("Dummy")
    manager.mark_in_progress(id)
    manager.update_task(id, "Updated Dummy")
    tasks = manager.all_tasks()
    assert tasks[id].get_description() == "Updated Dummy"
    assert tasks[id].get_status() == task_manager.TaskStatus.IN_PROGRESS