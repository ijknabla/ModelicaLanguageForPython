from arpeggio import RegExMatch

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
