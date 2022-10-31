import re
from contextlib import ExitStack

import pytest
from arpeggio import NoMatch, Parser

from modelica_language import ParserPEG
from tests.utils import assert_injective


@pytest.mark.parametrize(
    "text, match",
    [
        ("abc", True),
        (" abc ", True),
        ("ab c", False),
        ("model", False),
        ("modelica", True),
        ("modelA", True),
        ("model0", True),
        ("model:", False),
        ("'model'", True),
        ("$identifier", False),
    ],
)
def test_ident_parser(
    ident_parser: ParserPEG,
    text: str,
    match: bool,
) -> None:
    with ExitStack() as stack:
        if not match:
            stack.enter_context(pytest.raises(NoMatch))
        ident_parser.parse(text)


@pytest.mark.parametrize(
    "text, match",
    [
        ("abc", True),
        (" abc ", True),
        ("ab c", False),
        ("model", False),
        ("modelica", True),
        ("modelA", True),
        ("model0", True),
        ("model:", False),
        ("'model'", True),
        ("$identifier", True),
    ],
)
def test_ident_dialect_parser(
    ident_dialect_parser: ParserPEG,
    text: str,
    match: bool,
) -> None:
    with ExitStack() as stack:
        if not match:
            stack.enter_context(pytest.raises(NoMatch))
        ident_dialect_parser.parse(text)


def test_file_parser(file_parser: Parser) -> None:
    unify = assert_injective(unify_rule_name)

    assert file_parser.parser_model.root
    assert unify(file_parser.parser_model.rule_name) == "file"

    assert file_parser.comments_model is not None
    assert file_parser.comments_model.root
    assert unify(file_parser.comments_model.rule_name) == "COMMENT"


def unify_rule_name(s: str) -> str:
    if re.match(r"_[a-z]+_", s):
        s = s[1:-1].upper()
    return {
        "annotation": "annotation_comment",
        "ANY_KEYWORD": "KEYWORD",
        "CPP_STYLE_COMMENT": "COMMENT",
    }.get(s, s)
