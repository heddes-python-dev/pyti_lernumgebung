"""Register custom levels in the active UI catalog after persistent save."""

from .admin_store import AdminStore


def register_custom_level(levels, level_list, name, level, store):
    AdminStore.validate_level(level)
    key = store.speichern(name, level)
    if key not in levels:
        levels[key] = level
        level_list.addItem(key)
    else:
        levels[key] = level
        current = level_list.currentItem()
        if current is not None and current.text() == key:
            row = level_list.row(current)
            level_list.setCurrentRow(-1)
            level_list.setCurrentRow(row)
    return key


def delete_custom_level(levels, level_list, name, store):
    if not name.startswith(store.PREFIX):
        raise ValueError("Es können nur eigene Level gelöscht werden.")
    if name not in levels:
        raise ValueError(f"Eigenes Level nicht gefunden: {name}")
    store.loeschen(name)
    del levels[name]
    for row in range(level_list.count()):
        if level_list.item(row).text() == name:
            was_current = level_list.currentRow() == row
            level_list.takeItem(row)
            if was_current and level_list.count():
                level_list.setCurrentRow(min(row, level_list.count() - 1))
            break
