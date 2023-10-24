# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Removed

- Support for `python==3.6`
- `modelicalang.returns_parsing_expression` type-hint for arpeggio

## [0.1.0a1] - 2023-07-12

### Added

- `modelicalang.ModelicaLangInternalWarning` Warning class
    - It will be raised if arpeggio extension not enabled

### Removed

- Package dependency to `typing-extensions`

## [0.1.0a0] - 2023-02-01

### Added

- Type-hints for strict type checking for arpeggio
    - `modelicalang.ParsingExpressionLike`
    - `modelicalang.returns_parsing_expression`
- Extensible modelica grammar definition using arpeggio
    - `modelicalang.v3_4.Syntax` [Modelica Concrete Syntax v3.4](https://specification.modelica.org/maint/3.4/A2.html)
    - `modelicalang.v3_5.Syntax` [Modelica Concrete Syntax v3.5](https://specification.modelica.org/maint/3.5/modelica-concrete-syntax.html)


[Unreleased]: https://github.com/ijknabla/ModelicaLanguageForPython/compare/v0.1.0a1...HEAD
[0.1.0a1]: https://github.com/ijknabla/ModelicaLanguageForPython/tree/v0.1.0a1
[0.1.0a0]: https://github.com/ijknabla/ModelicaLanguageForPython/tree/v0.1.0a0
