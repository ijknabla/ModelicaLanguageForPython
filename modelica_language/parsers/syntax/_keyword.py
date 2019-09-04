
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
    r'('
    r'algorithm|and|annotation|block|break|class|connect|connector|'
    r'constant|constrainedby|der|discrete|each|else|elseif|elsewhen|'
    r'encapsulated|end|enumeration|equation|expandable|extends|external|'
    r'false|final|flow|for|function|if|import|impure|in|initial|inner|'
    r'input|loop|model|not|operator|or|outer|output|package|parameter|'
    r'partial|protected|public|pure|record|redeclare|replaceable|return|'
    r'stream|then|true|type|when|while|within'
    r')(?!\w)'
)


def ANY_KEYWORD():
    return RegExMatch(any_keyword)


ANY_KEYWORD.__doc__ = f"ANY_KEYWORD = r'{any_keyword}'"


def ALGORITHM():
    r"ALGORITHM = r'algorithm(?!\w)'"
    return RegExMatch(r'algorithm(?!\w)')


def AND():
    r"AND = r'and(?!\w)'"
    return RegExMatch(r'and(?!\w)')


def ANNOTATION():
    r"ANNOTATION = r'annotation(?!\w)'"
    return RegExMatch(r'annotation(?!\w)')


def BLOCK():
    r"BLOCK = r'block(?!\w)'"
    return RegExMatch(r'block(?!\w)')


def BREAK():
    r"BREAK = r'break(?!\w)'"
    return RegExMatch(r'break(?!\w)')


def CLASS():
    r"CLASS = r'class(?!\w)'"
    return RegExMatch(r'class(?!\w)')


def CONNECT():
    r"CONNECT = r'connect(?!\w)'"
    return RegExMatch(r'connect(?!\w)')


def CONNECTOR():
    r"CONNECTOR = r'connector(?!\w)'"
    return RegExMatch(r'connector(?!\w)')


def CONSTANT():
    r"CONSTANT = r'constant(?!\w)'"
    return RegExMatch(r'constant(?!\w)')


def CONSTRAINEDBY():
    r"CONSTRAINEDBY = r'constrainedby(?!\w)'"
    return RegExMatch(r'constrainedby(?!\w)')


def DER():
    r"DER = r'der(?!\w)'"
    return RegExMatch(r'der(?!\w)')


def DISCRETE():
    r"DISCRETE = r'discrete(?!\w)'"
    return RegExMatch(r'discrete(?!\w)')


def EACH():
    r"EACH = r'each(?!\w)'"
    return RegExMatch(r'each(?!\w)')


def ELSE():
    r"ELSE = r'else(?!\w)'"
    return RegExMatch(r'else(?!\w)')


def ELSEIF():
    r"ELSEIF = r'elseif(?!\w)'"
    return RegExMatch(r'elseif(?!\w)')


def ELSEWHEN():
    r"ELSEWHEN = r'elsewhen(?!\w)'"
    return RegExMatch(r'elsewhen(?!\w)')


def ENCAPSULATED():
    r"ENCAPSULATED = r'encapsulated(?!\w)'"
    return RegExMatch(r'encapsulated(?!\w)')


def END():
    r"END = r'end(?!\w)'"
    return RegExMatch(r'end(?!\w)')


def ENUMERATION():
    r"ENUMERATION = r'enumeration(?!\w)'"
    return RegExMatch(r'enumeration(?!\w)')


def EQUATION():
    r"EQUATION = r'equation(?!\w)'"
    return RegExMatch(r'equation(?!\w)')


def EXPANDABLE():
    r"EXPANDABLE = r'expandable(?!\w)'"
    return RegExMatch(r'expandable(?!\w)')


def EXTENDS():
    r"EXTENDS = r'extends(?!\w)'"
    return RegExMatch(r'extends(?!\w)')


def EXTERNAL():
    r"EXTERNAL = r'external(?!\w)'"
    return RegExMatch(r'external(?!\w)')


def FALSE():
    r"FALSE = r'false(?!\w)'"
    return RegExMatch(r'false(?!\w)')


def FINAL():
    r"FINAL = r'final(?!\w)'"
    return RegExMatch(r'final(?!\w)')


def FLOW():
    r"FLOW = r'flow(?!\w)'"
    return RegExMatch(r'flow(?!\w)')


def FOR():
    r"FOR = r'for(?!\w)'"
    return RegExMatch(r'for(?!\w)')


def FUNCTION():
    r"FUNCTION = r'function(?!\w)'"
    return RegExMatch(r'function(?!\w)')


def IF():
    r"IF = r'if(?!\w)'"
    return RegExMatch(r'if(?!\w)')


def IMPORT():
    r"IMPORT = r'import(?!\w)'"
    return RegExMatch(r'import(?!\w)')


def IMPURE():
    r"IMPURE = r'impure(?!\w)'"
    return RegExMatch(r'impure(?!\w)')


def IN():
    r"IN = r'in(?!\w)'"
    return RegExMatch(r'in(?!\w)')


def INITIAL():
    r"INITIAL = r'initial(?!\w)'"
    return RegExMatch(r'initial(?!\w)')


def INNER():
    r"INNER = r'inner(?!\w)'"
    return RegExMatch(r'inner(?!\w)')


def INPUT():
    r"INPUT = r'input(?!\w)'"
    return RegExMatch(r'input(?!\w)')


def LOOP():
    r"LOOP = r'loop(?!\w)'"
    return RegExMatch(r'loop(?!\w)')


def MODEL():
    r"MODEL = r'model(?!\w)'"
    return RegExMatch(r'model(?!\w)')


def NOT():
    r"NOT = r'not(?!\w)'"
    return RegExMatch(r'not(?!\w)')


def OPERATOR():
    r"OPERATOR = r'operator(?!\w)'"
    return RegExMatch(r'operator(?!\w)')


def OR():
    r"OR = r'or(?!\w)'"
    return RegExMatch(r'or(?!\w)')


def OUTER():
    r"OUTER = r'outer(?!\w)'"
    return RegExMatch(r'outer(?!\w)')


def OUTPUT():
    r"OUTPUT = r'output(?!\w)'"
    return RegExMatch(r'output(?!\w)')


def PACKAGE():
    r"PACKAGE = r'package(?!\w)'"
    return RegExMatch(r'package(?!\w)')


def PARAMETER():
    r"PARAMETER = r'parameter(?!\w)'"
    return RegExMatch(r'parameter(?!\w)')


def PARTIAL():
    r"PARTIAL = r'partial(?!\w)'"
    return RegExMatch(r'partial(?!\w)')


def PROTECTED():
    r"PROTECTED = r'protected(?!\w)'"
    return RegExMatch(r'protected(?!\w)')


def PUBLIC():
    r"PUBLIC = r'public(?!\w)'"
    return RegExMatch(r'public(?!\w)')


def PURE():
    r"PURE = r'pure(?!\w)'"
    return RegExMatch(r'pure(?!\w)')


def RECORD():
    r"RECORD = r'record(?!\w)'"
    return RegExMatch(r'record(?!\w)')


def REDECLARE():
    r"REDECLARE = r'redeclare(?!\w)'"
    return RegExMatch(r'redeclare(?!\w)')


def REPLACEABLE():
    r"REPLACEABLE = r'replaceable(?!\w)'"
    return RegExMatch(r'replaceable(?!\w)')


def RETURN():
    r"RETURN = r'return(?!\w)'"
    return RegExMatch(r'return(?!\w)')


def STREAM():
    r"STREAM = r'stream(?!\w)'"
    return RegExMatch(r'stream(?!\w)')


def THEN():
    r"THEN = r'then(?!\w)'"
    return RegExMatch(r'then(?!\w)')


def TRUE():
    r"TRUE = r'true(?!\w)'"
    return RegExMatch(r'true(?!\w)')


def TYPE():
    r"TYPE = r'type(?!\w)'"
    return RegExMatch(r'type(?!\w)')


def WHEN():
    r"WHEN = r'when(?!\w)'"
    return RegExMatch(r'when(?!\w)')


def WHILE():
    r"WHILE = r'while(?!\w)'"
    return RegExMatch(r'while(?!\w)')


def WITHIN():
    r"WITHIN = r'within(?!\w)'"
    return RegExMatch(r'within(?!\w)')
