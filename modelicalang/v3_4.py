from modelicalang._backend import *


class Syntax(metaclass=SyntaxMeta):
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
    def ALGORITHM() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ALGORITHM = `algorithm`
        """
        return RegExMatch("algorithm(?![0-9A-Z_a-z])")

    @staticmethod
    def AND() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            AND = `and`
        """
        return RegExMatch("and(?![0-9A-Z_a-z])")

    @staticmethod
    def ANNOTATION() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ANNOTATION = `annotation`
        """
        return RegExMatch("annotation(?![0-9A-Z_a-z])")

    @staticmethod
    def BLOCK() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            BLOCK = `block`
        """
        return RegExMatch("block(?![0-9A-Z_a-z])")

    @staticmethod
    def BREAK() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            BREAK = `break`
        """
        return RegExMatch("break(?![0-9A-Z_a-z])")

    @staticmethod
    def CLASS() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            CLASS = `class`
        """
        return RegExMatch("class(?![0-9A-Z_a-z])")

    @staticmethod
    def CONNECT() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            CONNECT = `connect`
        """
        return RegExMatch("connect(?![0-9A-Z_a-z])")

    @staticmethod
    def CONNECTOR() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            CONNECTOR = `connector`
        """
        return RegExMatch("connector(?![0-9A-Z_a-z])")

    @staticmethod
    def CONSTANT() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            CONSTANT = `constant`
        """
        return RegExMatch("constant(?![0-9A-Z_a-z])")

    @staticmethod
    def CONSTRAINEDBY() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            CONSTRAINEDBY = `constrainedby`
        """
        return RegExMatch("constrainedby(?![0-9A-Z_a-z])")

    @staticmethod
    def DER() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            DER = `der`
        """
        return RegExMatch("der(?![0-9A-Z_a-z])")

    @staticmethod
    def DISCRETE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            DISCRETE = `discrete`
        """
        return RegExMatch("discrete(?![0-9A-Z_a-z])")

    @staticmethod
    def EACH() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            EACH = `each`
        """
        return RegExMatch("each(?![0-9A-Z_a-z])")

    @staticmethod
    def ELSE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ELSE = `else`
        """
        return RegExMatch("else(?![0-9A-Z_a-z])")

    @staticmethod
    def ELSEIF() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ELSEIF = `elseif`
        """
        return RegExMatch("elseif(?![0-9A-Z_a-z])")

    @staticmethod
    def ELSEWHEN() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ELSEWHEN = `elsewhen`
        """
        return RegExMatch("elsewhen(?![0-9A-Z_a-z])")

    @staticmethod
    def ENCAPSULATED() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ENCAPSULATED = `encapsulated`
        """
        return RegExMatch("encapsulated(?![0-9A-Z_a-z])")

    @staticmethod
    def END() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            END = `end`
        """
        return RegExMatch("end(?![0-9A-Z_a-z])")

    @staticmethod
    def ENUMERATION() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ENUMERATION = `enumeration`
        """
        return RegExMatch("enumeration(?![0-9A-Z_a-z])")

    @staticmethod
    def EQUATION() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            EQUATION = `equation`
        """
        return RegExMatch("equation(?![0-9A-Z_a-z])")

    @staticmethod
    def EXPANDABLE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            EXPANDABLE = `expandable`
        """
        return RegExMatch("expandable(?![0-9A-Z_a-z])")

    @staticmethod
    def EXTENDS() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            EXTENDS = `extends`
        """
        return RegExMatch("extends(?![0-9A-Z_a-z])")

    @staticmethod
    def EXTERNAL() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            EXTERNAL = `external`
        """
        return RegExMatch("external(?![0-9A-Z_a-z])")

    @staticmethod
    def FALSE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            FALSE = `false`
        """
        return RegExMatch("false(?![0-9A-Z_a-z])")

    @staticmethod
    def FINAL() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            FINAL = `final`
        """
        return RegExMatch("final(?![0-9A-Z_a-z])")

    @staticmethod
    def FLOW() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            FLOW = `flow`
        """
        return RegExMatch("flow(?![0-9A-Z_a-z])")

    @staticmethod
    def FOR() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            FOR = `for`
        """
        return RegExMatch("for(?![0-9A-Z_a-z])")

    @staticmethod
    def FUNCTION() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            FUNCTION = `function`
        """
        return RegExMatch("function(?![0-9A-Z_a-z])")

    @staticmethod
    def IF() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            IF = `if`
        """
        return RegExMatch("if(?![0-9A-Z_a-z])")

    @staticmethod
    def IMPORT() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            IMPORT = `import`
        """
        return RegExMatch("import(?![0-9A-Z_a-z])")

    @staticmethod
    def IMPURE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            IMPURE = `impure`
        """
        return RegExMatch("impure(?![0-9A-Z_a-z])")

    @staticmethod
    def IN() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            IN = `in`
        """
        return RegExMatch("in(?![0-9A-Z_a-z])")

    @staticmethod
    def INITIAL() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            INITIAL = `initial`
        """
        return RegExMatch("initial(?![0-9A-Z_a-z])")

    @staticmethod
    def INNER() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            INNER = `inner`
        """
        return RegExMatch("inner(?![0-9A-Z_a-z])")

    @staticmethod
    def INPUT() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            INPUT = `input`
        """
        return RegExMatch("input(?![0-9A-Z_a-z])")

    @staticmethod
    def LOOP() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            LOOP = `loop`
        """
        return RegExMatch("loop(?![0-9A-Z_a-z])")

    @staticmethod
    def MODEL() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            MODEL = `model`
        """
        return RegExMatch("model(?![0-9A-Z_a-z])")

    @staticmethod
    def NOT() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            NOT = `not`
        """
        return RegExMatch("not(?![0-9A-Z_a-z])")

    @staticmethod
    def OPERATOR() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            OPERATOR = `operator`
        """
        return RegExMatch("operator(?![0-9A-Z_a-z])")

    @staticmethod
    def OR() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            OR = `or`
        """
        return RegExMatch("or(?![0-9A-Z_a-z])")

    @staticmethod
    def OUTER() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            OUTER = `outer`
        """
        return RegExMatch("outer(?![0-9A-Z_a-z])")

    @staticmethod
    def OUTPUT() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            OUTPUT = `output`
        """
        return RegExMatch("output(?![0-9A-Z_a-z])")

    @staticmethod
    def PACKAGE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            PACKAGE = `package`
        """
        return RegExMatch("package(?![0-9A-Z_a-z])")

    @staticmethod
    def PARAMETER() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            PARAMETER = `parameter`
        """
        return RegExMatch("parameter(?![0-9A-Z_a-z])")

    @staticmethod
    def PARTIAL() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            PARTIAL = `partial`
        """
        return RegExMatch("partial(?![0-9A-Z_a-z])")

    @staticmethod
    def PROTECTED() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            PROTECTED = `protected`
        """
        return RegExMatch("protected(?![0-9A-Z_a-z])")

    @staticmethod
    def PUBLIC() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            PUBLIC = `public`
        """
        return RegExMatch("public(?![0-9A-Z_a-z])")

    @staticmethod
    def PURE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            PURE = `pure`
        """
        return RegExMatch("pure(?![0-9A-Z_a-z])")

    @staticmethod
    def RECORD() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            RECORD = `record`
        """
        return RegExMatch("record(?![0-9A-Z_a-z])")

    @staticmethod
    def REDECLARE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            REDECLARE = `redeclare`
        """
        return RegExMatch("redeclare(?![0-9A-Z_a-z])")

    @staticmethod
    def REPLACEABLE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            REPLACEABLE = `replaceable`
        """
        return RegExMatch("replaceable(?![0-9A-Z_a-z])")

    @staticmethod
    def RETURN() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            RETURN = `return`
        """
        return RegExMatch("return(?![0-9A-Z_a-z])")

    @staticmethod
    def STREAM() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            STREAM = `stream`
        """
        return RegExMatch("stream(?![0-9A-Z_a-z])")

    @staticmethod
    def THEN() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            THEN = `then`
        """
        return RegExMatch("then(?![0-9A-Z_a-z])")

    @staticmethod
    def TRUE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            TRUE = `true`
        """
        return RegExMatch("true(?![0-9A-Z_a-z])")

    @staticmethod
    def TYPE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            TYPE = `type`
        """
        return RegExMatch("type(?![0-9A-Z_a-z])")

    @staticmethod
    def WHEN() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            WHEN = `when`
        """
        return RegExMatch("when(?![0-9A-Z_a-z])")

    @staticmethod
    def WHILE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            WHILE = `while`
        """
        return RegExMatch("while(?![0-9A-Z_a-z])")

    @staticmethod
    def WITHIN() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            WITHIN = `within`
        """
        return RegExMatch("within(?![0-9A-Z_a-z])")

    @classmethod
    @not_start_with_keyword
    def IDENT(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            IDENT = NONDIGIT { DIGIT | NONDIGIT } | Q-IDENT
        """
        return RegExMatch(
            "[A-Z_a-z][0-9A-Z_a-z]*|'([\\ !\\#-\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)([\\ -\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*'"
        )

    @classmethod
    def Q_IDENT(cls) -> RegExMatch:
        '''
        .. code-block:: modelicapeg

            Q-IDENT = "'" ( Q-CHAR | S-ESCAPE ) { Q-CHAR | S-ESCAPE | """ } "'"
        '''
        return RegExMatch(
            "'([\\ !\\#-\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)([\\ -\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*'"
        )

    @classmethod
    def NONDIGIT(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            NONDIGIT = "_" | r'[a-z]' | r'[A-Z]'
        """
        return RegExMatch("[A-Z_a-z]")

    @classmethod
    def STRING(cls) -> RegExMatch:
        '''
        .. code-block:: modelicapeg

            STRING = """ { S-CHAR | S-ESCAPE } """
        '''
        return RegExMatch(
            '"([^"\\\\]|\\\\\'|\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*"'
        )

    @classmethod
    def S_CHAR(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            S-CHAR =
               // S-CHAR is any member of the Unicode character set
               // (http://www.unicode.org; see section 13.2.2 for storing as UTF-8 on files)
               // except double-quote ”””, and backslash ”\\”
               r'[^"\\\\]'
        """
        return RegExMatch('[^"\\\\]')

    @classmethod
    def Q_CHAR(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            Q-CHAR = NONDIGIT | DIGIT | "!" | "#" | "$" | "%" | "&" | "(" | ")" | "*" | "+" | "," |
                     "-" | "." | "/" | ":" | ";" | "<" | ">" | "=" | "?" | "@" | "[" | "]" | "^" |
                    "{" | "}" | "|" | "~" | " "
        """
        return RegExMatch("[\\ !\\#-\\&\\(-\\[\\]-_a-\\~]")

    @classmethod
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
    def DIGIT(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
        """
        return RegExMatch("[0-9]")

    @classmethod
    def UNSIGNED_INTEGER(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            UNSIGNED-INTEGER = DIGIT { DIGIT }
        """
        return RegExMatch("[0-9][0-9]*")

    @classmethod
    def UNSIGNED_NUMBER(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            UNSIGNED-NUMBER = UNSIGNED-INTEGER [ "." [ UNSIGNED-INTEGER ] ]
                    [ ( "e" | "E" ) [ "+" | "-" ] UNSIGNED-INTEGER ]
        """
        return RegExMatch(
            "[0-9][0-9]*(\\.([0-9][0-9]*)?)?([Ee][\\+\\-]?[0-9][0-9]*)?"
        )

    @classmethod
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
    def stored_definition(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            stored-definition:
               [ `within` [ name ] ";" ]
               { [ `final` ] class-definition ";" }
        """
        return (
            Optional(cls.WITHIN, Optional(cls.name), ";"),
            ZeroOrMore(Optional(cls.FINAL), cls.class_definition, ";"),
        )

    @classmethod
    def class_definition(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def class_prefixes(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def class_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            class-specifier :
               long-class-specifier | short-class-specifier | der-class-specifier
        """
        return [
            cls.long_class_specifier,
            cls.short_class_specifier,
            cls.der_class_specifier,
        ]

    @classmethod
    def long_class_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def short_class_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def der_class_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def base_prefix(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            base-prefix :
               [ `input` | `output` ]
        """
        return Optional([cls.INPUT, cls.OUTPUT])

    @classmethod
    def enum_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            enum-list : enumeration-literal { "," enumeration-literal}
        """
        return (
            cls.enumeration_literal,
            ZeroOrMore(",", cls.enumeration_literal),
        )

    @classmethod
    def enumeration_literal(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            enumeration-literal : IDENT comment
        """
        return (cls.IDENT, cls.comment)

    @classmethod
    def composition(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def language_specification(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            language-specification :
               STRING
        """
        return cls.STRING

    @classmethod
    def external_function_call(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def element_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element-list :
               { element ";" }
        """
        return ZeroOrMore(cls.element, ";")

    @classmethod
    def element(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element :
               import-clause |
               extends-clause |
               [ `redeclare` ]
               [ `final` ]
               [ `inner` ] [ `outer` ]
               ( ( class-definition | component-clause) |
               `replaceable` ( class-definition | component-clause)
               [constraining-clause comment])
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
    def import_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def import_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            import-list :
               IDENT { "," IDENT }
        """
        return (cls.IDENT, ZeroOrMore(",", cls.IDENT))

    @classmethod
    def extends_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            extends-clause :
               `extends` type-specifier [ class-modification ] [annotation-comment]
        """
        return (
            cls.EXTENDS,
            cls.type_specifier,
            Optional(cls.class_modification),
            Optional(cls.annotation_comment),
        )

    @classmethod
    def constraining_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            constraining-clause :
               `constrainedby` type-specifier [ class-modification ]
        """
        return (
            cls.CONSTRAINEDBY,
            cls.type_specifier,
            Optional(cls.class_modification),
        )

    @classmethod
    def component_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            component-clause:
               type-prefix type-specifier [ array-subscripts ] component-list
        """
        return (
            cls.type_prefix,
            cls.type_specifier,
            Optional(cls.array_subscripts),
            cls.component_list,
        )

    @classmethod
    def type_prefix(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def component_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            component-list :
               component-declaration { "," component-declaration }
        """
        return (
            cls.component_declaration,
            ZeroOrMore(",", cls.component_declaration),
        )

    @classmethod
    def component_declaration(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            component-declaration :
               declaration [ condition-attribute ] comment
        """
        return (
            cls.declaration,
            Optional(cls.condition_attribute),
            cls.comment,
        )

    @classmethod
    def condition_attribute(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            condition-attribute:
               `if` expression
        """
        return (cls.IF, cls.expression)

    @classmethod
    def declaration(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            declaration :
               IDENT [ array-subscripts ] [ modification ]
        """
        return (
            cls.IDENT,
            Optional(cls.array_subscripts),
            Optional(cls.modification),
        )

    @classmethod
    def modification(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def class_modification(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            class-modification :
               "(" [ argument-list ] ")"
        """
        return ("(", Optional(cls.argument_list), ")")

    @classmethod
    def argument_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            argument-list :
               argument { "," argument }
        """
        return (cls.argument, ZeroOrMore(",", cls.argument))

    @classmethod
    def argument(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            argument :
               element-modification-or-replaceable
               | element-redeclaration
        """
        return [
            cls.element_modification_or_replaceable,
            cls.element_redeclaration,
        ]

    @classmethod
    def element_modification_or_replaceable(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element-modification-or-replaceable:
               [ `each` ] [ `final` ] ( element-modification | element-replaceable)
        """
        return (
            Optional(cls.EACH),
            Optional(cls.FINAL),
            [cls.element_modification, cls.element_replaceable],
        )

    @classmethod
    def element_modification(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element-modification :
               name [ modification ] string-comment
        """
        return (cls.name, Optional(cls.modification), cls.string_comment)

    @classmethod
    def element_redeclaration(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def element_replaceable(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element-replaceable:
               `replaceable` ( short-class-definition | component-clause1)
               [constraining-clause]
        """
        return (
            cls.REPLACEABLE,
            [cls.short_class_definition, cls.component_clause1],
            Optional(cls.constraining_clause),
        )

    @classmethod
    def component_clause1(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            component-clause1 :
               type-prefix type-specifier component-declaration1
        """
        return (
            cls.type_prefix,
            cls.type_specifier,
            cls.component_declaration1,
        )

    @classmethod
    def component_declaration1(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            component-declaration1 :
               declaration comment
        """
        return (cls.declaration, cls.comment)

    @classmethod
    def short_class_definition(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            short-class-definition :
               class-prefixes short-class-specifier
        """
        return (cls.class_prefixes, cls.short_class_specifier)

    @classmethod
    def equation_section(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            equation-section :
               [ `initial` ] `equation` { equation ";" }
        """
        return (
            Optional(cls.INITIAL),
            cls.EQUATION,
            ZeroOrMore(cls.equation, ";"),
        )

    @classmethod
    def algorithm_section(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            algorithm-section :
               [ `initial` ] `algorithm` { statement ";" }
        """
        return (
            Optional(cls.INITIAL),
            cls.ALGORITHM,
            ZeroOrMore(cls.statement, ";"),
        )

    @classmethod
    def equation(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def statement(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def if_equation(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def if_statement(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def for_equation(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def for_statement(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def for_indices(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            for-indices :
               for-index {"," for-index}
        """
        return (cls.for_index, ZeroOrMore(",", cls.for_index))

    @classmethod
    def for_index(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            for-index:
               IDENT [ `in` expression ]
        """
        return (cls.IDENT, Optional(cls.IN, cls.expression))

    @classmethod
    def while_statement(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def when_equation(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def when_statement(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def connect_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def expression(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def simple_expression(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def logical_expression(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            logical-expression :
               logical-term { `or` logical-term }
        """
        return (cls.logical_term, ZeroOrMore(cls.OR, cls.logical_term))

    @classmethod
    def logical_term(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            logical-term :
               logical-factor { `and` logical-factor }
        """
        return (cls.logical_factor, ZeroOrMore(cls.AND, cls.logical_factor))

    @classmethod
    def logical_factor(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            logical-factor :
               [ `not` ] relation
        """
        return (Optional(cls.NOT), cls.relation)

    @classmethod
    def relation(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            relation :
               arithmetic-expression [ relational-operator arithmetic-expression ]
        """
        return (
            cls.arithmetic_expression,
            Optional(cls.relational_operator, cls.arithmetic_expression),
        )

    @classmethod
    def relational_operator(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            relational-operator :
               /* 2-characters */ "==" | "<>" | "<=" | ">=" |
               /* 1-character  */ "<"  | ">"
        """
        return ["==", "<>", "<=", ">=", "<", ">"]

    @classmethod
    def arithmetic_expression(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            arithmetic-expression :
               [ add-operator ] term { add-operator term }
        """
        return (
            Optional(cls.add_operator),
            cls.term,
            ZeroOrMore(cls.add_operator, cls.term),
        )

    @classmethod
    def add_operator(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            add-operator :
               "+" | "-" | ".+" | ".-"
        """
        return ["+", "-", ".+", ".-"]

    @classmethod
    def term(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            term :
               factor { mul-operator factor }
        """
        return (cls.factor, ZeroOrMore(cls.mul_operator, cls.factor))

    @classmethod
    def mul_operator(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            mul-operator :
               "*" | "/" | ".*" | "./"
        """
        return ["*", "/", ".*", "./"]

    @classmethod
    def factor(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            factor :
               primary [ ("^" | ".^") primary ]
        """
        return (cls.primary, Optional(["^", ".^"], cls.primary))

    @classmethod
    def primary(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def type_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            type-specifier : ["."] name
        """
        return (Optional("."), cls.name)

    @classmethod
    def name(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            name : IDENT { "." IDENT }
        """
        return (cls.IDENT, ZeroOrMore(".", cls.IDENT))

    @classmethod
    def component_reference(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def function_call_args(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            function-call-args :
               "(" [ function-arguments ] ")"
        """
        return ("(", Optional(cls.function_arguments), ")")

    @classmethod
    def function_arguments(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def function_arguments_non_first(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def array_arguments(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def array_arguments_non_first(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            array-arguments-non-first :
               expression [ "," array-arguments-non-first ]
        """
        return (cls.expression, Optional(",", cls.array_arguments_non_first))

    @classmethod
    def named_arguments(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            named-arguments: named-argument [ "," named-arguments ]
        """
        return (cls.named_argument, Optional(",", cls.named_arguments))

    @classmethod
    def named_argument(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            named-argument: IDENT "=" function-argument
        """
        return (cls.IDENT, "=", cls.function_argument)

    @classmethod
    def function_argument(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    def output_expression_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            output-expression-list:
               [ expression ] { "," [ expression ] }
        """
        return (
            Optional(cls.expression),
            ZeroOrMore(",", Optional(cls.expression)),
        )

    @classmethod
    def expression_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            expression-list :
               expression { "," expression }
        """
        return (cls.expression, ZeroOrMore(",", cls.expression))

    @classmethod
    def array_subscripts(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            array-subscripts :
               "[" subscript { "," subscript } "]"
        """
        return ("[", cls.subscript, ZeroOrMore(",", cls.subscript), "]")

    @classmethod
    def subscript(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            subscript :
               ":" | expression
        """
        return [":", cls.expression]

    @classmethod
    def comment(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            comment :
               string-comment [ annotation-comment ]
        """
        return (cls.string_comment, Optional(cls.annotation_comment))

    @classmethod
    def string_comment(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            string-comment :
            [ STRING { "+" STRING } ]
        """
        return Optional(cls.STRING, ZeroOrMore("+", cls.STRING))

    @classmethod
    def annotation_comment(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            annotation-comment :
               `annotation` class-modification
        """
        return (cls.ANNOTATION, cls.class_modification)
