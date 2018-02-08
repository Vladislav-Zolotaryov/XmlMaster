import sys
import os
from typing import List
from xml.dom import minidom

from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker
from XqlLang import XqlLexer, XqlParser, XqlListener


class KeyPrinter(XqlListener.XqlListener):
    def enterR(self, ctx):
        print("Oh, a key!", ctx.ID().getText())

    def exitR(self, ctx):
        print("Oh, a key exit!", ctx)


def main(argv):
    input = FileStream(argv[1])
    lexer = XqlLexer.XqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = XqlParser.XqlParser(stream)
    printer = KeyPrinter()
    tree = parser.r()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main(sys.argv)


script_name, workdir, file_extension, recursive = sys.argv


class QueryScript:

    def __init__(self, script_content: str):
        self.parse(script_content)

    def parse(self, script_content: str):
        pass


def list_folder(workdir: str) -> List[str]:
    return [os.path.join(workdir, dir_item)
            for dir_item in os.listdir(workdir)]


def recursive_list_folder(workdir: str) -> List[str]:
    folder_items = list_folder(workdir)
    files = []
    for item in folder_items:
        if os.path.isdir(item):
            files.extend(recursive_list_folder(item))
        elif os.path.isfile(item):
            files.append(item)
    return files
