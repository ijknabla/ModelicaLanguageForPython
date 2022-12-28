from arpeggio import Not, Optional, RegExMatch, ZeroOrMore

from .. import regex, syntax

any_keyword = (
    r"("
    r"algorithm|and|annotation|block|break|class|connect|connector|"
    r"constant|constrainedby|der|discrete|each|else|elseif|elsewhen|"
    r"encapsulated|end|enumeration|equation|expandable|extends|external|"
    r"false|final|flow|for|function|if|import|impure|in|initial|inner|"
    r"input|loop|model|not|operator|or|outer|output|package|parameter|"
    r"partial|protected|public|pure|record|redeclare|replaceable|return|"
    r"stream|then|true|type|when|while|within"
    r")(?!\w)"
)


def regexPEG(regex: str) -> str:
    return "r'{}'".format(regex.replace("'", r"\'"))


class Syntax:
    # §2.3.3 Modelica Keywords
    @staticmethod
    def ANY_KEYWORD() -> RegExMatch:
        return RegExMatch(any_keyword)

    ANY_KEYWORD.__doc__ = f"ANY_KEYWORD = r'{any_keyword}'"

    @staticmethod
    def ALGORITHM() -> RegExMatch:
        r"ALGORITHM = r'algorithm(?!\w)'"
        return RegExMatch(r"algorithm(?!\w)")

    @staticmethod
    def AND() -> RegExMatch:
        r"AND = r'and(?!\w)'"
        return RegExMatch(r"and(?!\w)")

    @staticmethod
    def ANNOTATION() -> RegExMatch:
        r"ANNOTATION = r'annotation(?!\w)'"
        return RegExMatch(r"annotation(?!\w)")

    @staticmethod
    def BLOCK() -> RegExMatch:
        r"BLOCK = r'block(?!\w)'"
        return RegExMatch(r"block(?!\w)")

    @staticmethod
    def BREAK() -> RegExMatch:
        r"BREAK = r'break(?!\w)'"
        return RegExMatch(r"break(?!\w)")

    @staticmethod
    def CLASS() -> RegExMatch:
        r"CLASS = r'class(?!\w)'"
        return RegExMatch(r"class(?!\w)")

    @staticmethod
    def CONNECT() -> RegExMatch:
        r"CONNECT = r'connect(?!\w)'"
        return RegExMatch(r"connect(?!\w)")

    @staticmethod
    def CONNECTOR() -> RegExMatch:
        r"CONNECTOR = r'connector(?!\w)'"
        return RegExMatch(r"connector(?!\w)")

    @staticmethod
    def CONSTANT() -> RegExMatch:
        r"CONSTANT = r'constant(?!\w)'"
        return RegExMatch(r"constant(?!\w)")

    @staticmethod
    def CONSTRAINEDBY() -> RegExMatch:
        r"CONSTRAINEDBY = r'constrainedby(?!\w)'"
        return RegExMatch(r"constrainedby(?!\w)")

    @staticmethod
    def DER() -> RegExMatch:
        r"DER = r'der(?!\w)'"
        return RegExMatch(r"der(?!\w)")

    @staticmethod
    def DISCRETE() -> RegExMatch:
        r"DISCRETE = r'discrete(?!\w)'"
        return RegExMatch(r"discrete(?!\w)")

    @staticmethod
    def EACH() -> RegExMatch:
        r"EACH = r'each(?!\w)'"
        return RegExMatch(r"each(?!\w)")

    @staticmethod
    def ELSE() -> RegExMatch:
        r"ELSE = r'else(?!\w)'"
        return RegExMatch(r"else(?!\w)")

    @staticmethod
    def ELSEIF() -> RegExMatch:
        r"ELSEIF = r'elseif(?!\w)'"
        return RegExMatch(r"elseif(?!\w)")

    @staticmethod
    def ELSEWHEN() -> RegExMatch:
        r"ELSEWHEN = r'elsewhen(?!\w)'"
        return RegExMatch(r"elsewhen(?!\w)")

    @staticmethod
    def ENCAPSULATED() -> RegExMatch:
        r"ENCAPSULATED = r'encapsulated(?!\w)'"
        return RegExMatch(r"encapsulated(?!\w)")

    @staticmethod
    def END() -> RegExMatch:
        r"END = r'end(?!\w)'"
        return RegExMatch(r"end(?!\w)")

    @staticmethod
    def ENUMERATION() -> RegExMatch:
        r"ENUMERATION = r'enumeration(?!\w)'"
        return RegExMatch(r"enumeration(?!\w)")

    @staticmethod
    def EQUATION() -> RegExMatch:
        r"EQUATION = r'equation(?!\w)'"
        return RegExMatch(r"equation(?!\w)")

    @staticmethod
    def EXPANDABLE() -> RegExMatch:
        r"EXPANDABLE = r'expandable(?!\w)'"
        return RegExMatch(r"expandable(?!\w)")

    @staticmethod
    def EXTENDS() -> RegExMatch:
        r"EXTENDS = r'extends(?!\w)'"
        return RegExMatch(r"extends(?!\w)")

    @staticmethod
    def EXTERNAL() -> RegExMatch:
        r"EXTERNAL = r'external(?!\w)'"
        return RegExMatch(r"external(?!\w)")

    @staticmethod
    def FALSE() -> RegExMatch:
        r"FALSE = r'false(?!\w)'"
        return RegExMatch(r"false(?!\w)")

    @staticmethod
    def FINAL() -> RegExMatch:
        r"FINAL = r'final(?!\w)'"
        return RegExMatch(r"final(?!\w)")

    @staticmethod
    def FLOW() -> RegExMatch:
        r"FLOW = r'flow(?!\w)'"
        return RegExMatch(r"flow(?!\w)")

    @staticmethod
    def FOR() -> RegExMatch:
        r"FOR = r'for(?!\w)'"
        return RegExMatch(r"for(?!\w)")

    @staticmethod
    def FUNCTION() -> RegExMatch:
        r"FUNCTION = r'function(?!\w)'"
        return RegExMatch(r"function(?!\w)")

    @staticmethod
    def IF() -> RegExMatch:
        r"IF = r'if(?!\w)'"
        return RegExMatch(r"if(?!\w)")

    @staticmethod
    def IMPORT() -> RegExMatch:
        r"IMPORT = r'import(?!\w)'"
        return RegExMatch(r"import(?!\w)")

    @staticmethod
    def IMPURE() -> RegExMatch:
        r"IMPURE = r'impure(?!\w)'"
        return RegExMatch(r"impure(?!\w)")

    @staticmethod
    def IN() -> RegExMatch:
        r"IN = r'in(?!\w)'"
        return RegExMatch(r"in(?!\w)")

    @staticmethod
    def INITIAL() -> RegExMatch:
        r"INITIAL = r'initial(?!\w)'"
        return RegExMatch(r"initial(?!\w)")

    @staticmethod
    def INNER() -> RegExMatch:
        r"INNER = r'inner(?!\w)'"
        return RegExMatch(r"inner(?!\w)")

    @staticmethod
    def INPUT() -> RegExMatch:
        r"INPUT = r'input(?!\w)'"
        return RegExMatch(r"input(?!\w)")

    @staticmethod
    def LOOP() -> RegExMatch:
        r"LOOP = r'loop(?!\w)'"
        return RegExMatch(r"loop(?!\w)")

    @staticmethod
    def MODEL() -> RegExMatch:
        r"MODEL = r'model(?!\w)'"
        return RegExMatch(r"model(?!\w)")

    @staticmethod
    def NOT() -> RegExMatch:
        r"NOT = r'not(?!\w)'"
        return RegExMatch(r"not(?!\w)")

    @staticmethod
    def OPERATOR() -> RegExMatch:
        r"OPERATOR = r'operator(?!\w)'"
        return RegExMatch(r"operator(?!\w)")

    @staticmethod
    def OR() -> RegExMatch:
        r"OR = r'or(?!\w)'"
        return RegExMatch(r"or(?!\w)")

    @staticmethod
    def OUTER() -> RegExMatch:
        r"OUTER = r'outer(?!\w)'"
        return RegExMatch(r"outer(?!\w)")

    @staticmethod
    def OUTPUT() -> RegExMatch:
        r"OUTPUT = r'output(?!\w)'"
        return RegExMatch(r"output(?!\w)")

    @staticmethod
    def PACKAGE() -> RegExMatch:
        r"PACKAGE = r'package(?!\w)'"
        return RegExMatch(r"package(?!\w)")

    @staticmethod
    def PARAMETER() -> RegExMatch:
        r"PARAMETER = r'parameter(?!\w)'"
        return RegExMatch(r"parameter(?!\w)")

    @staticmethod
    def PARTIAL() -> RegExMatch:
        r"PARTIAL = r'partial(?!\w)'"
        return RegExMatch(r"partial(?!\w)")

    @staticmethod
    def PROTECTED() -> RegExMatch:
        r"PROTECTED = r'protected(?!\w)'"
        return RegExMatch(r"protected(?!\w)")

    @staticmethod
    def PUBLIC() -> RegExMatch:
        r"PUBLIC = r'public(?!\w)'"
        return RegExMatch(r"public(?!\w)")

    @staticmethod
    def PURE() -> RegExMatch:
        r"PURE = r'pure(?!\w)'"
        return RegExMatch(r"pure(?!\w)")

    @staticmethod
    def RECORD() -> RegExMatch:
        r"RECORD = r'record(?!\w)'"
        return RegExMatch(r"record(?!\w)")

    @staticmethod
    def REDECLARE() -> RegExMatch:
        r"REDECLARE = r'redeclare(?!\w)'"
        return RegExMatch(r"redeclare(?!\w)")

    @staticmethod
    def REPLACEABLE() -> RegExMatch:
        r"REPLACEABLE = r'replaceable(?!\w)'"
        return RegExMatch(r"replaceable(?!\w)")

    @staticmethod
    def RETURN() -> RegExMatch:
        r"RETURN = r'return(?!\w)'"
        return RegExMatch(r"return(?!\w)")

    @staticmethod
    def STREAM() -> RegExMatch:
        r"STREAM = r'stream(?!\w)'"
        return RegExMatch(r"stream(?!\w)")

    @staticmethod
    def THEN() -> RegExMatch:
        r"THEN = r'then(?!\w)'"
        return RegExMatch(r"then(?!\w)")

    @staticmethod
    def TRUE() -> RegExMatch:
        r"TRUE = r'true(?!\w)'"
        return RegExMatch(r"true(?!\w)")

    @staticmethod
    def TYPE() -> RegExMatch:
        r"TYPE = r'type(?!\w)'"
        return RegExMatch(r"type(?!\w)")

    @staticmethod
    def WHEN() -> RegExMatch:
        r"WHEN = r'when(?!\w)'"
        return RegExMatch(r"when(?!\w)")

    @staticmethod
    def WHILE() -> RegExMatch:
        r"WHILE = r'while(?!\w)'"
        return RegExMatch(r"while(?!\w)")

    @staticmethod
    def WITHIN() -> RegExMatch:
        r"WITHIN = r'within(?!\w)'"
        return RegExMatch(r"within(?!\w)")

    # §B.1 Lexical conventions
    @classmethod
    def IDENT(cls):  # type: ignore
        return Not(cls.ANY_KEYWORD), RegExMatch(regex.ident)

    IDENT.__doc__ = f"IDENT = !ANY_KEYWORD {regexPEG(regex.ident)}"

    @staticmethod
    def STRING() -> RegExMatch:
        return RegExMatch(regex.string)

    STRING.__doc__ = f"STRING = {regexPEG(regex.string)}"

    @staticmethod
    def UNSIGNED_NUMBER() -> RegExMatch:
        return RegExMatch(regex.unsigned_number)

    UNSIGNED_NUMBER.__doc__ = (
        f"UNSIGNED_NUMBER = {regexPEG(regex.unsigned_number)}"
    )

    @staticmethod
    def CPP_STYLE_COMMENT() -> RegExMatch:
        return RegExMatch(regex.cpp_style_comment)

    CPP_STYLE_COMMENT.__doc__ = (
        f"CPP_STYLE_COMMENT = {regexPEG(regex.cpp_style_comment)}"
    )

    # §B.2 Grammar
    # §B.2.1 Stored Definition - Within
    @classmethod
    def stored_definition(cls):  # type: ignore
        """
        stored_definition =
            (WITHIN name? ";")?
            (FINAL? class_definition ";")*
        """
        return (
            Optional(cls.WITHIN, Optional(syntax.name), ";"),
            ZeroOrMore(Optional(cls.FINAL), cls.class_definition, ";"),
        )

    # §B.2.2 Class Definition
    @classmethod
    def class_definition(cls):  # type: ignore
        """
        class_definition =
            ENCAPSULATED? class_prefixes class_specifier
        """
        return (
            Optional(cls.ENCAPSULATED),
            cls.class_prefixes,
            cls.class_specifier,
        )

    @classmethod
    def class_prefixes(cls):  # type: ignore
        """
        class_prefixes =
            PARTIAL?
            (
                CLASS / MODEL / OPERATOR? RECORD / BLOCK / EXPANDABLE? CONNECTOR
                / TYPE / PACKAGE / (PURE / IMPURE)? OPERATOR? FUNCTION / OPERATOR
            )
        """  # noqa: E501
        return (
            Optional(cls.PARTIAL),
            [
                cls.CLASS,
                cls.MODEL,
                (Optional(cls.OPERATOR), cls.RECORD),
                cls.BLOCK,
                (Optional(cls.EXPANDABLE), cls.CONNECTOR),
                cls.TYPE,
                cls.PACKAGE,
                (
                    Optional([cls.PURE, cls.IMPURE]),
                    Optional(cls.OPERATOR),
                    cls.FUNCTION,
                ),
                cls.OPERATOR,
            ],
        )

    @classmethod
    def class_specifier(cls):  # type: ignore
        """
        class_specifier =
            long_class_specifier / short_class_specifier / der_class_specifier
        """
        return [
            cls.long_class_specifier,
            cls.short_class_specifier,
            cls.der_class_specifier,
        ]

    @classmethod
    def long_class_specifier(cls):  # type: ignore
        """
        long_class_specifier =
            EXTENDS IDENT class_modification? string_comment composition END IDENT
            / IDENT string_comment composition END IDENT
        """  # noqa: E501
        return [
            (
                cls.EXTENDS,
                cls.IDENT,
                Optional(syntax.class_modification),
                syntax.string_comment,
                cls.composition,
                cls.END,
                cls.IDENT,
            ),
            (
                cls.IDENT,
                syntax.string_comment,
                cls.composition,
                cls.END,
                cls.IDENT,
            ),
        ]

    @classmethod
    def short_class_specifier(cls):  # type: ignore
        """
        short_class_specifier =
            IDENT "=" ENUMERATION "(" (":" / enum_list?) ")" comment
            / IDENT "=" base_prefix type_specifier array_subscripts?
            class_modification? comment
        """
        return [
            (
                cls.IDENT,
                "=",
                cls.ENUMERATION,
                "(",
                [":", Optional(cls.enum_list)],
                ")",
                syntax.comment,
            ),
            (
                cls.IDENT,
                "=",
                cls.base_prefix,
                syntax.type_specifier,
                Optional(syntax.array_subscripts),
                Optional(syntax.class_modification),
                syntax.comment,
            ),
        ]

    @classmethod
    def der_class_specifier(cls):  # type: ignore
        """
        der_class_specifer =
            IDENT "=" DER "(" type_specifier "," IDENT ("," IDENT)* ")" comment
        """
        return (
            cls.IDENT,
            "=",
            cls.DER,
            "(",
            syntax.type_specifier,
            ",",
            cls.IDENT,
            ZeroOrMore(",", cls.IDENT),
            ")",
            syntax.comment,
        )

    @classmethod
    def base_prefix(cls):  # type: ignore
        """
        base_prefix =
            (INPUT / OUTPUT)?
        """
        return Optional([cls.INPUT, cls.OUTPUT])

    @classmethod
    def enum_list(cls):  # type: ignore
        """
        enum_list = enumeration_literal ("," enumeration_literal)*
        """
        return cls.enumeration_literal, ZeroOrMore(
            ",", cls.enumeration_literal
        )

    @classmethod
    def enumeration_literal(cls):  # type: ignore
        """
        enumeration_literal = IDENT comment
        """
        return cls.IDENT, syntax.comment

    @classmethod
    def composition(cls):  # type: ignore
        """
        composition =
            element_list
            (
                PUBLIC element_list
                / PROTECTED element_list
                / equation_section
                / algorithm_section
            )*
            (
                EXTERNAL language_specification?
                external_function_call? annotation? ";"
            )?
            (annotation ";")?
        """
        return (
            cls.element_list,
            ZeroOrMore(
                [
                    (cls.PUBLIC, cls.element_list),  # type: ignore
                    (cls.PROTECTED, cls.element_list),  # type: ignore
                    syntax.equation_section,
                    syntax.algorithm_section,
                ]
            ),
            Optional(
                cls.EXTERNAL,
                Optional(cls.language_specification),
                Optional(cls.external_function_call),
                Optional(syntax.annotation),
                ";",
            ),
            Optional(syntax.annotation, ";"),
        )

    @classmethod
    def language_specification(cls):  # type: ignore
        """
        language_specification =
            STRING
        """
        return cls.STRING

    @classmethod
    def external_function_call(cls):  # type: ignore
        """
        external_function_call =
            (component_reference "=")? IDENT "(" expression_list? ")"
        """
        return (
            Optional(syntax.component_reference, "="),
            cls.IDENT,
            "(",
            Optional(syntax.expression_list),
            ")",
        )

    @classmethod
    def element_list(cls):  # type: ignore
        """
        element_list =
            (element ";")*
        """
        return ZeroOrMore(cls.element, ";")

    @classmethod
    def element(cls):  # type: ignore
        """
        element =
            import_clause
            extends_clause
            / REDECLARE? FINAL? INNER? OUTER?
                (
                    REPLACEABLE (class_definition / component_clause)
                    (constraining_clause comment)?
                    / (class_definition / component_clause)
                )
        """
        return [
            cls.import_clause,
            cls.extends_clause,
            (
                Optional(cls.REDECLARE),
                Optional(cls.FINAL),
                Optional(cls.INNER),
                Optional(cls.OUTER),
                [
                    (
                        cls.REPLACEABLE,
                        [cls.class_definition, syntax.component_clause],
                        Optional(cls.constraining_clause, syntax.comment),
                    ),
                    [cls.class_definition, syntax.component_clause],
                ],
            ),
        ]

    @classmethod
    def import_clause(cls):  # type: ignore
        """
        import_clause =
            import
            (
                IDENT "=" name
                / name ("." ("*" / "{" import_list "}") )?
            )
            comment
        """
        return (
            cls.IMPORT,
            [
                (cls.IDENT, "=", syntax.name),
                (
                    syntax.name,
                    Optional(
                        ".",
                        [
                            "*",
                            ("{", cls.import_list, "}"),  # type: ignore
                        ],
                    ),
                ),
            ],
            syntax.comment,
        )

    @classmethod
    def import_list(cls):  # type: ignore
        """
        import_list =
            IDENT ("," IDENT)*
        """
        return cls.IDENT, ZeroOrMore(",", cls.IDENT)

    # §B.2.3 Extends
    @classmethod
    def extends_clause(cls):  # type: ignore
        """
        extends_clause =
            EXTENDS type_specifier class_modification? annotation?
        """
        return (
            cls.EXTENDS,
            syntax.type_specifier,
            Optional(syntax.class_modification),
            Optional(syntax.annotation),
        )

    @classmethod
    def constraining_clause(cls):  # type: ignore
        """
        constraining_clause =
            CONSTRAINEDBY type_specifier class_modification?
        """
        return (
            cls.CONSTRAINEDBY,
            syntax.type_specifier,
            Optional(syntax.class_modification),
        )
