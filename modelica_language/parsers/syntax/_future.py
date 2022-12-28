from arpeggio import Not, Optional, RegExMatch, ZeroOrMore

from .. import regex

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
            Optional(cls.WITHIN, Optional(cls.name), ";"),
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
                Optional(cls.class_modification),
                cls.string_comment,
                cls.composition,
                cls.END,
                cls.IDENT,
            ),
            (
                cls.IDENT,
                cls.string_comment,
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
                cls.comment,
            ),
            (
                cls.IDENT,
                "=",
                cls.base_prefix,
                cls.type_specifier,
                Optional(cls.array_subscripts),
                Optional(cls.class_modification),
                cls.comment,
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
            cls.type_specifier,
            ",",
            cls.IDENT,
            ZeroOrMore(",", cls.IDENT),
            ")",
            cls.comment,
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
        return cls.IDENT, cls.comment

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
                    cls.equation_section,
                    cls.algorithm_section,
                ]
            ),
            Optional(
                cls.EXTERNAL,
                Optional(cls.language_specification),
                Optional(cls.external_function_call),
                Optional(cls.annotation),
                ";",
            ),
            Optional(cls.annotation, ";"),
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
            Optional(cls.component_reference, "="),
            cls.IDENT,
            "(",
            Optional(cls.expression_list),
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
                        [cls.class_definition, cls.component_clause],
                        Optional(cls.constraining_clause, cls.comment),
                    ),
                    [cls.class_definition, cls.component_clause],
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
                (cls.IDENT, "=", cls.name),
                (
                    cls.name,
                    Optional(
                        ".",
                        [
                            "*",
                            ("{", cls.import_list, "}"),  # type: ignore
                        ],
                    ),
                ),
            ],
            cls.comment,
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
            cls.type_specifier,
            Optional(cls.class_modification),
            Optional(cls.annotation),
        )

    @classmethod
    def constraining_clause(cls):  # type: ignore
        """
        constraining_clause =
            CONSTRAINEDBY type_specifier class_modification?
        """
        return (
            cls.CONSTRAINEDBY,
            cls.type_specifier,
            Optional(cls.class_modification),
        )

    # §B.2.4 Component Clause
    @classmethod
    def component_clause(cls):  # type: ignore
        """
        component_clause =
            type_prefix type_specifier array_subscripts? component_list
        """
        return (
            cls.type_prefix,
            cls.type_specifier,
            Optional(cls.array_subscripts),
            cls.component_list,
        )

    @classmethod
    def type_prefix(cls):  # type: ignore
        """
        type_prefix =
            (FLOW/STREAM)? (DISCRETE/PARAMETER/CONSTANT)? (INPUT/OUTPUT)?
        """
        return (
            Optional([cls.FLOW, cls.STREAM]),
            Optional(
                [
                    cls.DISCRETE,
                    cls.PARAMETER,
                    cls.CONSTANT,
                ]
            ),
            Optional(
                [
                    cls.INPUT,
                    cls.OUTPUT,
                ]
            ),
        )

    @classmethod
    def component_list(cls):  # type: ignore
        """
        component_list =
            component_declaration ("," component_declaration)*
        """
        return cls.component_declaration, ZeroOrMore(
            ",", cls.component_declaration
        )

    @classmethod
    def component_declaration(cls):  # type: ignore
        """
        component_declaration =
            declaration condition_attribute? comment
        """
        return (
            cls.declaration,
            Optional(cls.condition_attribute),
            cls.comment,
        )

    @classmethod
    def condition_attribute(cls):  # type: ignore
        """
        condition_attribute =
            IF expression
        """
        return cls.IF, cls.expression

    @classmethod
    def declaration(cls):  # type: ignore
        """
        declaration =
            IDENT array_subscripts? modification?
        """
        return (
            cls.IDENT,
            Optional(cls.array_subscripts),
            Optional(cls.modification),
        )

    # §B.2.5 Modification
    @classmethod
    def modification(cls):  # type: ignore
        """
        modification =
            "=" expression
            / ":=" expression
            / class_modification ("=" expression)?
        """
        return [
            ("=", cls.expression),
            (":=", cls.expression),
            (cls.class_modification, Optional("=", cls.expression)),
        ]

    @classmethod
    def class_modification(cls):  # type: ignore
        """
        class_modification =
            "(" argument_list? ")"
        """
        return "(", Optional(cls.argument_list), ")"

    @classmethod
    def argument_list(cls):  # type: ignore
        """
        argument_list =
            argument ("," argument)*
        """
        return cls.argument, ZeroOrMore(",", cls.argument)

    @classmethod
    def argument(cls):  # type: ignore
        """
        argument =
            element_redeclaration
            / element_modification_or_replaceable
        """
        return [
            cls.element_redeclaration,
            cls.element_modification_or_replaceable,
        ]

    @classmethod
    def element_modification_or_replaceable(cls):  # type: ignore
        """
        element_modification_or_replaceable =
            EACH? FINAL? (element_modification / element_replaceable)
        """
        return (
            Optional(cls.EACH),
            Optional(cls.FINAL),
            [cls.element_modification, cls.element_replaceable],
        )

    @classmethod
    def element_modification(cls):  # type: ignore
        """
        element_modification =
            name modification? string_comment
        """
        return (
            cls.name,
            Optional(cls.modification),
            cls.string_comment,
        )

    @classmethod
    def element_redeclaration(cls):  # type: ignore
        """
        element_redeclaration =
            REDECLARE EACH? FINAL?
            ((short_class_definition / component_clause1) / element_replaceable)
        """  # noqa: E501
        return (
            cls.REDECLARE,
            Optional(cls.EACH),
            Optional(cls.FINAL),
            [
                [
                    cls.short_class_definition,
                    cls.component_clause1,
                ],
                cls.element_replaceable,
            ],
        )

    @classmethod
    def element_replaceable(cls):  # type: ignore
        """
        element_replaceable =
            REPLACEABLE (short_class_definition / component_clause1)
            constraining_clause?
        """
        return (
            cls.REPLACEABLE,
            [cls.short_class_definition, cls.component_clause1],
            Optional(cls.constraining_clause),
        )

    @classmethod
    def component_clause1(cls):  # type: ignore
        """
        component_clause1 =
            type_prefix type_specifier component_declaration1
        """
        return (
            cls.type_prefix,
            cls.type_specifier,
            cls.component_declaration1,
        )

    @classmethod
    def component_declaration1(cls):  # type: ignore
        """
        component_declaration1 =
            declaration comment
        """
        return cls.declaration, cls.comment

    @classmethod
    def short_class_definition(cls):  # type: ignore
        """
        short_class_definition =
            class_prefixes short_class_specifier
        """
        return cls.class_prefixes, cls.short_class_specifier

    # §B.2.6 Equations
    @classmethod
    def equation_section(cls):  # type: ignore
        """
        equation_section =
            INITIAL? EQUATION (equation ";")*
        """
        return (
            Optional(cls.INITIAL),
            cls.EQUATION,
            ZeroOrMore(cls.equation, ";"),
        )

    @classmethod
    def algorithm_section(cls):  # type: ignore
        """
        algorithm_section =
            INITIAL? ALGORITHM (statement ";")*
        """
        return (
            Optional(cls.INITIAL),
            cls.ALGORITHM,
            ZeroOrMore(cls.statement, ";"),
        )

    @classmethod
    def equation(cls):  # type: ignore
        """
        equation =
            (
                if_equation
                / for_equation
                / connect_clause
                / when_equation
                / simple_expression "=" expression
                / component_reference function_call_args
            )
            comment
        """
        return (
            [
                cls.if_equation,
                cls.for_equation,
                cls.connect_clause,
                cls.when_equation,
                (cls.simple_expression, "=", cls.expression),
                (cls.component_reference, cls.function_call_args),
            ],
            cls.comment,
        )

    @classmethod
    def statement(cls):  # type: ignore
        """
        statement =
            (
                BREAK
                / RETURN
                / if_statement
                / for_statement
                / while_statement
                / when_statement
                / "(" output_expression_list ")" ":="
                component_reference function_call_args
                / component_reference (":=" expression / function_call_args)
            )
            comment
        """
        return (
            [
                cls.BREAK,
                cls.RETURN,
                cls.if_statement,
                cls.for_statement,
                cls.while_statement,
                cls.when_statement,
                (
                    "(",
                    cls.output_expression_list,
                    ")",
                    ":=",
                    cls.component_reference,
                    cls.function_call_args,
                ),
                (
                    cls.component_reference,
                    [(":=", cls.expression), cls.function_call_args],
                ),
            ],
            cls.comment,
        )

    @classmethod
    def if_equation(cls):  # type: ignore
        """
        if_equation =
            IF     expression THEN (equation ";")*
        ( ELSEIF expression THEN (equation ";")* )*
        ( ELSE                   (equation ";")* )?
            END IF
        """
        return (
            cls.IF,
            cls.expression,
            cls.THEN,
            ZeroOrMore(
                cls.equation,
                ";",
            ),
            ZeroOrMore(
                cls.ELSEIF,
                cls.expression,
                cls.THEN,
                ZeroOrMore(
                    cls.equation,
                    ";",
                ),
            ),
            Optional(
                cls.ELSE,
                ZeroOrMore(
                    cls.equation,
                    ";",
                ),
            ),
            cls.END,
            cls.IF,
        )

    @classmethod
    def if_statement(cls):  # type: ignore
        """
        if_statement =
            IF     expression THEN (statement ";")*
        ( ELSEIF expression THEN (statement ";")* )*
        ( ELSE                   (statement ";")* )?
            END IF
        """
        return (
            cls.IF,
            cls.expression,
            cls.THEN,
            ZeroOrMore(
                cls.statement,
                ";",
            ),
            ZeroOrMore(
                cls.ELSEIF,
                cls.expression,
                cls.THEN,
                ZeroOrMore(
                    cls.statement,
                    ";",
                ),
            ),
            Optional(
                cls.ELSE,
                ZeroOrMore(
                    cls.statement,
                    ";",
                ),
            ),
            cls.END,
            cls.IF,
        )

    @classmethod
    def for_equation(cls):  # type: ignore
        """
        for_equation =
            FOR for_indices LOOP
                (equation ";")*
            END FOR
        """
        return (
            cls.FOR,
            cls.for_indices,
            cls.LOOP,
            ZeroOrMore(
                cls.equation,
                ";",
            ),
            cls.END,
            cls.FOR,
        )

    @classmethod
    def for_statement(cls):  # type: ignore
        """
        for_statement =
            FOR for_indices LOOP
                (statement ";")*
            END FOR
        """
        return (
            cls.FOR,
            cls.for_indices,
            cls.LOOP,
            ZeroOrMore(
                cls.statement,
                ";",
            ),
            cls.END,
            cls.FOR,
        )

    @classmethod
    def for_indices(cls):  # type: ignore
        """
        for_indices =
            for_index ("," for_index)*
        """
        return cls.for_index, ZeroOrMore(",", cls.for_index)

    @classmethod
    def for_index(cls):  # type: ignore
        """
        for_index =
            IDENT (IN expression)?
        """
        return cls.IDENT, Optional(cls.IN, cls.expression)

    @classmethod
    def while_statement(cls):  # type: ignore
        """
        while_statement =
            WHILE expression LOOP
                (statement ";")*
            END WHILE
        """
        return (
            cls.WHILE,
            cls.expression,
            cls.LOOP,
            ZeroOrMore(
                cls.statement,
                ";",
            ),
            cls.END,
            cls.WHILE,
        )

    @classmethod
    def when_equation(cls):  # type: ignore
        """
        when_equation =
            WHEN     expression THEN (equation ";")*
        ( ELSEWHEN expression THEN (equation ";")* )*
            END WHEN
        """
        return (
            cls.WHEN,
            cls.expression,
            cls.THEN,
            ZeroOrMore(
                cls.equation,
                ";",
            ),
            ZeroOrMore(
                cls.ELSEWHEN,
                cls.expression,
                cls.THEN,
                ZeroOrMore(
                    cls.equation,
                    ";",
                ),
            ),
            cls.END,
            cls.WHEN,
        )

    @classmethod
    def when_statement(cls):  # type: ignore
        """
        when_statement =
            WHEN     expression THEN (statement ";")*
        ( ELSEWHEN expression THEN (statement ";")* )*
            END WHEN
        """
        return (
            cls.WHEN,
            cls.expression,
            cls.THEN,
            ZeroOrMore(
                cls.statement,
                ";",
            ),
            ZeroOrMore(
                cls.ELSEWHEN,
                cls.expression,
                cls.THEN,
                ZeroOrMore(
                    cls.statement,
                    ";",
                ),
            ),
            cls.END,
            cls.WHEN,
        )

    @classmethod
    def connect_clause(cls):  # type: ignore
        """
        connect_clause =
            CONNECT "(" component_reference "," component_reference ")"
        """
        return (
            cls.CONNECT,
            "(",
            cls.component_reference,
            ",",
            cls.component_reference,
            ")",
        )

    # §B.2.7 Expressions
    @classmethod
    def expression(cls):  # type: ignore
        """
        expression =
            simple_expression
            / IF expression THEN expression
            (ELSEIF expression THEN expression)*
            ELSE expression
        """
        return [
            cls.simple_expression,
            (
                (
                    cls.IF,
                    cls.expression,
                    cls.THEN,
                    cls.expression,
                ),
                ZeroOrMore(
                    cls.ELSEIF,
                    cls.expression,
                    cls.THEN,
                    cls.expression,
                ),
                (
                    cls.ELSE,
                    cls.expression,
                ),
            ),
        ]

    @classmethod
    def simple_expression(cls):  # type: ignore
        """
        simple_expression =
            logical_expression (":" logical_expression (":" logical_expression)?)?
        """  # noqa: E501
        return (
            cls.logical_expression,
            Optional(
                ":",
                cls.logical_expression,
                Optional(":", cls.logical_expression),
            ),
        )

    @classmethod
    def logical_expression(cls):  # type: ignore
        """
        logical_expression =
            logical_term (OR logical_term)*
        """
        return cls.logical_term, ZeroOrMore(cls.OR, cls.logical_term)

    @classmethod
    def logical_term(cls):  # type: ignore
        """
        logical_term =
            logical_factor (AND logical_factor)*
        """
        return cls.logical_factor, ZeroOrMore(cls.AND, cls.logical_factor)

    @classmethod
    def logical_factor(cls):  # type: ignore
        """
        logical_factor =
            NOT? relation
        """
        return Optional(cls.NOT), cls.relation

    @classmethod
    def relation(cls):  # type: ignore
        """
        relation =
            arithmetic_expression (relational_operator arithmetic_expression)?
        """
        return (
            cls.arithmetic_expression,
            Optional(cls.relational_operator, cls.arithmetic_expression),
        )

    @classmethod
    def relational_operator(cls):  # type: ignore
        """
        relational_operator =
            "<>" / "<=" / ">=" / "<" / ">" / "=="
        """
        return ["<>", "<=", ">=", "<", ">", "=="]

    @classmethod
    def arithmetic_expression(cls):  # type: ignore
        """
        arithmetic_expression =
            add_operator? term (add_operator term)*
        """

        return (
            Optional(cls.add_operator),
            cls.term,
            ZeroOrMore(cls.add_operator, cls.term),
        )

    @classmethod
    def add_operator(cls):  # type: ignore
        """
        add_operator =
            "+" / "-" / ".+" / ".-"
        """
        return ["+", "-", ".+", ".-"]

    @classmethod
    def term(cls):  # type: ignore
        """
        term =
            factor (mul_operator factor)*
        """
        return cls.factor, ZeroOrMore(cls.mul_operator, cls.factor)

    @classmethod
    def mul_operator(cls):  # type: ignore
        """
        mul_operator =
            "*" / "/" / ".*" / "./"
        """
        return ["*", "/", ".*", "./"]

    @classmethod
    def factor(cls):  # type: ignore
        """
        factor =
            primary (("^" / ".^") primary)?
        """
        return cls.primary, Optional(["^", ".^"], cls.primary)

    @classmethod
    def primary(cls):  # type: ignore
        """
        primary =
            FALSE
            / TRUE
            / END
            / UNSIGNED_NUMBER
            / STRING
            / "(" output_expression_list ")"
            / "[" expression_list (";" expression_list)* "]"
            / "{" array_arguments "}"
            / (component_reference / DER / INITIAL / PURE) function_call_args
            / component_reference
        """
        return [
            cls.FALSE,
            cls.TRUE,
            cls.END,
            cls.UNSIGNED_NUMBER,
            cls.STRING,
            ("(", cls.output_expression_list, ")"),
            (
                "[",
                cls.expression_list,
                ZeroOrMore(";", cls.expression_list),
                "]",
            ),
            ("{", cls.array_arguments, "}"),
            (
                [
                    cls.component_reference,
                    cls.DER,
                    cls.INITIAL,
                    cls.PURE,
                ],
                cls.function_call_args,
            ),
            cls.component_reference,
        ]

    @classmethod
    def type_specifier(cls):  # type: ignore
        """
        type_specifier = "."? name
        """
        return Optional("."), cls.name

    @classmethod
    def name(cls):  # type: ignore
        """
        name = IDENT ("." IDENT)*
        """
        return cls.IDENT, ZeroOrMore(".", cls.IDENT)

    @classmethod
    def component_reference(cls):  # type: ignore
        """
        component_reference =
            "."? IDENT array_subscripts? ("." IDENT array_subscripts?)*
        """
        return (
            Optional("."),
            cls.IDENT,
            Optional(cls.array_subscripts),
            ZeroOrMore(".", cls.IDENT, Optional(cls.array_subscripts)),
        )

    @classmethod
    def function_call_args(cls):  # type: ignore
        """
        function_call_args =
            "(" function_arguments? ")"
        """
        return "(", Optional(cls.function_arguments), ")"

    @classmethod
    def function_arguments(cls):  # type: ignore
        """
        function_arguments =
            FUNCTION name "(" named_arguments? ")"
            ("," function_arguments_non_first)?
            / named_arguments
            / expression ("," function_arguments_non_first / FOR for_indices)
        """
        return [
            (
                cls.FUNCTION,
                cls.name,
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
                        (
                            ",",
                            cls.function_arguments_non_first,
                        ),  # type: ignore
                        (cls.FOR, cls.for_indices),  # type: ignore
                    ]
                ),
            ),
        ]

    @classmethod
    def function_arguments_non_first(cls):  # type: ignore
        """
        function_arguments_non_first =
            named_arguments
            / function_argument ("," function_arguments_non_first)?
        """
        return [
            cls.named_arguments,
            (
                cls.function_argument,
                Optional(",", cls.function_arguments_non_first),
            ),
        ]

    @classmethod
    def named_arguments(cls):  # type: ignore
        """
        named_arguments = named_argument ("," named_arguments)?
        """
        return cls.named_argument, ZeroOrMore(",", cls.named_argument)

    @classmethod
    def array_arguments(cls):  # type: ignore
        """
        array_arguments =
            expression ("," array_arguments_non_first / FOR for_indices)?
        """
        return (
            cls.expression,
            Optional(
                [
                    (",", cls.array_arguments_non_first),  # type: ignore
                    (cls.FOR, cls.for_indices),  # type: ignore
                ]
            ),
        )

    @classmethod
    def array_arguments_non_first(cls):  # type: ignore
        """
        array_arguments_non_first =
            expression ("," array_arguments_non_first)?
        """
        return cls.expression, ZeroOrMore(",", cls.expression)

    @classmethod
    def named_argument(cls):  # type: ignore
        """
        named_argument = IDENT "=" function_argument
        """
        return cls.IDENT, "=", cls.function_argument

    @classmethod
    def function_argument(cls):  # type: ignore
        """
        function_argument =
            FUNCTION name "(" named_arguments? ")"
            / expression
        """
        return [
            (
                cls.FUNCTION,
                cls.name,
                "(",
                Optional(cls.named_arguments),
                ")",
            ),
            cls.expression,
        ]

    @classmethod
    def output_expression_list(cls):  # type: ignore
        """
        output_expression_list =
            expression? ("," expression?)*
        """
        return (
            Optional(cls.expression),
            ZeroOrMore(",", Optional(cls.expression)),
        )

    @classmethod
    def expression_list(cls):  # type: ignore
        """
        expression_list =
            expression ("," expression)*
        """
        return cls.expression, ZeroOrMore(",", cls.expression)

    @classmethod
    def array_subscripts(cls):  # type: ignore
        """
        array_subscripts =
            "[" subscript ("," subscript)* "]"
        """
        return "[", cls.subscript, ZeroOrMore(",", cls.subscript), "]"

    @classmethod
    def subscript(cls):  # type: ignore
        """
        subscript =
            ":" / expression
        """
        return [":", cls.expression]

    @classmethod
    def comment(cls):  # type: ignore
        """
        comment =
            string_comment annotation?
        """
        return (
            cls.string_comment,
            Optional(cls.annotation),
        )

    @classmethod
    def string_comment(cls):  # type: ignore
        """
        string_comment =
            (STRING ("+" STRING)*)?
        """
        return Optional(cls.STRING, ZeroOrMore("+", cls.STRING))

    @classmethod
    def annotation(cls):  # type: ignore
        """
        annotation =
            ANNOTATION class_modification
        """
        return cls.ANNOTATION, cls.class_modification
