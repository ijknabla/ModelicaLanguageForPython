__all__ = (
    "ANY_KEYWORD",
    "ALGORITHM",
    "AND",
    "ANNOTATION",
    "BLOCK",
    "BREAK",
    "CLASS",
    "CONNECT",
    "CONNECTOR",
    "CONSTANT",
    "CONSTRAINEDBY",
    "DER",
    "DISCRETE",
    "EACH",
    "ELSE",
    "ELSEIF",
    "ELSEWHEN",
    "ENCAPSULATED",
    "END",
    "ENUMERATION",
    "EQUATION",
    "EXPANDABLE",
    "EXTENDS",
    "EXTERNAL",
    "FALSE",
    "FINAL",
    "FLOW",
    "FOR",
    "FUNCTION",
    "IF",
    "IMPORT",
    "IMPURE",
    "IN",
    "INITIAL",
    "INNER",
    "INPUT",
    "LOOP",
    "MODEL",
    "NOT",
    "OPERATOR",
    "OR",
    "OUTER",
    "OUTPUT",
    "PACKAGE",
    "PARAMETER",
    "PARTIAL",
    "PROTECTED",
    "PUBLIC",
    "PURE",
    "RECORD",
    "REDECLARE",
    "REPLACEABLE",
    "RETURN",
    "STREAM",
    "THEN",
    "TRUE",
    "TYPE",
    "WHEN",
    "WHILE",
    "WITHIN",
)

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


def ANY_KEYWORD():  # type: ignore
    return RegExMatch(any_keyword)


ANY_KEYWORD.__doc__ = f"ANY_KEYWORD = r'{any_keyword}'"


def ALGORITHM():  # type: ignore
    r"ALGORITHM = r'algorithm(?!\w)'"
    return RegExMatch(r"algorithm(?!\w)")


def AND():  # type: ignore
    r"AND = r'and(?!\w)'"
    return RegExMatch(r"and(?!\w)")


def ANNOTATION():  # type: ignore
    r"ANNOTATION = r'annotation(?!\w)'"
    return RegExMatch(r"annotation(?!\w)")


def BLOCK():  # type: ignore
    r"BLOCK = r'block(?!\w)'"
    return RegExMatch(r"block(?!\w)")


def BREAK():  # type: ignore
    r"BREAK = r'break(?!\w)'"
    return RegExMatch(r"break(?!\w)")


def CLASS():  # type: ignore
    r"CLASS = r'class(?!\w)'"
    return RegExMatch(r"class(?!\w)")


def CONNECT():  # type: ignore
    r"CONNECT = r'connect(?!\w)'"
    return RegExMatch(r"connect(?!\w)")


def CONNECTOR():  # type: ignore
    r"CONNECTOR = r'connector(?!\w)'"
    return RegExMatch(r"connector(?!\w)")


def CONSTANT():  # type: ignore
    r"CONSTANT = r'constant(?!\w)'"
    return RegExMatch(r"constant(?!\w)")


def CONSTRAINEDBY():  # type: ignore
    r"CONSTRAINEDBY = r'constrainedby(?!\w)'"
    return RegExMatch(r"constrainedby(?!\w)")


def DER():  # type: ignore
    r"DER = r'der(?!\w)'"
    return RegExMatch(r"der(?!\w)")


def DISCRETE():  # type: ignore
    r"DISCRETE = r'discrete(?!\w)'"
    return RegExMatch(r"discrete(?!\w)")


def EACH():  # type: ignore
    r"EACH = r'each(?!\w)'"
    return RegExMatch(r"each(?!\w)")


def ELSE():  # type: ignore
    r"ELSE = r'else(?!\w)'"
    return RegExMatch(r"else(?!\w)")


def ELSEIF():  # type: ignore
    r"ELSEIF = r'elseif(?!\w)'"
    return RegExMatch(r"elseif(?!\w)")


def ELSEWHEN():  # type: ignore
    r"ELSEWHEN = r'elsewhen(?!\w)'"
    return RegExMatch(r"elsewhen(?!\w)")


def ENCAPSULATED():  # type: ignore
    r"ENCAPSULATED = r'encapsulated(?!\w)'"
    return RegExMatch(r"encapsulated(?!\w)")


def END():  # type: ignore
    r"END = r'end(?!\w)'"
    return RegExMatch(r"end(?!\w)")


def ENUMERATION():  # type: ignore
    r"ENUMERATION = r'enumeration(?!\w)'"
    return RegExMatch(r"enumeration(?!\w)")


def EQUATION():  # type: ignore
    r"EQUATION = r'equation(?!\w)'"
    return RegExMatch(r"equation(?!\w)")


def EXPANDABLE():  # type: ignore
    r"EXPANDABLE = r'expandable(?!\w)'"
    return RegExMatch(r"expandable(?!\w)")


def EXTENDS():  # type: ignore
    r"EXTENDS = r'extends(?!\w)'"
    return RegExMatch(r"extends(?!\w)")


def EXTERNAL():  # type: ignore
    r"EXTERNAL = r'external(?!\w)'"
    return RegExMatch(r"external(?!\w)")


def FALSE():  # type: ignore
    r"FALSE = r'false(?!\w)'"
    return RegExMatch(r"false(?!\w)")


def FINAL():  # type: ignore
    r"FINAL = r'final(?!\w)'"
    return RegExMatch(r"final(?!\w)")


def FLOW():  # type: ignore
    r"FLOW = r'flow(?!\w)'"
    return RegExMatch(r"flow(?!\w)")


def FOR():  # type: ignore
    r"FOR = r'for(?!\w)'"
    return RegExMatch(r"for(?!\w)")


def FUNCTION():  # type: ignore
    r"FUNCTION = r'function(?!\w)'"
    return RegExMatch(r"function(?!\w)")


def IF():  # type: ignore
    r"IF = r'if(?!\w)'"
    return RegExMatch(r"if(?!\w)")


def IMPORT():  # type: ignore
    r"IMPORT = r'import(?!\w)'"
    return RegExMatch(r"import(?!\w)")


def IMPURE():  # type: ignore
    r"IMPURE = r'impure(?!\w)'"
    return RegExMatch(r"impure(?!\w)")


def IN():  # type: ignore
    r"IN = r'in(?!\w)'"
    return RegExMatch(r"in(?!\w)")


def INITIAL():  # type: ignore
    r"INITIAL = r'initial(?!\w)'"
    return RegExMatch(r"initial(?!\w)")


def INNER():  # type: ignore
    r"INNER = r'inner(?!\w)'"
    return RegExMatch(r"inner(?!\w)")


def INPUT():  # type: ignore
    r"INPUT = r'input(?!\w)'"
    return RegExMatch(r"input(?!\w)")


def LOOP():  # type: ignore
    r"LOOP = r'loop(?!\w)'"
    return RegExMatch(r"loop(?!\w)")


def MODEL():  # type: ignore
    r"MODEL = r'model(?!\w)'"
    return RegExMatch(r"model(?!\w)")


def NOT():  # type: ignore
    r"NOT = r'not(?!\w)'"
    return RegExMatch(r"not(?!\w)")


def OPERATOR():  # type: ignore
    r"OPERATOR = r'operator(?!\w)'"
    return RegExMatch(r"operator(?!\w)")


def OR():  # type: ignore
    r"OR = r'or(?!\w)'"
    return RegExMatch(r"or(?!\w)")


def OUTER():  # type: ignore
    r"OUTER = r'outer(?!\w)'"
    return RegExMatch(r"outer(?!\w)")


def OUTPUT():  # type: ignore
    r"OUTPUT = r'output(?!\w)'"
    return RegExMatch(r"output(?!\w)")


def PACKAGE():  # type: ignore
    r"PACKAGE = r'package(?!\w)'"
    return RegExMatch(r"package(?!\w)")


def PARAMETER():  # type: ignore
    r"PARAMETER = r'parameter(?!\w)'"
    return RegExMatch(r"parameter(?!\w)")


def PARTIAL():  # type: ignore
    r"PARTIAL = r'partial(?!\w)'"
    return RegExMatch(r"partial(?!\w)")


def PROTECTED():  # type: ignore
    r"PROTECTED = r'protected(?!\w)'"
    return RegExMatch(r"protected(?!\w)")


def PUBLIC():  # type: ignore
    r"PUBLIC = r'public(?!\w)'"
    return RegExMatch(r"public(?!\w)")


def PURE():  # type: ignore
    r"PURE = r'pure(?!\w)'"
    return RegExMatch(r"pure(?!\w)")


def RECORD():  # type: ignore
    r"RECORD = r'record(?!\w)'"
    return RegExMatch(r"record(?!\w)")


def REDECLARE():  # type: ignore
    r"REDECLARE = r'redeclare(?!\w)'"
    return RegExMatch(r"redeclare(?!\w)")


def REPLACEABLE():  # type: ignore
    r"REPLACEABLE = r'replaceable(?!\w)'"
    return RegExMatch(r"replaceable(?!\w)")


def RETURN():  # type: ignore
    r"RETURN = r'return(?!\w)'"
    return RegExMatch(r"return(?!\w)")


def STREAM():  # type: ignore
    r"STREAM = r'stream(?!\w)'"
    return RegExMatch(r"stream(?!\w)")


def THEN():  # type: ignore
    r"THEN = r'then(?!\w)'"
    return RegExMatch(r"then(?!\w)")


def TRUE():  # type: ignore
    r"TRUE = r'true(?!\w)'"
    return RegExMatch(r"true(?!\w)")


def TYPE():  # type: ignore
    r"TYPE = r'type(?!\w)'"
    return RegExMatch(r"type(?!\w)")


def WHEN():  # type: ignore
    r"WHEN = r'when(?!\w)'"
    return RegExMatch(r"when(?!\w)")


def WHILE():  # type: ignore
    r"WHILE = r'while(?!\w)'"
    return RegExMatch(r"while(?!\w)")


def WITHIN():  # type: ignore
    r"WITHIN = r'within(?!\w)'"
    return RegExMatch(r"within(?!\w)")
