memory_store = {}

def get_memory(session_id: str):
    return memory_store.get(session_id, [])

def update_memory(session_id: str, new_entry: str):
    memory_store.setdefault(session_id, []).append(new_entry)
