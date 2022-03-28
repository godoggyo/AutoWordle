import _gamefunc as gf


if __name__ == "__main__":
    gf.establishWordPool()
    word = gf.selectWord()
    gf.gameStart()
    guess = gf.userInput()
    gf.letterCheck(word, guess)