"""
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py

1)relative imports are based on the name of the current module.
     From the surround module for example:
     from . import echo
    from .. import formats
    from ..filters import equalizer
output_formatting_1)Since the name of the main module is always "__main__",
3)modules intended for use as the main module of a Python application must always use absolute imports.

"""