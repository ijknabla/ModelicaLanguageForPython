from typing import ClassVar, Tuple

from arpeggio import Optional, RegExMatch, ZeroOrMore

from modelica_language._backend import (
    ParsingExpressionLike,
    not_start_with_keyword,
    returns_parsing_expression,
)


class Syntax:
    _keywords_: ClassVar[Tuple[str, ...]] = (
        "algorithm",
        "and",
        "annotation",
        "block",
        "break",
        "class",
        "connect",
        "connector",
        "constant",
        "constrainedby",
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
        "impure",
        "in",
        "initial",
        "inner",
        "input",
        "loop",
        "model",
        "not",
        "operator",
        "or",
        "outer",
        "output",
        "package",
        "parameter",
        "partial",
        "protected",
        "public",
        "pure",
        "record",
        "redeclare",
        "replaceable",
        "return",
        "stream",
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
        `algorithm`
        """
        return RegExMatch("algorithm(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def AND() -> RegExMatch:
        """
        `and`
        """
        return RegExMatch("and(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def ANNOTATION() -> RegExMatch:
        """
        `annotation`
        """
        return RegExMatch("annotation(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def BLOCK() -> RegExMatch:
        """
        `block`
        """
        return RegExMatch("block(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def BREAK() -> RegExMatch:
        """
        `break`
        """
        return RegExMatch("break(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def CLASS() -> RegExMatch:
        """
        `class`
        """
        return RegExMatch("class(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def CONNECT() -> RegExMatch:
        """
        `connect`
        """
        return RegExMatch("connect(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def CONNECTOR() -> RegExMatch:
        """
        `connector`
        """
        return RegExMatch("connector(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def CONSTANT() -> RegExMatch:
        """
        `constant`
        """
        return RegExMatch("constant(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def CONSTRAINEDBY() -> RegExMatch:
        """
        `constrainedby`
        """
        return RegExMatch("constrainedby(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def DER() -> RegExMatch:
        """
        `der`
        """
        return RegExMatch("der(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def DISCRETE() -> RegExMatch:
        """
        `discrete`
        """
        return RegExMatch("discrete(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def EACH() -> RegExMatch:
        """
        `each`
        """
        return RegExMatch("each(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def ELSE() -> RegExMatch:
        """
        `else`
        """
        return RegExMatch("else(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def ELSEIF() -> RegExMatch:
        """
        `elseif`
        """
        return RegExMatch("elseif(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def ELSEWHEN() -> RegExMatch:
        """
        `elsewhen`
        """
        return RegExMatch("elsewhen(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def ENCAPSULATED() -> RegExMatch:
        """
        `encapsulated`
        """
        return RegExMatch("encapsulated(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def END() -> RegExMatch:
        """
        `end`
        """
        return RegExMatch("end(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def ENUMERATION() -> RegExMatch:
        """
        `enumeration`
        """
        return RegExMatch("enumeration(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def EQUATION() -> RegExMatch:
        """
        `equation`
        """
        return RegExMatch("equation(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def EXPANDABLE() -> RegExMatch:
        """
        `expandable`
        """
        return RegExMatch("expandable(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def EXTENDS() -> RegExMatch:
        """
        `extends`
        """
        return RegExMatch("extends(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def EXTERNAL() -> RegExMatch:
        """
        `external`
        """
        return RegExMatch("external(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def FALSE() -> RegExMatch:
        """
        `false`
        """
        return RegExMatch("false(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def FINAL() -> RegExMatch:
        """
        `final`
        """
        return RegExMatch("final(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def FLOW() -> RegExMatch:
        """
        `flow`
        """
        return RegExMatch("flow(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def FOR() -> RegExMatch:
        """
        `for`
        """
        return RegExMatch("for(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def FUNCTION() -> RegExMatch:
        """
        `function`
        """
        return RegExMatch("function(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def IF() -> RegExMatch:
        """
        `if`
        """
        return RegExMatch("if(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def IMPORT() -> RegExMatch:
        """
        `import`
        """
        return RegExMatch("import(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def IMPURE() -> RegExMatch:
        """
        `impure`
        """
        return RegExMatch("impure(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def IN() -> RegExMatch:
        """
        `in`
        """
        return RegExMatch("in(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def INITIAL() -> RegExMatch:
        """
        `initial`
        """
        return RegExMatch("initial(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def INNER() -> RegExMatch:
        """
        `inner`
        """
        return RegExMatch("inner(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def INPUT() -> RegExMatch:
        """
        `input`
        """
        return RegExMatch("input(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def LOOP() -> RegExMatch:
        """
        `loop`
        """
        return RegExMatch("loop(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def MODEL() -> RegExMatch:
        """
        `model`
        """
        return RegExMatch("model(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def NOT() -> RegExMatch:
        """
        `not`
        """
        return RegExMatch("not(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def OPERATOR() -> RegExMatch:
        """
        `operator`
        """
        return RegExMatch("operator(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def OR() -> RegExMatch:
        """
        `or`
        """
        return RegExMatch("or(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def OUTER() -> RegExMatch:
        """
        `outer`
        """
        return RegExMatch("outer(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def OUTPUT() -> RegExMatch:
        """
        `output`
        """
        return RegExMatch("output(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def PACKAGE() -> RegExMatch:
        """
        `package`
        """
        return RegExMatch("package(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def PARAMETER() -> RegExMatch:
        """
        `parameter`
        """
        return RegExMatch("parameter(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def PARTIAL() -> RegExMatch:
        """
        `partial`
        """
        return RegExMatch("partial(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def PROTECTED() -> RegExMatch:
        """
        `protected`
        """
        return RegExMatch("protected(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def PUBLIC() -> RegExMatch:
        """
        `public`
        """
        return RegExMatch("public(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def PURE() -> RegExMatch:
        """
        `pure`
        """
        return RegExMatch("pure(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def RECORD() -> RegExMatch:
        """
        `record`
        """
        return RegExMatch("record(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def REDECLARE() -> RegExMatch:
        """
        `redeclare`
        """
        return RegExMatch("redeclare(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def REPLACEABLE() -> RegExMatch:
        """
        `replaceable`
        """
        return RegExMatch("replaceable(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def RETURN() -> RegExMatch:
        """
        `return`
        """
        return RegExMatch("return(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def STREAM() -> RegExMatch:
        """
        `stream`
        """
        return RegExMatch("stream(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def THEN() -> RegExMatch:
        """
        `then`
        """
        return RegExMatch("then(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def TRUE() -> RegExMatch:
        """
        `true`
        """
        return RegExMatch("true(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def TYPE() -> RegExMatch:
        """
        `type`
        """
        return RegExMatch("type(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def WHEN() -> RegExMatch:
        """
        `when`
        """
        return RegExMatch("when(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def WHILE() -> RegExMatch:
        """
        `while`
        """
        return RegExMatch("while(?![0-9A-Z_a-z])")

    @staticmethod
    @returns_parsing_expression
    def WITHIN() -> RegExMatch:
        """
        `within`
        """
        return RegExMatch("within(?![0-9A-Z_a-z])")

    @classmethod
    @not_start_with_keyword
    @returns_parsing_expression
    def IDENT(cls) -> RegExMatch:
        """
        IDENT = NONDIGIT { DIGIT | NONDIGIT } | Q-IDENT
        """
        return RegExMatch(
            "[A-Z_a-z][0-9A-Z_a-z]*|'([\\ !\\#-\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)([\\ -\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*'"
        )

    @classmethod
    @returns_parsing_expression
    def Q_IDENT(cls) -> RegExMatch:
        '''
        Q-IDENT = "'" ( Q-CHAR | S-ESCAPE ) { Q-CHAR | S-ESCAPE | """ } "'"
        '''
        return RegExMatch(
            "'([\\ !\\#-\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)([\\ -\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*'"
        )

    @classmethod
    @returns_parsing_expression
    def NONDIGIT(cls) -> RegExMatch:
        """
        NONDIGIT = "_" | r'[a-z]' | r'[A-Z]'
        """
        return RegExMatch("[A-Z_a-z]")

    @classmethod
    @returns_parsing_expression
    def STRING(cls) -> RegExMatch:
        '''
        STRING = """ { S-CHAR | S-ESCAPE } """
        '''
        return RegExMatch(
            '"([^"\\\\]|\\\\\'|\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*"'
        )

    @classmethod
    @returns_parsing_expression
    def S_CHAR(cls) -> RegExMatch:
        """
        S-CHAR = r'[^"\\\\]'
        """
        return RegExMatch('[^"\\\\]')

    @classmethod
    @returns_parsing_expression
    def Q_CHAR(cls) -> RegExMatch:
        """
        Q-CHAR =
          NONDIGIT | DIGIT | "!" | "#" | "$" | "%" | "&" | "(" | ")" | "*" | "+" | "," |
           "-" | "." | "/" | ":" | ";" | "<" | ">" | "=" | "?" | "@" | "[" | "]" | "^" |
           "{" | "}" | "|" | "~" | " "
        """
        return RegExMatch("[\\ !\\#-\\&\\(-\\[\\]-_a-\\~]")

    @classmethod
    @returns_parsing_expression
    def S_ESCAPE(cls) -> RegExMatch:
        """
        S-ESCAPE =
           "\\'" | "\\"" | "\\?" | "\\\\" |
           "\\a" | "\\b" | "\\f" | "\\n" | "\\r" | "\\t" | "\\v"
        """
        return RegExMatch(
            "\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v"
        )

    @classmethod
    @returns_parsing_expression
    def DIGIT(cls) -> RegExMatch:
        """
        DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
        """
        return RegExMatch("[0-9]")

    @classmethod
    @returns_parsing_expression
    def UNSIGNED_INTEGER(cls) -> RegExMatch:
        """
        UNSIGNED-INTEGER = DIGIT { DIGIT }
        """
        return RegExMatch("[0-9][0-9]*")

    @classmethod
    @returns_parsing_expression
    def UNSIGNED_NUMBER(cls) -> RegExMatch:
        """
        UNSIGNED-NUMBER =
           UNSIGNED-INTEGER [ "." [ UNSIGNED-INTEGER ] ]
           [ ( "e" | "E" ) [ "+" | "-" ] UNSIGNED-INTEGER ]
        """
        return RegExMatch(
            "[0-9][0-9]*(\\.([0-9][0-9]*)?)?([Ee][\\+\\-]?[0-9][0-9]*)?"
        )

    @classmethod
    @returns_parsing_expression
    def COMMENT(cls) -> RegExMatch:
        """
        COMMENT =
             r'//.*'                   // single-line comment
           | r'/\\*([^*]|\\*(?!/))*\\*/'
        """
        return RegExMatch("//.*|/\\*([^*]|\\*(?!/))*\\*/")

    @classmethod
    @returns_parsing_expression
    def stored_definition(cls) -> ParsingExpressionLike:
        """
        stored-definition :
           [ `within` [ name ] ";" ]
           { [ `final` ] class-definition ";" }
        """
        return (
            Optional(cls.WITHIN, Optional(cls.name), ";"),
            ZeroOrMore(Optional(cls.FINAL), cls.class_definition, ";"),
        )

    @classmethod
    @returns_parsing_expression
    def class_definition(cls) -> ParsingExpressionLike:
        """
        class-definition :
           [ `encapsulated` ] class-prefixes
           class-specifier
        """
        return (
            Optional(cls.ENCAPSULATED),
            cls.class_prefixes,
            cls.class_specifier,
        )

    @classmethod
    @returns_parsing_expression
    def class_prefixes(cls) -> ParsingExpressionLike:
        """
        class-prefixes :
           [ `partial` ]
           ( `class` | `model` | [ `operator` ] `record` | `block` | [ `expandable` ] `connector` | `type` |
           `package` | [ ( `pure` | `impure` ) ] [ `operator` ] `function` | `operator` )
        """
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
    @returns_parsing_expression
    def class_specifier(cls) -> ParsingExpressionLike:
        """
        class-specifier :
           long-class-specifier | short-class-specifier | der-class-specifier
        """
        return [
            cls.long_class_specifier,
            cls.short_class_specifier,
            cls.der_class_specifier,
        ]

    @classmethod
    @returns_parsing_expression
    def long_class_specifier(cls) -> ParsingExpressionLike:
        """
        long-class-specifier :
           IDENT string-comment composition `end` IDENT
           | `extends` IDENT [ class-modification ] string-comment composition
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
    def short_class_specifier(cls) -> ParsingExpressionLike:
        """
        short-class-specifier :
           IDENT "=" base-prefix type-specifier [ array-subscripts ]
           [ class-modification ] comment
           | IDENT "=" `enumeration` "(" ( [enum-list] | ":" ) ")" comment
        """
        return [
            (
                cls.IDENT,
                "=",
                cls.base_prefix,
                cls.type_specifier,
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
        ]

    @classmethod
    @returns_parsing_expression
    def der_class_specifier(cls) -> ParsingExpressionLike:
        """
        der-class-specifier :
           IDENT "=" `der` "(" type-specifier "," IDENT { "," IDENT } ")" comment
        """
        return (
            cls.IDENT,
            "=",
            cls.DER,
            "(",
            cls.type_specifier,
            ",",
            cls.IDENT,
            ZeroOrMore(",", cls.IDENT),
            ")",
            cls.comment,
        )

    @classmethod
    @returns_parsing_expression
    def base_prefix(cls) -> ParsingExpressionLike:
        """
        base-prefix :
           [ `input` | `output` ]
        """
        return Optional([cls.INPUT, cls.OUTPUT])

    @classmethod
    @returns_parsing_expression
    def enum_list(cls) -> ParsingExpressionLike:
        """
        enum-list : enumeration-literal { "," enumeration-literal}
        """
        return (
            cls.enumeration_literal,
            ZeroOrMore(",", cls.enumeration_literal),
        )

    @classmethod
    @returns_parsing_expression
    def enumeration_literal(cls) -> ParsingExpressionLike:
        """
        enumeration-literal : IDENT comment
        """
        return (cls.IDENT, cls.comment)

    @classmethod
    @returns_parsing_expression
    def composition(cls) -> ParsingExpressionLike:
        """
        composition :
           element-list
           { `public` element-list |
             `protected` element-list |
             equation-section |
             algorithm-section
           }
           [ `external` [ language-specification ]
           [ external-function-call ] [ annotation-comment ] ";" ]
           [ annotation-comment ";" ]
        """
        return (
            cls.element_list,
            ZeroOrMore(
                [
                    (cls.PUBLIC, cls.element_list),
                    (cls.PROTECTED, cls.element_list),
                    cls.equation_section,
                    cls.algorithm_section,
                ]
            ),
            Optional(
                cls.EXTERNAL,
                Optional(cls.language_specification),
                Optional(cls.external_function_call),
                Optional(cls.annotation_comment),
                ";",
            ),
            Optional(cls.annotation_comment, ";"),
        )

    @classmethod
    @returns_parsing_expression
    def language_specification(cls) -> ParsingExpressionLike:
        """
        language-specification :
           STRING
        """
        return cls.STRING

    @classmethod
    @returns_parsing_expression
    def external_function_call(cls) -> ParsingExpressionLike:
        """
        external-function-call :
           [ component-reference "=" ]
           IDENT "(" [ expression-list ] ")"
        """
        return (
            Optional(cls.component_reference, "="),
            cls.IDENT,
            "(",
            Optional(cls.expression_list),
            ")",
        )

    @classmethod
    @returns_parsing_expression
    def element_list(cls) -> ParsingExpressionLike:
        """
        element-list :
           { element ";" }
        """
        return ZeroOrMore(cls.element, ";")

    @classmethod
    @returns_parsing_expression
    def element(cls) -> ParsingExpressionLike:
        """
        element :
           import-clause |
           extends-clause |
           [ `redeclare` ]
           [ `final` ]
           [ `inner` ] [ `outer` ]
           ( ( class-definition | component-clause ) |
           `replaceable` ( class-definition | component-clause )
           [ constraining-clause comment ] )
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
        import-clause :
           `import` ( IDENT "=" name | name ["." ( "*" | "{" import-list "}" ) ] ) comment
        """
        return (
            cls.IMPORT,
            [
                (cls.IDENT, "=", cls.name),
                (cls.name, Optional(".", ["*", ("{", cls.import_list, "}")])),
            ],
            cls.comment,
        )

    @classmethod
    @returns_parsing_expression
    def import_list(cls) -> ParsingExpressionLike:
        """
        import-list :
           IDENT { "," IDENT }
        """
        return (cls.IDENT, ZeroOrMore(",", cls.IDENT))

    @classmethod
    @returns_parsing_expression
    def extends_clause(cls) -> ParsingExpressionLike:
        """
        extends-clause :
           `extends` type-specifier [ class-modification ] [ annotation-comment ]
        """
        return (
            cls.EXTENDS,
            cls.type_specifier,
            Optional(cls.class_modification),
            Optional(cls.annotation_comment),
        )

    @classmethod
    @returns_parsing_expression
    def constraining_clause(cls) -> ParsingExpressionLike:
        """
        constraining-clause :
           `constrainedby` type-specifier [ class-modification ]
        """
        return (
            cls.CONSTRAINEDBY,
            cls.type_specifier,
            Optional(cls.class_modification),
        )

    @classmethod
    @returns_parsing_expression
    def component_clause(cls) -> ParsingExpressionLike:
        """
        component-clause :
           type-prefix type-specifier [ array-subscripts ] component-list
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
        type-prefix :
           [ `flow` | `stream` ]
           [ `discrete` | `parameter` | `constant` ] [ `input` | `output` ]
        """
        return (
            Optional([cls.FLOW, cls.STREAM]),
            Optional([cls.DISCRETE, cls.PARAMETER, cls.CONSTANT]),
            Optional([cls.INPUT, cls.OUTPUT]),
        )

    @classmethod
    @returns_parsing_expression
    def component_list(cls) -> ParsingExpressionLike:
        """
        component-list :
           component-declaration { "," component-declaration }
        """
        return (
            cls.component_declaration,
            ZeroOrMore(",", cls.component_declaration),
        )

    @classmethod
    @returns_parsing_expression
    def component_declaration(cls) -> ParsingExpressionLike:
        """
        component-declaration :
           declaration [ condition-attribute ] comment
        """
        return (
            cls.declaration,
            Optional(cls.condition_attribute),
            cls.comment,
        )

    @classmethod
    @returns_parsing_expression
    def condition_attribute(cls) -> ParsingExpressionLike:
        """
        condition-attribute :
           `if` expression
        """
        return (cls.IF, cls.expression)

    @classmethod
    @returns_parsing_expression
    def declaration(cls) -> ParsingExpressionLike:
        """
        declaration :
           IDENT [ array-subscripts ] [ modification ]
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
        modification :
           class-modification [ "=" expression ]
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
        class-modification :
           "(" [ argument-list ] ")"
        """
        return ("(", Optional(cls.argument_list), ")")

    @classmethod
    @returns_parsing_expression
    def argument_list(cls) -> ParsingExpressionLike:
        """
        argument-list :
           argument { "," argument }
        """
        return (cls.argument, ZeroOrMore(",", cls.argument))

    @classmethod
    @returns_parsing_expression
    def argument(cls) -> ParsingExpressionLike:
        """
        argument :
           element-modification-or-replaceable
           | element-redeclaration
        """
        return [
            cls.element_modification_or_replaceable,
            cls.element_redeclaration,
        ]

    @classmethod
    @returns_parsing_expression
    def element_modification_or_replaceable(cls) -> ParsingExpressionLike:
        """
        element-modification-or-replaceable :
           [ `each` ] [ `final` ] ( element-modification | element-replaceable)
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
        element-modification :
           name [ modification ] string-comment
        """
        return (cls.name, Optional(cls.modification), cls.string_comment)

    @classmethod
    @returns_parsing_expression
    def element_redeclaration(cls) -> ParsingExpressionLike:
        """
        element-redeclaration :
           `redeclare` [ `each` ] [ `final` ]
           ( ( short-class-definition | component-clause1) | element-replaceable )
        """
        return (
            cls.REDECLARE,
            Optional(cls.EACH),
            Optional(cls.FINAL),
            [
                [cls.short_class_definition, cls.component_clause1],
                cls.element_replaceable,
            ],
        )

    @classmethod
    @returns_parsing_expression
    def element_replaceable(cls) -> ParsingExpressionLike:
        """
        element-replaceable :
           `replaceable` ( short-class-definition | component-clause1 )
           [ constraining-clause ]
        """
        return (
            cls.REPLACEABLE,
            [cls.short_class_definition, cls.component_clause1],
            Optional(cls.constraining_clause),
        )

    @classmethod
    @returns_parsing_expression
    def component_clause1(cls) -> ParsingExpressionLike:
        """
        component-clause1 :
           type-prefix type-specifier component-declaration1
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
        component-declaration1 :
           declaration comment
        """
        return (cls.declaration, cls.comment)

    @classmethod
    @returns_parsing_expression
    def short_class_definition(cls) -> ParsingExpressionLike:
        """
        short-class-definition :
           class-prefixes short-class-specifier
        """
        return (cls.class_prefixes, cls.short_class_specifier)

    @classmethod
    @returns_parsing_expression
    def equation_section(cls) -> ParsingExpressionLike:
        """
        equation-section :
           [ `initial` ] `equation` { equation ";" }
        """
        return (
            Optional(cls.INITIAL),
            cls.EQUATION,
            ZeroOrMore(cls.equation, ";"),
        )

    @classmethod
    @returns_parsing_expression
    def algorithm_section(cls) -> ParsingExpressionLike:
        """
        algorithm-section :
           [ `initial` ] `algorithm` { statement ";" }
        """
        return (
            Optional(cls.INITIAL),
            cls.ALGORITHM,
            ZeroOrMore(cls.statement, ";"),
        )

    @classmethod
    @returns_parsing_expression
    def equation(cls) -> ParsingExpressionLike:
        """
        equation :
           ( simple-expression "=" expression
             | if-equation
             | for-equation
             | connect-clause
             | when-equation
             | component-reference function-call-args )
           comment
        """
        return (
            [
                (cls.simple_expression, "=", cls.expression),
                cls.if_equation,
                cls.for_equation,
                cls.connect_clause,
                cls.when_equation,
                (cls.component_reference, cls.function_call_args),
            ],
            cls.comment,
        )

    @classmethod
    @returns_parsing_expression
    def statement(cls) -> ParsingExpressionLike:
        """
        statement :
           ( component-reference ( ":=" expression | function-call-args )
             | "(" output-expression-list ")" ":=" component-reference function-call-args
             | `break`
             | `return`
             | if-statement
             | for-statement
             | while-statement
             | when-statement )
           comment
        """
        return (
            [
                (
                    cls.component_reference,
                    [(":=", cls.expression), cls.function_call_args],
                ),
                (
                    "(",
                    cls.output_expression_list,
                    ")",
                    ":=",
                    cls.component_reference,
                    cls.function_call_args,
                ),
                cls.BREAK,
                cls.RETURN,
                cls.if_statement,
                cls.for_statement,
                cls.while_statement,
                cls.when_statement,
            ],
            cls.comment,
        )

    @classmethod
    @returns_parsing_expression
    def if_equation(cls) -> ParsingExpressionLike:
        """
        if-equation :
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
    def if_statement(cls) -> ParsingExpressionLike:
        """
        if-statement :
           `if` expression `then`
             { statement ";" }
           { `elseif` expression `then`
             { statement ";" }
           }
           [ `else`
             { statement ";" }
           ]
           `end` `if`
        """
        return (
            cls.IF,
            cls.expression,
            cls.THEN,
            ZeroOrMore(cls.statement, ";"),
            ZeroOrMore(
                cls.ELSEIF,
                cls.expression,
                cls.THEN,
                ZeroOrMore(cls.statement, ";"),
            ),
            Optional(cls.ELSE, ZeroOrMore(cls.statement, ";")),
            cls.END,
            cls.IF,
        )

    @classmethod
    @returns_parsing_expression
    def for_equation(cls) -> ParsingExpressionLike:
        """
        for-equation :
           `for` for-indices `loop`
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
    def for_statement(cls) -> ParsingExpressionLike:
        """
        for-statement :
           `for` for-indices `loop`
             { statement ";" }
           `end` `for`
        """
        return (
            cls.FOR,
            cls.for_indices,
            cls.LOOP,
            ZeroOrMore(cls.statement, ";"),
            cls.END,
            cls.FOR,
        )

    @classmethod
    @returns_parsing_expression
    def for_indices(cls) -> ParsingExpressionLike:
        """
        for-indices :
           for-index {"," for-index}
        """
        return (cls.for_index, ZeroOrMore(",", cls.for_index))

    @classmethod
    @returns_parsing_expression
    def for_index(cls) -> ParsingExpressionLike:
        """
        for-index :
           IDENT [ `in` expression ]
        """
        return (cls.IDENT, Optional(cls.IN, cls.expression))

    @classmethod
    @returns_parsing_expression
    def while_statement(cls) -> ParsingExpressionLike:
        """
        while-statement :
           `while` expression `loop`
           { statement ";" }
           `end` `while`
        """
        return (
            cls.WHILE,
            cls.expression,
            cls.LOOP,
            ZeroOrMore(cls.statement, ";"),
            cls.END,
            cls.WHILE,
        )

    @classmethod
    @returns_parsing_expression
    def when_equation(cls) -> ParsingExpressionLike:
        """
        when-equation :
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
    def when_statement(cls) -> ParsingExpressionLike:
        """
        when-statement :
           `when` expression `then`
             { statement ";" }
           { `elsewhen` expression `then`
             { statement ";" } }
           `end` `when`
        """
        return (
            cls.WHEN,
            cls.expression,
            cls.THEN,
            ZeroOrMore(cls.statement, ";"),
            ZeroOrMore(
                cls.ELSEWHEN,
                cls.expression,
                cls.THEN,
                ZeroOrMore(cls.statement, ";"),
            ),
            cls.END,
            cls.WHEN,
        )

    @classmethod
    @returns_parsing_expression
    def connect_clause(cls) -> ParsingExpressionLike:
        """
        connect-clause :
           `connect` "(" component-reference "," component-reference ")"
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
        expression :
           simple-expression
           | `if` expression `then` expression { `elseif` expression `then` expression }
           `else` expression
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
        simple-expression :
           logical-expression [ ":" logical-expression [ ":" logical-expression ] ]
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
        logical-expression :
           logical-term { `or` logical-term }
        """
        return (cls.logical_term, ZeroOrMore(cls.OR, cls.logical_term))

    @classmethod
    @returns_parsing_expression
    def logical_term(cls) -> ParsingExpressionLike:
        """
        logical-term :
           logical-factor { `and` logical-factor }
        """
        return (cls.logical_factor, ZeroOrMore(cls.AND, cls.logical_factor))

    @classmethod
    @returns_parsing_expression
    def logical_factor(cls) -> ParsingExpressionLike:
        """
        logical-factor :
           [ `not` ] relation
        """
        return (Optional(cls.NOT), cls.relation)

    @classmethod
    @returns_parsing_expression
    def relation(cls) -> ParsingExpressionLike:
        """
        relation :
           arithmetic-expression [ relational-operator arithmetic-expression ]
        """
        return (
            cls.arithmetic_expression,
            Optional(cls.relational_operator, cls.arithmetic_expression),
        )

    @classmethod
    @returns_parsing_expression
    def relational_operator(cls) -> ParsingExpressionLike:
        """
        relational-operator :
           "==" | "<>" | "<=" | ">=" |  // 2-letter operators
           "<" | ">"
        """
        return ["==", "<>", "<=", ">=", "<", ">"]

    @classmethod
    @returns_parsing_expression
    def arithmetic_expression(cls) -> ParsingExpressionLike:
        """
        arithmetic-expression :
           [ add-operator ] term { add-operator term }
        """
        return (
            Optional(cls.add_operator),
            cls.term,
            ZeroOrMore(cls.add_operator, cls.term),
        )

    @classmethod
    @returns_parsing_expression
    def add_operator(cls) -> ParsingExpressionLike:
        """
        add-operator :
           "+" | "-" | ".+" | ".-"
        """
        return ["+", "-", ".+", ".-"]

    @classmethod
    @returns_parsing_expression
    def term(cls) -> ParsingExpressionLike:
        """
        term :
           factor { mul-operator factor }
        """
        return (cls.factor, ZeroOrMore(cls.mul_operator, cls.factor))

    @classmethod
    @returns_parsing_expression
    def mul_operator(cls) -> ParsingExpressionLike:
        """
        mul-operator :
           "*" | "/" | ".*" | "./"
        """
        return ["*", "/", ".*", "./"]

    @classmethod
    @returns_parsing_expression
    def factor(cls) -> ParsingExpressionLike:
        """
        factor :
           primary [ ("^" | ".^") primary ]
        """
        return (cls.primary, Optional(["^", ".^"], cls.primary))

    @classmethod
    @returns_parsing_expression
    def primary(cls) -> ParsingExpressionLike:
        """
        primary :
           UNSIGNED-NUMBER
           | STRING
           | `false`
           | `true`
           | (component-reference | `der` | `initial` | `pure` ) function-call-args
           | component-reference
           | "(" output-expression-list ")"
           | "[" expression-list { ";" expression-list } "]"
           | "{" array-arguments "}"
           | `end`
        """
        return [
            cls.UNSIGNED_NUMBER,
            cls.STRING,
            cls.FALSE,
            cls.TRUE,
            (
                [cls.component_reference, cls.DER, cls.INITIAL, cls.PURE],
                cls.function_call_args,
            ),
            cls.component_reference,
            ("(", cls.output_expression_list, ")"),
            (
                "[",
                cls.expression_list,
                ZeroOrMore(";", cls.expression_list),
                "]",
            ),
            ("{", cls.array_arguments, "}"),
            cls.END,
        ]

    @classmethod
    @returns_parsing_expression
    def type_specifier(cls) -> ParsingExpressionLike:
        """
        type-specifier : ["."] name
        """
        return (Optional("."), cls.name)

    @classmethod
    @returns_parsing_expression
    def name(cls) -> ParsingExpressionLike:
        """
        name : IDENT { "." IDENT }
        """
        return (cls.IDENT, ZeroOrMore(".", cls.IDENT))

    @classmethod
    @returns_parsing_expression
    def component_reference(cls) -> ParsingExpressionLike:
        """
        component-reference :
           [ "." ] IDENT [ array-subscripts ] { "." IDENT [ array-subscripts ] }
        """
        return (
            Optional("."),
            cls.IDENT,
            Optional(cls.array_subscripts),
            ZeroOrMore(".", cls.IDENT, Optional(cls.array_subscripts)),
        )

    @classmethod
    @returns_parsing_expression
    def function_call_args(cls) -> ParsingExpressionLike:
        """
        function-call-args :
           "(" [ function-arguments ] ")"
        """
        return ("(", Optional(cls.function_arguments), ")")

    @classmethod
    @returns_parsing_expression
    def function_arguments(cls) -> ParsingExpressionLike:
        """
        function-arguments :
           `function` type-specifier "(" [ named-arguments ] ")" [ "," function-arguments-non-first ]
           | named-arguments
           | expression [ "," function-arguments-non-first | `for` for-indices ]
        """
        return [
            (
                cls.FUNCTION,
                cls.type_specifier,
                "(",
                Optional(cls.named_arguments),
                ")",
                Optional(",", cls.function_arguments_non_first),
            ),
            cls.named_arguments,
            (
                cls.expression,
                Optional(
                    [
                        (",", cls.function_arguments_non_first),
                        (cls.FOR, cls.for_indices),
                    ]
                ),
            ),
        ]

    @classmethod
    @returns_parsing_expression
    def function_arguments_non_first(cls) -> ParsingExpressionLike:
        """
        function-arguments-non-first :
           named-arguments
           | function-argument [ "," function-arguments-non-first ]
        """
        return [
            cls.named_arguments,
            (
                cls.function_argument,
                Optional(",", cls.function_arguments_non_first),
            ),
        ]

    @classmethod
    @returns_parsing_expression
    def array_arguments(cls) -> ParsingExpressionLike:
        """
        array-arguments :
           expression [ "," array-arguments-non-first | `for` for-indices ]
        """
        return (
            cls.expression,
            Optional(
                [
                    (",", cls.array_arguments_non_first),
                    (cls.FOR, cls.for_indices),
                ]
            ),
        )

    @classmethod
    @returns_parsing_expression
    def array_arguments_non_first(cls) -> ParsingExpressionLike:
        """
        array-arguments-non-first :
           expression [ "," array-arguments-non-first ]
        """
        return (cls.expression, Optional(",", cls.array_arguments_non_first))

    @classmethod
    @returns_parsing_expression
    def named_arguments(cls) -> ParsingExpressionLike:
        """
        named-arguments : named-argument [ "," named-arguments ]
        """
        return (cls.named_argument, Optional(",", cls.named_arguments))

    @classmethod
    @returns_parsing_expression
    def named_argument(cls) -> ParsingExpressionLike:
        """
        named-argument : IDENT "=" function-argument
        """
        return (cls.IDENT, "=", cls.function_argument)

    @classmethod
    @returns_parsing_expression
    def function_argument(cls) -> ParsingExpressionLike:
        """
        function-argument :
           `function` type-specifier "(" [ named-arguments ] ")" | expression
        """
        return [
            (
                cls.FUNCTION,
                cls.type_specifier,
                "(",
                Optional(cls.named_arguments),
                ")",
            ),
            cls.expression,
        ]

    @classmethod
    @returns_parsing_expression
    def output_expression_list(cls) -> ParsingExpressionLike:
        """
        output-expression-list :
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
        expression-list :
           expression { "," expression }
        """
        return (cls.expression, ZeroOrMore(",", cls.expression))

    @classmethod
    @returns_parsing_expression
    def array_subscripts(cls) -> ParsingExpressionLike:
        """
        array-subscripts :
           "[" subscript { "," subscript } "]"
        """
        return ("[", cls.subscript, ZeroOrMore(",", cls.subscript), "]")

    @classmethod
    @returns_parsing_expression
    def subscript(cls) -> ParsingExpressionLike:
        """
        subscript :
           ":" | expression
        """
        return [":", cls.expression]

    @classmethod
    @returns_parsing_expression
    def comment(cls) -> ParsingExpressionLike:
        """
        comment :
           string-comment [ annotation-comment ]
        """
        return (cls.string_comment, Optional(cls.annotation_comment))

    @classmethod
    @returns_parsing_expression
    def string_comment(cls) -> ParsingExpressionLike:
        """
        string-comment :
           [ STRING { "+" STRING } ]
        """
        return Optional(cls.STRING, ZeroOrMore("+", cls.STRING))

    @classmethod
    @returns_parsing_expression
    def annotation_comment(cls) -> ParsingExpressionLike:
        """
        annotation-comment :
           `annotation` class-modification
        """
        return (cls.ANNOTATION, cls.class_modification)
