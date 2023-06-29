import sys


def tqma(_, /):
    try:
        h = f"/{len(_)}"
    except TypeError:
        h = ""
    for i, __ in enumerate(_):
        sys.stderr.write(f"\r{i+1}{h}")
        yield __
    print("\n")
