import atheris

# Import target function
with atheris.instrument_imports():
    from date import validate_datestring,print_date


def get_input(data: bytes) -> str:
    """Erzeuge einen String mit Länge 8..10 aus den Zeichen 0-9 und '-'."""
    fdp = atheris.FuzzedDataProvider(data)
    max_len = 10
    
    """
    min_len = 7
    max_len = 10

    # Länge sicher erzeugen (falls etwas schiefgeht, fallback auf min_len)
    try:
        length = fdp.ConsumeIntInRange(min_len, max_len)
    except Exception:
        length = min_len

    allowed = "0123456789-"
    out_chars = []

    for _ in range(length):
        try:
            # Index für erlaubtes Zeichen wählen
            idx = fdp.ConsumeIntInRange(0, len(allowed) - 1)
            out_chars.append(allowed[idx])
        except Exception:
            # Falls Provider leer wird, fülle mit '0'
            out_chars.append("0")

    return "".join(out_chars)
    """
    

    return fdp.ConsumeUnicodeNoSurrogates(max_len)




def TestOneInput(data: bytes) -> None:
    """Run an input through the target function"""
    expr = get_input(data)
    print_date(expr)
    
      

if __name__ == "__main__":
    import sys
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()
