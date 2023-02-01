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
    def ANNOTATION() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            ANNOTATION = `annotation`
        """
        return RegExMatch("annotation(?![0-9A-Z_a-z])")

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
    def CONSTRAINEDBY() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            CONSTRAINEDBY = `constrainedby`
        """
        return RegExMatch("constrainedby(?![0-9A-Z_a-z])")

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
    def IMPURE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            IMPURE = `impure`
        """
        return RegExMatch("impure(?![0-9A-Z_a-z])")

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
    def OPERATOR() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            OPERATOR = `operator`
        """
        return RegExMatch("operator(?![0-9A-Z_a-z])")

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
    def PURE() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            PURE = `pure`
        """
        return RegExMatch("pure(?![0-9A-Z_a-z])")

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
    def STREAM() -> RegExMatch:
        """
        .. code-block:: modelicapeg

            STREAM = `stream`
        """
        return RegExMatch("stream(?![0-9A-Z_a-z])")

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
            "[A-Z_a-z][0-9A-Z_a-z]*|'([\\ -\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*'"
        )

    @classmethod
    @returns_parsing_expression
    def Q_IDENT(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            Q-IDENT = "'" { Q-CHAR | S-ESCAPE } "'"
        """
        return RegExMatch(
            "'([\\ -\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*'"
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
        """
        .. code-block:: modelicapeg

            S-CHAR =
               // S-CHAR is any member of the Unicode character set
               // (http://www.unicode.org; see section 13.4 for storing as UTF-8 on files)
               // except double-quote ‘”’, and backslash ‘\\’.
               r'[^"\\\\]'
        """
        return RegExMatch('[^"\\\\]')

    @classmethod
    @returns_parsing_expression
    def Q_CHAR(cls) -> RegExMatch:
        '''
        .. code-block:: modelicapeg

            Q-CHAR = NONDIGIT | DIGIT | "!" | "#" | "$" | "%" | "&" | "(" | ")"
               | "*" | "+" | "," | "-" | "." | "/" | ":" | ";" | "<" | ">" | "="
               | "?" | "@" | "[" | "]" | "^" | "{" | "}" | "|" | "~" | " " | """
        '''
        return RegExMatch("[\\ -\\&\\(-\\[\\]-_a-\\~]")

    @classmethod
    @returns_parsing_expression
    def S_ESCAPE(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            S-ESCAPE = "\\'" | "\\"" | "\\?" | "\\\\"
               | "\\a" | "\\b" | "\\f" | "\\n" | "\\r" | "\\t" | "\\v"
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

            UNSIGNED-INTEGER = DIGIT { DIGIT }
        """
        return RegExMatch("[0-9][0-9]*")

    @classmethod
    @returns_parsing_expression
    def UNSIGNED_REAL(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            UNSIGNED-REAL =
               UNSIGNED_INTEGER [ "." [ UNSIGNED_INTEGER ] ]
               ( "e" | "E" ) [ "+" | "-" ] UNSIGNED-INTEGER
               | UNSIGNED-INTEGER  "." [ UNSIGNED-INTEGER ]
               | "."  UNSIGNED-INTEGER [ ( "e" | "E" ) [ "+" | "-" ] UNSIGNED-INTEGER ]
        """
        return RegExMatch(
            "[0-9][0-9]*(\\.([0-9][0-9]*)?)?[Ee][\\+\\-]?[0-9][0-9]*|[0-9][0-9]*\\.([0-9][0-9]*)?|\\.[0-9][0-9]*([Ee][\\+\\-]?[0-9][0-9]*)?"
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
        .. code-block:: modelicapeg

            class-definition :
               [ `encapsulated` ] class-prefixes class-specifier
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
        .. code-block:: modelicapeg

            class-prefixes :
               [ `partial` ]
               ( `class`
                 | `model`
                 | [ `operator` ] `record`
                 | `block`
                 | [ `expandable` ] `connector`
                 | `type`
                 | `package`
                 | [ `pure` | `impure` ] [ `operator` ] `function`
                 | `operator`
               )
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
    @returns_parsing_expression
    def long_class_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            long-class-specifier :
               IDENT description-string composition `end` IDENT
               | `extends` IDENT [ class-modification ] description-string composition
                 `end` IDENT
        """
        return [
            (
                cls.IDENT,
                cls.description_string,
                cls.composition,
                cls.END,
                cls.IDENT,
            ),
            (
                cls.EXTENDS,
                cls.IDENT,
                Optional(cls.class_modification),
                cls.description_string,
                cls.composition,
                cls.END,
                cls.IDENT,
            ),
        ]

    @classmethod
    @returns_parsing_expression
    def short_class_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            short-class-specifier :
               IDENT "=" base-prefix type-specifier [ array-subscripts ]
               [ class-modification ] description
               | IDENT "=" `enumeration` "(" ( [ enum-list ] | ":" ) ")" description
        """
        return [
            (
                cls.IDENT,
                "=",
                cls.base_prefix,
                cls.type_specifier,
                Optional(cls.array_subscripts),
                Optional(cls.class_modification),
                cls.description,
            ),
            (
                cls.IDENT,
                "=",
                cls.ENUMERATION,
                "(",
                [Optional(cls.enum_list), ":"],
                ")",
                cls.description,
            ),
        ]

    @classmethod
    @returns_parsing_expression
    def der_class_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            der-class-specifier :
               IDENT "=" `der` "(" type-specifier "," IDENT { "," IDENT } ")" description
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
            cls.description,
        )

    @classmethod
    @returns_parsing_expression
    def base_prefix(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            base-prefix :
               [ `input` | `output` ]
        """
        return Optional([cls.INPUT, cls.OUTPUT])

    @classmethod
    @returns_parsing_expression
    def enum_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            enum-list :
               enumeration-literal { "," enumeration-literal }
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

            enumeration-literal :
               IDENT description
        """
        return (cls.IDENT, cls.description)

    @classmethod
    @returns_parsing_expression
    def composition(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            composition :
               element-list
               { `public` element-list
                 | `protected` element-list
                 | equation-section
                 | algorithm-section
               }
               [ `external` [ language-specification ]
               [ external-function-call ] [ annotation-clause ] ";" ]
               [ annotation-clause ";" ]
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
                Optional(cls.annotation_clause),
                ";",
            ),
            Optional(cls.annotation_clause, ";"),
        )

    @classmethod
    @returns_parsing_expression
    def language_specification(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            language-specification :
               STRING
        """
        return cls.STRING

    @classmethod
    @returns_parsing_expression
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
    @returns_parsing_expression
    def element_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element-list :
               { element ";" }
        """
        return ZeroOrMore(cls.element, ";")

    @classmethod
    @returns_parsing_expression
    def element(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element :
               import-clause
               | extends-clause
               | [ `redeclare` ]
                 [ `final` ]
                 [ `inner` ] [ `outer` ]
                 ( class-definition
                   | component-clause
                   | `replaceable` ( class-definition | component-clause )
                     [ constraining-clause description ]
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
                    cls.class_definition,
                    cls.component_clause,
                    (
                        cls.REPLACEABLE,
                        [cls.class_definition, cls.component_clause],
                        Optional(cls.constraining_clause, cls.description),
                    ),
                ],
            ),
        ]

    @classmethod
    @returns_parsing_expression
    def import_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            import-clause :
               `import`
               ( IDENT "=" name
                 | name [ ".*" | "." ( "*" | "{" import-list "}" ) ]
               )
               description
        """
        return (
            cls.IMPORT,
            [
                (cls.IDENT, "=", cls.name),
                (
                    cls.name,
                    Optional(
                        [".*", (".", ["*", ("{", cls.import_list, "}")])]
                    ),
                ),
            ],
            cls.description,
        )

    @classmethod
    @returns_parsing_expression
    def import_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            import-list :
               IDENT { "," IDENT }
        """
        return (cls.IDENT, ZeroOrMore(",", cls.IDENT))

    @classmethod
    @returns_parsing_expression
    def extends_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            extends-clause :
               `extends` type-specifier [ class-modification ] [ annotation-clause ]
        """
        return (
            cls.EXTENDS,
            cls.type_specifier,
            Optional(cls.class_modification),
            Optional(cls.annotation_clause),
        )

    @classmethod
    @returns_parsing_expression
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
    @returns_parsing_expression
    def component_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
        .. code-block:: modelicapeg

            type-prefix :
               [ `flow` | `stream` ]
               [ `discrete` | `parameter` | `constant` ]
               [ `input` | `output` ]
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
        .. code-block:: modelicapeg

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
        .. code-block:: modelicapeg

            component-declaration :
               declaration [ condition-attribute ] description
        """
        return (
            cls.declaration,
            Optional(cls.condition_attribute),
            cls.description,
        )

    @classmethod
    @returns_parsing_expression
    def condition_attribute(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            condition-attribute :
               `if` expression
        """
        return (cls.IF, cls.expression)

    @classmethod
    @returns_parsing_expression
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
    @returns_parsing_expression
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
    @returns_parsing_expression
    def class_modification(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            class-modification :
               "(" [ argument-list ] ")"
        """
        return ("(", Optional(cls.argument_list), ")")

    @classmethod
    @returns_parsing_expression
    def argument_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            argument-list :
               argument { "," argument }
        """
        return (cls.argument, ZeroOrMore(",", cls.argument))

    @classmethod
    @returns_parsing_expression
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
    @returns_parsing_expression
    def element_modification_or_replaceable(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element-modification-or-replaceable :
               [ `each` ] [ `final` ] ( element-modification | element-replaceable )
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

            element-modification :
               name [ modification ] description-string
        """
        return (cls.name, Optional(cls.modification), cls.description_string)

    @classmethod
    @returns_parsing_expression
    def element_redeclaration(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            element-redeclaration :
               `redeclare` [ `each` ] [ `final` ]
               ( short-class-definition | component-clause1 | element-replaceable )
        """
        return (
            cls.REDECLARE,
            Optional(cls.EACH),
            Optional(cls.FINAL),
            [
                cls.short_class_definition,
                cls.component_clause1,
                cls.element_replaceable,
            ],
        )

    @classmethod
    @returns_parsing_expression
    def element_replaceable(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
    @returns_parsing_expression
    def component_declaration1(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            component-declaration1 :
               declaration description
        """
        return (cls.declaration, cls.description)

    @classmethod
    @returns_parsing_expression
    def short_class_definition(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            short-class-definition :
               class-prefixes short-class-specifier
        """
        return (cls.class_prefixes, cls.short_class_specifier)

    @classmethod
    @returns_parsing_expression
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
    @returns_parsing_expression
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
    @returns_parsing_expression
    def equation(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            equation :
               ( simple-expression "=" expression
                 | if-equation
                 | for-equation
                 | connect-clause
                 | when-equation
                 | component-reference function-call-args
               )
               description
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
            cls.description,
        )

    @classmethod
    @returns_parsing_expression
    def statement(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            statement :
               ( component-reference ( ":=" expression | function-call-args )
                 | "(" output-expression-list ")" ":="
                   component-reference function-call-args
                 | `break`
                 | `return`
                 | if-statement
                 | for-statement
                 | while-statement
                 | when-statement
               )
               description
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
            cls.description,
        )

    @classmethod
    @returns_parsing_expression
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
    @returns_parsing_expression
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
    @returns_parsing_expression
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
    @returns_parsing_expression
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
    @returns_parsing_expression
    def for_indices(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            for-indices :
               for-index { "," for-index }
        """
        return (cls.for_index, ZeroOrMore(",", cls.for_index))

    @classmethod
    @returns_parsing_expression
    def for_index(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            for-index :
               IDENT [ `in` expression ]
        """
        return (cls.IDENT, Optional(cls.IN, cls.expression))

    @classmethod
    @returns_parsing_expression
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
    @returns_parsing_expression
    def when_equation(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            when-equation :
               `when` expression `then`
                 { equation ";" }
               { `elsewhen` expression `then`
                 { equation ";" }
               }
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
        .. code-block:: modelicapeg

            when-statement :
               `when` expression `then`
                 { statement ";" }
               { `elsewhen` expression `then`
                 { statement ";" }
               }
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
    @returns_parsing_expression
    def expression(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            expression :
               simple-expression
               | `if` expression `then` expression
                 { `elseif` expression `then` expression }
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
    @returns_parsing_expression
    def logical_expression(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            logical-expression :
               logical-term { `or` logical-term }
        """
        return (cls.logical_term, ZeroOrMore(cls.OR, cls.logical_term))

    @classmethod
    @returns_parsing_expression
    def logical_term(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            logical-term :
               logical-factor { `and` logical-factor }
        """
        return (cls.logical_factor, ZeroOrMore(cls.AND, cls.logical_factor))

    @classmethod
    @returns_parsing_expression
    def logical_factor(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            logical-factor :
               [ `not` ] relation
        """
        return (Optional(cls.NOT), cls.relation)

    @classmethod
    @returns_parsing_expression
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
    @returns_parsing_expression
    def relational_operator(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            relational-operator :
               /* 2-characters */ "==" | "<>" | "<=" | ">=" |
               /* 1-character  */ "<"  | ">"
        """
        return ["==", "<>", "<=", ">=", "<", ">"]

    @classmethod
    @returns_parsing_expression
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
    @returns_parsing_expression
    def add_operator(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            add-operator :
               "+" | "-" | ".+" | ".-"
        """
        return ["+", "-", ".+", ".-"]

    @classmethod
    @returns_parsing_expression
    def term(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            term :
               factor { mul-operator factor }
        """
        return (cls.factor, ZeroOrMore(cls.mul_operator, cls.factor))

    @classmethod
    @returns_parsing_expression
    def mul_operator(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            mul-operator :
               "*" | "/" | ".*" | "./"
        """
        return ["*", "/", ".*", "./"]

    @classmethod
    @returns_parsing_expression
    def factor(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            factor :
               primary [ ("^" | ".^") primary ]
        """
        return (cls.primary, Optional(["^", ".^"], cls.primary))

    @classmethod
    @returns_parsing_expression
    def primary(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            primary :
               UNSIGNED-NUMBER
               | STRING
               | `false`
               | `true`
               | ( component-reference | `der` | `initial` | `pure` ) function-call-args
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
    def UNSIGNED_NUMBER(cls) -> RegExMatch:
        """
        .. code-block:: modelicapeg

            UNSIGNED-NUMBER =
               UNSIGNED-REAL | UNSIGNED-INTEGER
        """
        return RegExMatch(
            "[0-9][0-9]*(\\.([0-9][0-9]*)?)?[Ee][\\+\\-]?[0-9][0-9]*|[0-9][0-9]*\\.([0-9][0-9]*)?|\\.[0-9][0-9]*([Ee][\\+\\-]?[0-9][0-9]*)?|[0-9][0-9]*"
        )

    @classmethod
    @returns_parsing_expression
    def type_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            type-specifier :
               ["."] name
        """
        return (Optional("."), cls.name)

    @classmethod
    @returns_parsing_expression
    def name(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            name :
               IDENT { "." IDENT }
        """
        return (cls.IDENT, ZeroOrMore(".", cls.IDENT))

    @classmethod
    @returns_parsing_expression
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
    @returns_parsing_expression
    def function_call_args(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            function-call-args :
               "(" [ function-arguments ] ")"
        """
        return ("(", Optional(cls.function_arguments), ")")

    @classmethod
    @returns_parsing_expression
    def function_arguments(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            function-arguments :
               function-partial-application [ "," function-arguments-non-first ]
               | named-arguments
               | expression [ "," function-arguments-non-first | `for` for-indices ]
        """
        return [
            (
                cls.function_partial_application,
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
    @returns_parsing_expression
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
    @returns_parsing_expression
    def array_arguments_non_first(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            array-arguments-non-first :
               expression [ "," array-arguments-non-first ]
        """
        return (cls.expression, Optional(",", cls.array_arguments_non_first))

    @classmethod
    @returns_parsing_expression
    def named_arguments(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            named-arguments: named-argument [ "," named-arguments ]
        """
        return (cls.named_argument, Optional(",", cls.named_arguments))

    @classmethod
    @returns_parsing_expression
    def named_argument(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            named-argument: IDENT "=" function-argument
        """
        return (cls.IDENT, "=", cls.function_argument)

    @classmethod
    @returns_parsing_expression
    def function_argument(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            function-argument :
               function-partial-application | expression
        """
        return [cls.function_partial_application, cls.expression]

    @classmethod
    @returns_parsing_expression
    def function_partial_application(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            function-partial-application :
               `function` type-specifier "(" [ named-arguments ] ")"
        """
        return (
            cls.FUNCTION,
            cls.type_specifier,
            "(",
            Optional(cls.named_arguments),
            ")",
        )

    @classmethod
    @returns_parsing_expression
    def output_expression_list(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

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
        .. code-block:: modelicapeg

            expression-list :
               expression { "," expression }
        """
        return (cls.expression, ZeroOrMore(",", cls.expression))

    @classmethod
    @returns_parsing_expression
    def array_subscripts(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            array-subscripts :
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
    def description(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            description :
               description-string [ annotation-clause ]
        """
        return (cls.description_string, Optional(cls.annotation_clause))

    @classmethod
    @returns_parsing_expression
    def description_string(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            description-string :
               [ STRING { "+" STRING } ]
        """
        return Optional(cls.STRING, ZeroOrMore("+", cls.STRING))

    @classmethod
    @returns_parsing_expression
    def annotation_clause(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            annotation-clause :
               `annotation` class-modification
        """
        return (cls.ANNOTATION, cls.class_modification)
