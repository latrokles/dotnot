from dataclasses import dataclass, field
from typing import ClassVar


def is_blank(s):
    return s == '' or s.isspace()


def is_not_blank(s):
    return not is_blank(s)


def is_int(token):
    try:
        int(token)
        return True
    except ValueError:
        return False


def is_float(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


class ScanError(Exception):
    """Raised if an error is encountered during scanning."""


class ParseError(Exception):
    """Raised if an error is encountered during parsing."""


@dataclass
class Scanner:
    src: str
    pos: int = 0
    row: int = 1
    col: int = 1

    EOF: ClassVar[str] = '#EOF#'

    def next_token(self):
        char = self.peek()
        if is_blank(char):
            self.consume_blank_space()

        char = self.peek()
        match char:
            case '\'':
                return self.consume_string()

            case _:
                return self.consume_value()

        return Scanner.EOF

    def consume(self):
        char = self.src[self.pos]
        self.pos += 1
        self.col += 1
        return char

    def consume_blank_space(self):
        while is_blank(self.peek()) and self.is_not_finished():
            char = self.consume()

            if char == '\n':
                self.col = 1
                self.row += 1

    def consume_string(self):
        chars = []
        self.consume()
        while (self.peek() != '\'') and (self.is_not_finished()):
            if self.peek() == '\n':
                self.col = 1
                self.row += 1

            chars.append(self.consume())

        if self.is_finished():
            self.emit_error('unterminated string')

        self.consume()
        return ''.join(chars)

    def consume_value(self):
        chars = []
        while is_not_blank(self.peek()) and self.is_not_finished():
            chars.append(self.consume())

        text = ''.join(chars)
        if is_int(text):
            return int(text)

        if is_float(text):
            return float(text)

        return text

    def peek(self):
        if self.is_finished():
            return '\0'
        return self.src[self.pos]

    def is_not_finished(self):
        return self.pos < len(self.src)

    def is_finished(self):
        return self.pos >= len(self.src)

    def emit_error(self, message):
        raise ScanError(f'error={message}, row={self.row}, col={self.col}')

@dataclass
class Parser:
    scanner: Scanner|None = None

    def parse_source(self, source):
        self.scanner = Scanner(source)
        return self.parse()

    def parse(self):
        values = []
        while self.scanner.is_not_finished():
            token = self.scanner.next_token()
            print(f'token={token}')
            values.append(token)

        return values
