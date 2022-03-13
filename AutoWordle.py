import _gamefunc as ws

class AutoWordle():

    word = None

    def __init__(self) -> None:
        ws.establishWordPool
        word = ws.selectWord()