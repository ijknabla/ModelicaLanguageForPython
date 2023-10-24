from arpeggio import EOF, Not, OneOrMore, RegExMatch

from modelicalang._backend import ParsingExpressionLike, SyntaxMeta


class PEGSyntax(metaclass=SyntaxMeta):
    # ## PEG comment rule
    @staticmethod
    def COMMENT() -> ParsingExpressionLike:
        return [
            RegExMatch(r"//.*"),
            RegExMatch(r"/\*([^*]|\*[^/])*\*/"),
        ]

    # ## PEG lexical rules
    @staticmethod
    def KEYWORD() -> RegExMatch:
        return RegExMatch("`[a-z]+`")

    @classmethod
    def LEXICAL_REFERENCE(cls) -> ParsingExpressionLike:
        return cls.LEXICAL_RULE, Not("=")

    @staticmethod
    def LEXICAL_RULE() -> RegExMatch:
        return RegExMatch(r"[A-Z]([\-0-9A-Z_]*[0-9A-Z])?")

    @staticmethod
    def REGEX() -> ParsingExpressionLike:
        return [
            RegExMatch(r"r'([^'\\]|\\.)*'"),
            RegExMatch(r'r"([^"\\]|\\.)*"'),
        ]

    @classmethod
    def SYNTAX_REFERENCE(cls) -> ParsingExpressionLike:
        return [cls.LEXICAL_REFERENCE, (cls.SYNTAX_RULE, Not(":"))]

    @staticmethod
    def SYNTAX_RULE() -> RegExMatch:
        return RegExMatch(r"[a-z]([\-0-9_a-z]*[0-9a-z])?")

    @staticmethod
    def TEXT() -> ParsingExpressionLike:
        return [
            RegExMatch(r"'([^']|'(?='))*'"),
            RegExMatch(r'"([^"]|"(?="))*"'),
        ]

    # ## PEG syntax rules
    @classmethod
    def grammar(cls) -> ParsingExpressionLike:
        return (
            OneOrMore(
                [
                    cls.keyword_list,
                    cls.lexical_rule_statement,
                    cls.syntax_rule_statement,
                ]
            ),
            EOF,
        )

    @classmethod
    def keyword_list(cls) -> ParsingExpressionLike:
        return OneOrMore(cls.KEYWORD, sep="|")

    @classmethod
    def lexical_rule_statement(cls) -> ParsingExpressionLike:
        return (
            cls.LEXICAL_RULE,
            "=",
            cls.lexical_expression,
        )

    @classmethod
    def syntax_rule_statement(cls) -> ParsingExpressionLike:
        return (
            cls.SYNTAX_RULE,
            ":",
            cls.syntax_expression,
        )

    # ## Lexical expression
    @classmethod
    def lexical_expression(cls) -> ParsingExpressionLike:
        return (cls.lexical_ordered_choice,)

    @classmethod
    def lexical_ordered_choice(cls) -> ParsingExpressionLike:
        return OneOrMore(cls.lexical_sequence, sep="|")

    @classmethod
    def lexical_sequence(cls) -> ParsingExpressionLike:
        return OneOrMore(cls.lexical_quantity)

    @classmethod
    def lexical_quantity(cls) -> ParsingExpressionLike:
        return [
            ("[", cls.lexical_expression, "]"),
            ("{", cls.lexical_expression, "}"),
            cls.lexical_primary,
        ]

    @classmethod
    def lexical_primary(cls) -> ParsingExpressionLike:
        return [
            ("(", cls.lexical_expression, ")"),
            cls.REGEX,
            cls.TEXT,
            cls.LEXICAL_REFERENCE,
        ]

    # ## Syntax expression
    @classmethod
    def syntax_expression(cls) -> ParsingExpressionLike:
        return (cls.syntax_ordered_choice,)

    @classmethod
    def syntax_ordered_choice(cls) -> ParsingExpressionLike:
        return OneOrMore(cls.syntax_sequence, sep="|")

    @classmethod
    def syntax_sequence(cls) -> ParsingExpressionLike:
        return OneOrMore(cls.syntax_quantity)

    @classmethod
    def syntax_quantity(cls) -> ParsingExpressionLike:
        return [
            ("[", cls.syntax_expression, "]"),
            ("{", cls.syntax_expression, "}"),
            cls.syntax_primary,
        ]

    @classmethod
    def syntax_primary(cls) -> ParsingExpressionLike:
        return [
            ("(", cls.syntax_expression, ")"),
            cls.KEYWORD,
            cls.TEXT,
            cls.SYNTAX_REFERENCE,
        ]
