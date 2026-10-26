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
