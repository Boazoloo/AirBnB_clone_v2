

def clear_stream(stream):
    """Clears the contents of a given stream (e.g. a StringIO)."""
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)
