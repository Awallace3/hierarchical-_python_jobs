from dataclasses import dataclass
import numpy as np

"""
All dataclass_js should have id_label for ms_sl() usage to update sql db
correctly

if you are using a postgresql db, you need to include mem set to None to have compatability with sql
"""


@dataclass
class example_js:
    id_label: int
    val: float
    extra_info: {}
    mem: str = None


@dataclass
class vina_js:
    id_label: int
    PRO_PDB: str
    LIG_PDB: str
    WAT_PDB: str
    OTH_PDB: str
    extra_info: {}


def vina_js_headers():
    return [
        "id",
        "PRO_PDB",
        "LIG_PDB",
        "WAT_PDB",
        "OTH_PDB",
    ]


@dataclass
class apnet_disco_js:
    id_label: int
    PRO_PDB: str
    LIG_PDB: str
    WAT_PDB: str
    OTH_PDB: str
    PRO_CHARGE: int
    LIG_CHARGE: int
    extra_info: {}
    mem: str = None


def apnet_disco_js_headers():
    return [
        "id",
        "PRO_PDB_Hs",
        "LIG_PDB",
        "WAT_PDB",
        "OTH_PDB",
        "PRO_CHARGE",
        "LIG_CHARGE",
    ]

@dataclass
class autodock_vina_disco_js:
    id_label: int
    PRO_PDB: str
    LIG_PDB: str
    WAT_PDB: str
    OTH_PDB: str
    extra_info: {}
    mem: str = None


def autodock_vina_disco_js_headers():
    return [
        "id",
        "PRO_PDB",
        "LIG_PDB",
        "WAT_PDB",
        "OTH_PDB",
    ]

