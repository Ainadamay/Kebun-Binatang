import importlib
import pkgutil
import koleksi
from hewan import Hewan

for modul in pkgutil.iter_modules(koleksi.__path__):
    try:
        importlib.import_module(f"koleksi.{modul.name}")
    except Exception as e:
        print(f"[GAGAL MEMUAT] {modul.name}: {e}")

for kelas in Hewan.__subclasses__():
    try:
        kelas(kelas.__name__).bersuara()
    except Exception as e:
        print(f"[ERROR] {kelas.__name__}: {e}")
