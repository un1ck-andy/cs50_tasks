from twttr import shorten

def main():
    test_1()

def test_vowels():
    assert shorten("hello") == "hll"
    assert shorten("GOODday") == "GDdy"
def test_punctuation():
    assert shorten("hello, world") == "hll, wrld"
def test_numbers():
    assert shorten("number testing 1") == "nmbr tstng 1"

if __name__ == "__main__":
    main()
