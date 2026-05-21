# GnuChanGUI - Work TODO

Status as of 2026-05-21

- [x] Run module import smoke test (completed, import succeeded)
- [x] Lazy-load `urllib.request` in `_copy_files_from_github` (completed)
- [x] Search for remaining heavy top-level imports and lazy-load (completed; no remaining direct heavy imports found)
- [x] Remove leftover Python 2 compatibility code (completed)
- [x] Re-run import test and verify no NameError (completed)
- [x] Fix Pylance syntax errors in `GnuChanGUI/gcLibrary.py` (completed)
- [x] Fix typing/type-check Pylance diagnostics (`Any`, `List`, `Dict`, `configparser`) (completed)

Recent changes made
- Consolidated duplicate `TKINTER_CURSORS` and fixed ttk-scrollbar docstring.
- Added `_lazy_import` wrappers for `urllib.request` and used it in `_copy_files_from_github`.
- Added `from typing import Any, List, Dict, Optional, TYPE_CHECKING` and `if TYPE_CHECKING: import configparser` to satisfy static type checker.
- Removed Python 2 compatibility fallback in REPL/watch evaluation code.
- Verified no remaining top-level heavy imports for `json`, `pickle`, `subprocess`, `configparser`, `pydoc`, `ctypes`, or `urllib`.
- Added `Multiline` undo/redo keyboard shortcut support (Ctrl+Z / Ctrl+Y / Ctrl+Shift+Z) and exposed `EnableUndo` in `GMultiline`.

Next steps
1. Refresh editor/Pylance diagnostics locally to clear stale errors.
2. Optionally test a representative GUI or sample script from `Examples/` to validate runtime behavior.
3. Review `gcLibrary.py` for any remaining cleanup if new diagnostics appear.
4. Add transparent window support and improve `GOutput` read-only / crash-report behavior in `GnuChanGUI/__init__.py`.

Pending work
- [ ] Run an interactive smoke test with a selected example from `Examples/`.
- [ ] Implement missing `GnuChanGUI` window/window-state methods in `GnuChanGUI/__init__.py`.
- [ ] Add transparent window system support to `GnuChanGUI/__init__.py`.
- [ ] Improve `GOutput` to support read-only mode and print a pre-crash error report before use.

GC Library audit
- [x] Confirmed `gcLibrary.py` now includes lazy import wrappers for optional heavy modules (`pickle`, `subprocess`, `json`, `configparser`, `pydoc`, `ctypes`, `urllib.parse`, `urllib.request`).
- [x] Confirmed `typing` imports and `if TYPE_CHECKING: import configparser` stub are in place.
- [x] Confirmed PIL import is guarded and only attempted during screenshot/image-grab functionality.
- [x] Confirmed no remaining direct heavy imports beyond the expected Tkinter GUI core and standard library.
- [ ] Review whether top-level `tkinter` imports can be deferred or isolated further.
- [ ] Address explicit `XXX ToDo: cget and configure` comment found in `gcLibrary.py`.
- [ ] Run full `gcLibrary.py` static type / Pylance check to validate any remaining typing coverage issues.

How I can proceed
- I can run the import smoke test here; say "Run import test" and I'll execute it and report results.
- I can continue auditing imports automatically.

