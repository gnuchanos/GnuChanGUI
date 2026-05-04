"""xStretch_weight / yStretch_weight — part09 tam demosu.

Genisleme odakli kisa ornek (once bunu dene):
  python Examples/genisleme_stretch_ornek.py

Bu dosya (part09):
  python Examples/expand_weights_demo.py
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve()
    repo_root = here.parents[1]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))
    target = repo_root / "Examples" / "Tutorials" / "part09_layout_expand_weights.py"
    spec = importlib.util.spec_from_file_location("part09_layout_expand_weights", target)
    if spec is None or spec.loader is None:
        raise RuntimeError("Ornek dosyasi bulunamadi: {}".format(target))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.Part09()


if __name__ == "__main__":
    main()
