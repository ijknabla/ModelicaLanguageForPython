from arpeggio import EndOfFile, Not, OneOrMore, RegExMatch

from ._types import ParsingExpressionLike, returns_parsing_expression


class PEGSyntax:
    # ## PEG comment rule
    @staticmethod
    @returns_parsing_expression
    def COMMENT() -> ParsingExpressionLike:
        return [
            RegExMatch(r"//.*"),
            RegExMatch(r"/\*([^*]|\*[^/])*\*/"),
        ]

    # ## PEG lexical rules
    @staticmethod
    @returns_parsing_expression
    def KEYWORD() -> RegExMatch:
        return RegExMatch("`[a-z]+`")

    @classmethod
    @returns_parsing_expression
    def LEXICAL_REFERENCE(cls) -> ParsingExpressionLike:
        return cls.LEXICAL_RULE, Not("=")

    @staticmethod
    @returns_parsing_expression
    def LEXICAL_RULE() -> RegExMatch:
        return RegExMatch(r"[A-Z](([0-9A-Z]*-)*[0-9A-Z]+)?")

    @staticmethod
    @returns_parsing_expression
    def REGEX() -> ParsingExpressionLike:
        return [
            RegExMatch(r"r'([^'\\]|\\.)*'"),
            RegExMatch(r'r"([^"\\]|\\.)*"'),
        ]

    @classmethod
    @returns_parsing_expression
    def SYNTAX_REFERENCE(cls) -> ParsingExpressionLike:
        return [cls.LEXICAL_REFERENCE, (cls.SYNTAX_RULE, Not(":"))]

    @staticmethod
    @returns_parsing_expression
    def SYNTAX_RULE() -> RegExMatch:
        return RegExMatch(r"[a-z](([0-9a-z]*-)*[0-9a-z]+)?")

    @staticmethod
    @returns_parsing_expression
    def TEXT() -> ParsingExpressionLike:
        return [
            RegExMatch(r"'([^']|'(?='))*'"),
            RegExMatch(r'"([^"]|"(?="))*"'),
        ]

    # ## PEG syntax rules
    @classmethod
    @returns_parsing_expression
    def grammar(cls) -> ParsingExpressionLike:
        return (
            OneOrMore(
                [
                    cls.keyword_list,
                    cls.lexical_rule_statement,
                    cls.syntax_rule_statement,
                ]
            ),
            EndOfFile(),
        )

    @classmethod
    @returns_parsing_expression
    def keyword_list(cls) -> ParsingExpressionLike:
        return OneOrMore(cls.KEYWORD, sep="|")

    @classmethod
    @returns_parsing_expression
    def lexical_rule_statement(cls) -> ParsingExpressionLike:
        return (
            cls.LEXICAL_RULE,
            "=",
            cls.lexical_expression,
        )

    @classmethod
    @returns_parsing_expression
    def syntax_rule_statement(cls) -> ParsingExpressionLike:
        return (
            cls.SYNTAX_RULE,
            ":",
            cls.syntax_expression,
        )

    # ## Lexical expression
    @classmethod
    @returns_parsing_expression
    def lexical_expression(cls) -> ParsingExpressionLike:
        return (cls.lexical_ordered_choice,)

    @classmethod
    @returns_parsing_expression
    def lexical_ordered_choice(cls) -> ParsingExpressionLike:
        return OneOrMore(cls.lexical_sequence, sep="|")

    @classmethod
    @returns_parsing_expression
    def lexical_sequence(cls) -> ParsingExpressionLike:
        return OneOrMore(cls.lexical_quantity)

    @classmethod
    @returns_parsing_expression
    def lexical_quantity(cls) -> ParsingExpressionLike:
        return [
            ("[", cls.lexical_expression, "]"),
            ("{", cls.lexical_expression, "}"),
            cls.lexical_primary,
        ]

    @classmethod
    @returns_parsing_expression
    def lexical_primary(cls) -> ParsingExpressionLike:
        return [
            ("(", cls.lexical_expression, ")"),
            cls.REGEX,
            cls.TEXT,
            cls.LEXICAL_REFERENCE,
        ]

    # ## Syntax expression
    @classmethod
    @returns_parsing_expression
    def syntax_expression(cls) -> ParsingExpressionLike:
        return (cls.syntax_ordered_choice,)

    @classmethod
    @returns_parsing_expression
    def syntax_ordered_choice(cls) -> ParsingExpressionLike:
        return OneOrMore(cls.syntax_sequence, sep="|")

    @classmethod
    @returns_parsing_expression
    def syntax_sequence(cls) -> ParsingExpressionLike:
        return OneOrMore(cls.syntax_quantity)

    @classmethod
    @returns_parsing_expression
    def syntax_quantity(cls) -> ParsingExpressionLike:
        return [
            ("[", cls.syntax_expression, "]"),
            ("{", cls.syntax_expression, "}"),
            cls.syntax_primary,
        ]

    @classmethod
    @returns_parsing_expression
    def syntax_primary(cls) -> ParsingExpressionLike:
        return [
            ("(", cls.syntax_expression, ")"),
            cls.KEYWORD,
            cls.TEXT,
            cls.SYNTAX_REFERENCE,
        ]
