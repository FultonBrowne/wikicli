#!/usr/bin/python3

import wikipediaapi, sys
class WikiBrain:
    def __init__(self, lang):
        self.wiki = wikipediaapi.Wikipedia(lang)

    def pageexist(self, term):
        return self.wiki.page(term)
    
    def summary(self, page):
        return self.wiki.page(page).summary
    def full_page(self, page):
        return self.wiki.page(page).text

def main():
    if __name__ != "__main__":
        print("no")
        return
    if len(sys.argv) != 3:
        print("no")
        return
    print(sys.argv)
    arg = sys.argv[1]
    name = sys.argv[2]
    wikibrain = WikiBrain("en")
    if arg == "sources":
        return wikibrain.summary(name)
    elif arg == "page":
        return wikibrain.full_page(name)
    elif arg == "desc":
        return wikibrain.summary(name)

print(main())