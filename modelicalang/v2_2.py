from typing import ClassVar, Tuple

from arpeggio import Optional, RegExMatch, ZeroOrMore

from modelicalang._backend import (
    ParsingExpressionLike,
    not_start_with_keyword,
    returns_parsing_expression,
)


class Syntax:
    _keywords_: ClassVar[Tuple[str, ...]] = (
        "algorithm",
        "and",
        "block",
        "break",
        "class",
        "connect",
        "connector",
        "constant",
        "der",
        "discrete",
        "each",
        "else",
        "elseif",
        "elsewhen",
        "encapsulated",
        "end",
        "enumeration",
        "equation",
        "expandable",
        "extends",
        "external",
        "false",
        "final",
        "flow",
        "for",
        "function",
        "if",
        "import",
        "in",
        "initial",
        "inner",
        "input",
        "loop",
        "model",
        "not",
        "or",
        "outer",
        "output",
        "package",
        "parameter",
        "partial",
        "protected",
        "public",
        "record",
        "redeclare",
        "replaceable",
        "return",
        "then",
        "true",
        "type",
        "when",
        "while",
        "within",
    )

    @staticmethod
    @returns_parsing_expression
    def ALGORITHM() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ALGORITHM = `algorithm`
        """
        return RegExMatch("algorithm(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def AND() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            AND = `and`
        """
        return RegExMatch("and(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def BLOCK() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            BLOCK = `block`
        """
        return RegExMatch("block(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def BREAK() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            BREAK = `break`
        """
        return RegExMatch("break(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def CLASS() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            CLASS = `class`
        """
        return RegExMatch("class(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def CONNECT() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            CONNECT = `connect`
        """
        return RegExMatch("connect(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def CONNECTOR() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            CONNECTOR = `connector`
        """
        return RegExMatch("connector(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def CONSTANT() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            CONSTANT = `constant`
        """
        return RegExMatch("constant(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def DER() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            DER = `der`
        """
        return RegExMatch("der(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def DISCRETE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            DISCRETE = `discrete`
        """
        return RegExMatch("discrete(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def EACH() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            EACH = `each`
        """
        return RegExMatch("each(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def ELSE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ELSE = `else`
        """
        return RegExMatch("else(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def ELSEIF() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ELSEIF = `elseif`
        """
        return RegExMatch("elseif(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def ELSEWHEN() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ELSEWHEN = `elsewhen`
        """
        return RegExMatch("elsewhen(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def ENCAPSULATED() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ENCAPSULATED = `encapsulated`
        """
        return RegExMatch("encapsulated(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def END() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            END = `end`
        """
        return RegExMatch("end(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def ENUMERATION() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ENUMERATION = `enumeration`
        """
        return RegExMatch("enumeration(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def EQUATION() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            EQUATION = `equation`
        """
        return RegExMatch("equation(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def EXPANDABLE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            EXPANDABLE = `expandable`
        """
        return RegExMatch("expandable(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def EXTENDS() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            EXTENDS = `extends`
        """
        return RegExMatch("extends(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def EXTERNAL() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            EXTERNAL = `external`
        """
        return RegExMatch("external(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def FALSE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            FALSE = `false`
        """
        return RegExMatch("false(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def FINAL() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            FINAL = `final`
        """
        return RegExMatch("final(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def FLOW() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            FLOW = `flow`
        """
        return RegExMatch("flow(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def FOR() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            FOR = `for`
        """
        return RegExMatch("for(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def FUNCTION() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            FUNCTION = `function`
        """
        return RegExMatch("function(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def IF() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            IF = `if`
        """
        return RegExMatch("if(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def IMPORT() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            IMPORT = `import`
        """
        return RegExMatch("import(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def IN() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            IN = `in`
        """
        return RegExMatch("in(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def INITIAL() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            INITIAL = `initial`
        """
        return RegExMatch("initial(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def INNER() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            INNER = `inner`
        """
        return RegExMatch("inner(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def INPUT() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            INPUT = `input`
        """
        return RegExMatch("input(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def LOOP() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            LOOP = `loop`
        """
        return RegExMatch("loop(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def MODEL() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            MODEL = `model`
        """
        return RegExMatch("model(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def NOT() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            NOT = `not`
        """
        return RegExMatch("not(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def OR() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            OR = `or`
        """
        return RegExMatch("or(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def OUTER() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            OUTER = `outer`
        """
        return RegExMatch("outer(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def OUTPUT() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            OUTPUT = `output`
        """
        return RegExMatch("output(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def PACKAGE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            PACKAGE = `package`
        """
        return RegExMatch("package(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def PARAMETER() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            PARAMETER = `parameter`
        """
        return RegExMatch("parameter(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def PARTIAL() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            PARTIAL = `partial`
        """
        return RegExMatch("partial(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def PROTECTED() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            PROTECTED = `protected`
        """
        return RegExMatch("protected(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def PUBLIC() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            PUBLIC = `public`
        """
        return RegExMatch("public(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def RECORD() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            RECORD = `record`
        """
        return RegExMatch("record(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def REDECLARE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            REDECLARE = `redeclare`
        """
        return RegExMatch("redeclare(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def REPLACEABLE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            REPLACEABLE = `replaceable`
        """
        return RegExMatch("replaceable(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def RETURN() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            RETURN = `return`
        """
        return RegExMatch("return(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def THEN() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            THEN = `then`
        """
        return RegExMatch("then(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def TRUE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            TRUE = `true`
        """
        return RegExMatch("true(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def TYPE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            TYPE = `type`
        """
        return RegExMatch("type(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def WHEN() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            WHEN = `when`
        """
        return RegExMatch("when(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def WHILE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            WHILE = `while`
        """
        return RegExMatch("while(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def WITHIN() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            WITHIN = `within`
        """
        return RegExMatch("within(?![0-9A-Z_a-z])")

    @classmethod
    @not_start_with_keyword
    @returns_parsing_expression
    def IDENT(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            IDENT = NONDIGIT { DIGIT | NONDIGIT } | Q-IDENT
        """
        return RegExMatch(
            "[A-Z_a-z][0-9A-Z_a-z]*|'([^'\\\\]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)([^'\\\\]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*'"
        )

    @classmethod
    @returns_parsing_expression
    def Q_IDENT(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            Q-IDENT = "'" ( Q-CHAR | S-ESCAPE ) { Q-CHAR | S-ESCAPE } "'"
        """
        return RegExMatch(
            "'([^'\\\\]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)([^'\\\\]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*'"
        )

    @classmethod
    @returns_parsing_expression
    def NONDIGIT(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            NONDIGIT = "_" | r'[a-z]' | r'[A-Z]'
        """
        return RegExMatch("[A-Z_a-z]")

    @classmethod
    @returns_parsing_expression
    def STRING(cls) -> RegExMatch:
        '''
        .. code-block:: modelicapeg

            STRING = """ { S-CHAR | S-ESCAPE } """
        '''
        return RegExMatch(
            '"([^"\\\\]|\\\\\'|\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*"'
        )

    @classmethod
    @returns_parsing_expression
    def S_CHAR(cls) -> RegExMatch:
        '''
        .. code-block:: modelicapeg

            S-CHAR =
               // any member of the source character set except double-quote """, and backslash "\\"
               r'[^"\\\\]'
        '''
        return RegExMatch('[^"\\\\]')

    @classmethod
    @returns_parsing_expression
    def Q_CHAR(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            Q-CHAR =
               // any member of the source character set except single-quote "’", and backslash "\\"
               r"[^'\\\\]"
        """
        return RegExMatch("[^'\\\\]")

    @classmethod
    @returns_parsing_expression
    def S_ESCAPE(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            S-ESCAPE = "\\'" | "\\"" | "\\?" | "\\\\" |
             "\\a" | "\\b" | "\\f" | "\\n" | "\\r" | "\\t" | "\\v"
        """
        return RegExMatch(
            "\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v"
        )

    @classmethod
    @returns_parsing_expression
    def DIGIT(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
        """
        return RegExMatch("[0-9]")

    @classmethod
    @returns_parsing_expression
    def UNSIGNED_INTEGER(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            UNSIGNED_INTEGER = DIGIT { DIGIT }
        """
        return RegExMatch("[0-9][0-9]*")

    @classmethod
    @returns_parsing_expression
    def UNSIGNED_NUMBER(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            UNSIGNED_NUMBER = UNSIGNED_INTEGER [ "." [ UNSIGNED_INTEGER ] ]
             [ ( "e" | "E" ) [ "+" | "-" ] UNSIGNED_INTEGER ]
        """
        return RegExMatch(
            "[0-9][0-9]*(\\.([0-9][0-9]*)?)?([Ee][\\+\\-]?[0-9][0-9]*)?"
        )

    @classmethod
    @returns_parsing_expression
    def COMMENT(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            COMMENT =
               // line comment
               r'//.*'
               /* multi-line comment */
               | r'/\\*([^*]|\\*(?!/))*\\*/'
        """
        return RegExMatch("//.*|/\\*([^*]|\\*(?!/))*\\*/")

    @classmethod
    @returns_parsing_expression
    def stored_definition(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            stored_definition:
             [ `within` [ name ] ";" ]
             { [ `final` ] class_definition ";" }
        """
        return (
            Optional(cls.WITHIN, Optional(cls.name), ";"),
            ZeroOrMore(Optional(cls.FINAL), cls.class_definition, ";"),
        )

    @classmethod
    @returns_parsing_expression
    def class_definition(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            class_definition :
             [ `encapsulated` ]
             [ `partial` ]
             ( `class` | `model` | `record` | `block` | [ `expandable` ] `connector` | `type` |
             `package` | `function` )
             class_specifier
        """
        return (
            Optional(cls.ENCAPSULATED),
            Optional(cls.PARTIAL),
            [
                cls.CLASS,
                cls.MODEL,
                cls.RECORD,
                cls.BLOCK,
                (Optional(cls.EXPANDABLE), cls.CONNECTOR),
                cls.TYPE,
                cls.PACKAGE,
                cls.FUNCTION,
            ],
            cls.class_specifier,
        )

    @classmethod
    @returns_parsing_expression
    def class_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            class_specifier :
             IDENT string_comment composition `end` IDENT
             | IDENT "=" base_prefix name [ array_subscripts ]
             [ class_modification ] comment
             | IDENT "=" `enumeration` "(" ( [enum_list] | ":" ) ")" comment
             | IDENT "=" `der` "(" name "," IDENT { "," IDENT } ")" comment
             | `extends` IDENT [ class_modification ] string_comment composition
             `end` IDENT
        """
        return [
            (
                cls.IDENT,
                cls.string_comment,
                cls.composition,
                cls.END,
                cls.IDENT,
            ),
            (
                cls.IDENT,
                "=",
                cls.base_prefix,
                cls.name,
                Optional(cls.array_subscripts),
                Optional(cls.class_modification),
                cls.comment,
            ),
            (
                cls.IDENT,
                "=",
                cls.ENUMERATION,
                "(",
                [Optional(cls.enum_list), ":"],
                ")",
                cls.comment,
            ),
            (
                cls.IDENT,
                "=",
                cls.DER,
                "(",
                cls.name,
                ",",
                cls.IDENT,
                ZeroOrMore(",", cls.IDENT),
                ")",
                cls.comment,
            ),
            (
                cls.EXTENDS,
                cls.IDENT,
                Optional(cls.class_modification),
                cls.string_comment,
                cls.composition,
                cls.END,
                cls.IDENT,
            ),
        ]

    @classmethod
    @returns_parsing_expression
    def base_prefix(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            base_prefix :
             type_prefix
        """
        return cls.type_prefix

    @classmethod
    @returns_parsing_expression
    def enum_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            enum_list : enumeration_literal { "," enumeration_literal}
        """
        return (
            cls.enumeration_literal,
            ZeroOrMore(",", cls.enumeration_literal),
        )

    @classmethod
    @returns_parsing_expression
    def enumeration_literal(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            enumeration_literal : IDENT comment
        """
        return (cls.IDENT, cls.comment)

    @classmethod
    @returns_parsing_expression
    def composition(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            composition :
             element_list
             { `public` element_list |
             `protected` element_list |
             equation_clause |
             algorithm_clause
             }
             [ `external` [ language_specification ]
             [ external_function_call ] [ annotation ";" ]
             [ annotation ";" ] ]
        """
        return (
            cls.element_list,
            ZeroOrMore(
                [
                    (cls.PUBLIC, cls.element_list),
                    (cls.PROTECTED, cls.element_list),
                    cls.equation_clause,
                    cls.algorithm_clause,
                ]
            ),
            Optional(
                cls.EXTERNAL,
                Optional(cls.language_specification),
                Optional(cls.external_function_call),
                Optional(cls.annotation, ";"),
                Optional(cls.annotation, ";"),
            ),
        )

    @classmethod
    @returns_parsing_expression
    def language_specification(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            language_specification :
             STRING
        """
        return cls.STRING

    @classmethod
    @returns_parsing_expression
    def external_function_call(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            external_function_call :
             [ component_reference "=" ]
             IDENT "(" [ expression { "," expression } ] ")"
        """
        return (
            Optional(cls.component_reference, "="),
            cls.IDENT,
            "(",
            Optional(cls.expression, ZeroOrMore(",", cls.expression)),
            ")",
        )

    @classmethod
    @returns_parsing_expression
    def element_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element_list :
             { element ";" | annotation ";" }
        """
        return ZeroOrMore([(cls.element, ";"), (cls.annotation, ";")])

    @classmethod
    @returns_parsing_expression
    def element(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element :
             import_clause |
             extends_clause |
             [ `redeclare` ]
             [ `final` ]
             [ `inner` ] [ `outer` ]
             ( ( class_definition | component_clause) |
             `replaceable` ( class_definition | component_clause)
             [constraining_clause comment])
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
                    [cls.class_definition, cls.component_clause],
                    (
                        cls.REPLACEABLE,
                        [cls.class_definition, cls.component_clause],
                        Optional(cls.constraining_clause, cls.comment),
                    ),
                ],
            ),
        ]

    @classmethod
    @returns_parsing_expression
    def import_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            import_clause :
             `import` ( IDENT "=" name | name ["." "*"] ) comment
        """
        return (
            cls.IMPORT,
            [(cls.IDENT, "=", cls.name), (cls.name, Optional(".", "*"))],
            cls.comment,
        )

    @classmethod
    @returns_parsing_expression
    def extends_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            extends_clause :
             `extends` name [ class_modification ] [annotation]
        """
        return (
            cls.EXTENDS,
            cls.name,
            Optional(cls.class_modification),
            Optional(cls.annotation),
        )

    @classmethod
    @returns_parsing_expression
    def constraining_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            constraining_clause :
             `extends` name [ class_modification ]
        """
        return (cls.EXTENDS, cls.name, Optional(cls.class_modification))

    @classmethod
    @returns_parsing_expression
    def component_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            component_clause:
             type_prefix type_specifier [ array_subscripts ] component_list
        """
        return (
            cls.type_prefix,
            cls.type_specifier,
            Optional(cls.array_subscripts),
            cls.component_list,
        )

    @classmethod
    @returns_parsing_expression
    def type_prefix(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            type_prefix :
             [ `flow` ]
             [ `discrete` | `parameter` | `constant` ] [ `input` | `output` ]
        """
        return (
            Optional(cls.FLOW),
            Optional([cls.DISCRETE, cls.PARAMETER, cls.CONSTANT]),
            Optional([cls.INPUT, cls.OUTPUT]),
        )

    @classmethod
    @returns_parsing_expression
    def type_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            type_specifier :
             name
        """
        return cls.name

    @classmethod
    @returns_parsing_expression
    def component_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            component_list :
             component_declaration { "," component_declaration }
        """
        return (
            cls.component_declaration,
            ZeroOrMore(",", cls.component_declaration),
        )

    @classmethod
    @returns_parsing_expression
    def component_declaration(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            component_declaration :
             declaration [ conditional_attribute ] comment
        """
        return (
            cls.declaration,
            Optional(cls.conditional_attribute),
            cls.comment,
        )

    @classmethod
    @returns_parsing_expression
    def conditional_attribute(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            conditional_attribute:
             `if` expression
        """
        return (cls.IF, cls.expression)

    @classmethod
    @returns_parsing_expression
    def declaration(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            declaration :
             IDENT [ array_subscripts ] [ modification ]
        """
        return (
            cls.IDENT,
            Optional(cls.array_subscripts),
            Optional(cls.modification),
        )

    @classmethod
    @returns_parsing_expression
    def modification(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            modification :
             class_modification [ "=" expression ]
             | "=" expression
             | ":=" expression
        """
        return [
            (cls.class_modification, Optional("=", cls.expression)),
            ("=", cls.expression),
            (":=", cls.expression),
        ]

    @classmethod
    @returns_parsing_expression
    def class_modification(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            class_modification :
             "(" [ argument_list ] ")"
        """
        return ("(", Optional(cls.argument_list), ")")

    @classmethod
    @returns_parsing_expression
    def argument_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            argument_list :
             argument { "," argument }
        """
        return (cls.argument, ZeroOrMore(",", cls.argument))

    @classmethod
    @returns_parsing_expression
    def argument(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            argument :
             element_modification_or_replaceable
             | element_redeclaration
        """
        return [
            cls.element_modification_or_replaceable,
            cls.element_redeclaration,
        ]

    @classmethod
    @returns_parsing_expression
    def element_modification_or_replaceable(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element_modification_or_replaceable:
             [ `each` ] [ `final` ] ( element_modification | element_replaceable)
        """
        return (
            Optional(cls.EACH),
            Optional(cls.FINAL),
            [cls.element_modification, cls.element_replaceable],
        )

    @classmethod
    @returns_parsing_expression
    def element_modification(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element_modification :
             component_reference [ modification ] string_comment
        """
        return (
            cls.component_reference,
            Optional(cls.modification),
            cls.string_comment,
        )

    @classmethod
    @returns_parsing_expression
    def element_redeclaration(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element_redeclaration :
             `redeclare` [ `each` ] [ `final` ]
            ( ( class_definition | component_clause1) | element_replaceable )
        """
        return (
            cls.REDECLARE,
            Optional(cls.EACH),
            Optional(cls.FINAL),
            [
                [cls.class_definition, cls.component_clause1],
                cls.element_replaceable,
            ],
        )

    @classmethod
    @returns_parsing_expression
    def element_replaceable(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element_replaceable:
             `replaceable` ( class_definition | component_clause1)
             [constraining_clause]
        """
        return (
            cls.REPLACEABLE,
            [cls.class_definition, cls.component_clause1],
            Optional(cls.constraining_clause),
        )

    @classmethod
    @returns_parsing_expression
    def component_clause1(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            component_clause1 :
             type_prefix type_specifier component_declaration1
        """
        return (
            cls.type_prefix,
            cls.type_specifier,
            cls.component_declaration1,
        )

    @classmethod
    @returns_parsing_expression
    def component_declaration1(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            component_declaration1 :
             declaration comment
        """
        return (cls.declaration, cls.comment)

    @classmethod
    @returns_parsing_expression
    def equation_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            equation_clause :
             [ `initial` ] `equation` { equation ";" | annotation ";" }
        """
        return (
            Optional(cls.INITIAL),
            cls.EQUATION,
            ZeroOrMore([(cls.equation, ";"), (cls.annotation, ";")]),
        )

    @classmethod
    @returns_parsing_expression
    def algorithm_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            algorithm_clause :
             [ `initial` ] `algorithm` { algorithm ";" | annotation ";" }
        """
        return (
            Optional(cls.INITIAL),
            cls.ALGORITHM,
            ZeroOrMore([(cls.algorithm, ";"), (cls.annotation, ";")]),
        )

    @classmethod
    @returns_parsing_expression
    def equation(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            equation :
             ( simple_expression "=" expression
             | conditional_equation_e
             | for_clause_e
             | connect_clause
             | when_clause_e
             | IDENT function_call )
             comment
        """
        return (
            [
                (cls.simple_expression, "=", cls.expression),
                cls.conditional_equation_e,
                cls.for_clause_e,
                cls.connect_clause,
                cls.when_clause_e,
                (cls.IDENT, cls.function_call),
            ],
            cls.comment,
        )

    @classmethod
    @returns_parsing_expression
    def algorithm(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            algorithm :
             ( component_reference ( ":=" expression | function_call )
             | "(" output_expression_list ")" ":=" component_reference function_call
             | `break`
             | `return`
             | conditional_equation_a
             | for_clause_a
             | while_clause
             | when_clause_a )
             comment
        """
        return (
            [
                (
                    cls.component_reference,
                    [(":=", cls.expression), cls.function_call],
                ),
                (
                    "(",
                    cls.output_expression_list,
                    ")",
                    ":=",
                    cls.component_reference,
                    cls.function_call,
                ),
                cls.BREAK,
                cls.RETURN,
                cls.conditional_equation_a,
                cls.for_clause_a,
                cls.while_clause,
                cls.when_clause_a,
            ],
            cls.comment,
        )

    @classmethod
    @returns_parsing_expression
    def conditional_equation_e(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            conditional_equation_e :
             `if` expression `then`
            { equation ";" }
             { `elseif` expression `then`
             { equation ";" }
             }
             [ `else`
             { equation ";" }
             ]
             `end` `if`
        """
        return (
            cls.IF,
            cls.expression,
            cls.THEN,
            ZeroOrMore(cls.equation, ";"),
            ZeroOrMore(
                cls.ELSEIF,
                cls.expression,
                cls.THEN,
                ZeroOrMore(cls.equation, ";"),
            ),
            Optional(cls.ELSE, ZeroOrMore(cls.equation, ";")),
            cls.END,
            cls.IF,
        )

    @classmethod
    @returns_parsing_expression
    def conditional_equation_a(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            conditional_equation_a :
             `if` expression `then`
             { algorithm ";" }
             { `elseif` expression `then`
             { algorithm ";" }
             }
             [ `else`
             { algorithm ";" }
             ]
             `end` `if`
        """
        return (
            cls.IF,
            cls.expression,
            cls.THEN,
            ZeroOrMore(cls.algorithm, ";"),
            ZeroOrMore(
                cls.ELSEIF,
                cls.expression,
                cls.THEN,
                ZeroOrMore(cls.algorithm, ";"),
            ),
            Optional(cls.ELSE, ZeroOrMore(cls.algorithm, ";")),
            cls.END,
            cls.IF,
        )

    @classmethod
    @returns_parsing_expression
    def for_clause_e(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            for_clause_e :
             `for` for_indices `loop`
             { equation ";" }
             `end` `for`
        """
        return (
            cls.FOR,
            cls.for_indices,
            cls.LOOP,
            ZeroOrMore(cls.equation, ";"),
            cls.END,
            cls.FOR,
        )

    @classmethod
    @returns_parsing_expression
    def for_clause_a(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            for_clause_a :
             `for` for_indices `loop`
             { algorithm ";" }
             `end` `for`
        """
        return (
            cls.FOR,
            cls.for_indices,
            cls.LOOP,
            ZeroOrMore(cls.algorithm, ";"),
            cls.END,
            cls.FOR,
        )

    @classmethod
    @returns_parsing_expression
    def for_indices(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            for_indices :
             for_index {"," for_index}
        """
        return (cls.for_index, ZeroOrMore(",", cls.for_index))

    @classmethod
    @returns_parsing_expression
    def for_index(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            for_index:
             IDENT [ `in` expression ]
        """
        return (cls.IDENT, Optional(cls.IN, cls.expression))

    @classmethod
    @returns_parsing_expression
    def while_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            while_clause :
             `while` expression `loop`
             { algorithm ";" }
             `end` `while`
        """
        return (
            cls.WHILE,
            cls.expression,
            cls.LOOP,
            ZeroOrMore(cls.algorithm, ";"),
            cls.END,
            cls.WHILE,
        )

    @classmethod
    @returns_parsing_expression
    def when_clause_e(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            when_clause_e :
             `when` expression `then`
             { equation ";" }
             { `elsewhen` expression `then`
             { equation ";" } }
             `end` `when`
        """
        return (
            cls.WHEN,
            cls.expression,
            cls.THEN,
            ZeroOrMore(cls.equation, ";"),
            ZeroOrMore(
                cls.ELSEWHEN,
                cls.expression,
                cls.THEN,
                ZeroOrMore(cls.equation, ";"),
            ),
            cls.END,
            cls.WHEN,
        )

    @classmethod
    @returns_parsing_expression
    def when_clause_a(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            when_clause_a :
             `when` expression `then`
             { algorithm ";" }
             { `elsewhen` expression `then`
             { algorithm ";" } }
             `end` `when`
        """
        return (
            cls.WHEN,
            cls.expression,
            cls.THEN,
            ZeroOrMore(cls.algorithm, ";"),
            ZeroOrMore(
                cls.ELSEWHEN,
                cls.expression,
                cls.THEN,
                ZeroOrMore(cls.algorithm, ";"),
            ),
            cls.END,
            cls.WHEN,
        )

    @classmethod
    @returns_parsing_expression
    def connect_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            connect_clause :
             `connect` "(" component_reference "," component_reference ")"
        """
        return (
            cls.CONNECT,
            "(",
            cls.component_reference,
            ",",
            cls.component_reference,
            ")",
        )

    @classmethod
    @returns_parsing_expression
    def expression(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            expression :
             simple_expression
             | `if` expression `then` expression { `elseif` expression `then` expression } `else`
            expression
        """
        return [
            cls.simple_expression,
            (
                cls.IF,
                cls.expression,
                cls.THEN,
                cls.expression,
                ZeroOrMore(
                    cls.ELSEIF, cls.expression, cls.THEN, cls.expression
                ),
                cls.ELSE,
                cls.expression,
            ),
        ]

    @classmethod
    @returns_parsing_expression
    def simple_expression(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            simple_expression :
             logical_expression [ ":" logical_expression [ ":" logical_expression ] ]
        """
        return (
            cls.logical_expression,
            Optional(
                ":",
                cls.logical_expression,
                Optional(":", cls.logical_expression),
            ),
        )

    @classmethod
    @returns_parsing_expression
    def logical_expression(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            logical_expression :
             logical_term { `or` logical_term }
        """
        return (cls.logical_term, ZeroOrMore(cls.OR, cls.logical_term))

    @classmethod
    @returns_parsing_expression
    def logical_term(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            logical_term :
             logical_factor { `and` logical_factor }
        """
        return (cls.logical_factor, ZeroOrMore(cls.AND, cls.logical_factor))

    @classmethod
    @returns_parsing_expression
    def logical_factor(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            logical_factor :
             [ `not` ] relation
        """
        return (Optional(cls.NOT), cls.relation)

    @classmethod
    @returns_parsing_expression
    def relation(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            relation :
             arithmetic_expression [ rel_op arithmetic_expression ]
        """
        return (
            cls.arithmetic_expression,
            Optional(cls.rel_op, cls.arithmetic_expression),
        )

    @classmethod
    @returns_parsing_expression
    def rel_op(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            rel_op :
               /* 2-characters */ "==" | "<>" | "<=" | ">=" |
               /* 1-character  */ "<"  | ">"
        """
        return ["==", "<>", "<=", ">=", "<", ">"]

    @classmethod
    @returns_parsing_expression
    def arithmetic_expression(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            arithmetic_expression :
             [ add_op ] term { add_op term }
        """
        return (
            Optional(cls.add_op),
            cls.term,
            ZeroOrMore(cls.add_op, cls.term),
        )

    @classmethod
    @returns_parsing_expression
    def add_op(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            add_op :
             "+" | "-"
        """
        return ["+", "-"]

    @classmethod
    @returns_parsing_expression
    def term(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            term :
             factor { mul_op factor }
        """
        return (cls.factor, ZeroOrMore(cls.mul_op, cls.factor))

    @classmethod
    @returns_parsing_expression
    def mul_op(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            mul_op :
             "*" | "/"
        """
        return ["*", "/"]

    @classmethod
    @returns_parsing_expression
    def factor(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            factor :
             primary [ "^" primary ]
        """
        return (cls.primary, Optional("^", cls.primary))

    @classmethod
    @returns_parsing_expression
    def primary(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            primary :
             UNSIGNED_NUMBER
             | STRING
             | `false`
             | `true`
             | component_reference [ function_call ]
             | "(" output_expression_list ")"
             | "[" expression_list { ";" expression_list } "]"
             | "{" function_arguments "}"
             | `end`
        """
        return [
            cls.UNSIGNED_NUMBER,
            cls.STRING,
            cls.FALSE,
            cls.TRUE,
            (cls.component_reference, Optional(cls.function_call)),
            ("(", cls.output_expression_list, ")"),
            (
                "[",
                cls.expression_list,
                ZeroOrMore(";", cls.expression_list),
                "]",
            ),
            ("{", cls.function_arguments, "}"),
            cls.END,
        ]

    @classmethod
    @returns_parsing_expression
    def name(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            name :
             IDENT [ "." name ]
        """
        return (cls.IDENT, Optional(".", cls.name))

    @classmethod
    @returns_parsing_expression
    def component_reference(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            component_reference :
             IDENT [ array_subscripts ] [ "." component_reference ]
        """
        return (
            cls.IDENT,
            Optional(cls.array_subscripts),
            Optional(".", cls.component_reference),
        )

    @classmethod
    @returns_parsing_expression
    def function_call(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            function_call :
             "(" [ function_arguments ] ")"
        """
        return ("(", Optional(cls.function_arguments), ")")

    @classmethod
    @returns_parsing_expression
    def function_arguments(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            function_arguments :
             expression [ "," function_arguments | `for` for_indices ]
             | named_arguments
        """
        return [
            (
                cls.expression,
                Optional(
                    [(",", cls.function_arguments), (cls.FOR, cls.for_indices)]
                ),
            ),
            cls.named_arguments,
        ]

    @classmethod
    @returns_parsing_expression
    def named_arguments(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            named_arguments: named_argument [ "," named_arguments ]
        """
        return (cls.named_argument, Optional(",", cls.named_arguments))

    @classmethod
    @returns_parsing_expression
    def named_argument(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            named_argument: IDENT "=" expression
        """
        return (cls.IDENT, "=", cls.expression)

    @classmethod
    @returns_parsing_expression
    def output_expression_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            output_expression_list:
             [ expression ] { "," [ expression ] }
        """
        return (
            Optional(cls.expression),
            ZeroOrMore(",", Optional(cls.expression)),
        )

    @classmethod
    @returns_parsing_expression
    def expression_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            expression_list :
             expression { "," expression }
        """
        return (cls.expression, ZeroOrMore(",", cls.expression))

    @classmethod
    @returns_parsing_expression
    def array_subscripts(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            array_subscripts :
             "[" subscript { "," subscript } "]"
        """
        return ("[", cls.subscript, ZeroOrMore(",", cls.subscript), "]")

    @classmethod
    @returns_parsing_expression
    def subscript(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            subscript :
             ":" | expression
        """
        return [":", cls.expression]

    @classmethod
    @returns_parsing_expression
    def comment(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            comment :
             string_comment [ annotation ]
        """
        return (cls.string_comment, Optional(cls.annotation))

    @classmethod
    @returns_parsing_expression
    def string_comment(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            string_comment :
             [ STRING { "+" STRING } ]
        """
        return Optional(cls.STRING, ZeroOrMore("+", cls.STRING))

    @classmethod
    @returns_parsing_expression
    def annotation(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            annotation :
             annotation class_modification
        """
        return (cls.annotation, cls.class_modification)
