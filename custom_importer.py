import sys
import os
import importlib.util

def import_local_ifcopenshell():
    local_ifcopenshell_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'local_ifcopenshell'))
    ifcopenshell_spec = importlib.util.spec_from_file_location("ifcopenshell", os.path.join(local_ifcopenshell_path, "__init__.py"))
    ifcopenshell = importlib.util.module_from_spec(ifcopenshell_spec)
    sys.modules["ifcopenshell"] = ifcopenshell
    ifcopenshell_spec.loader.exec_module(ifcopenshell)
    return ifcopenshell

ifcopenshell = import_local_ifcopenshell()