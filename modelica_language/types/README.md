
# Python class structure for Modelica® (planned)

## class diagrams

### `modelica_language.types.size`

```plantuml
package builtins {
    class int
    class tuple
}

package enum {
    class Enum
}

package modelica_language.types.size {
    abstract class SizeBase {
        + {abstract} __hash__()
        + {abstract} __index__()
        + {abstract} __eq__()
        + {abstract} asSuffix()
    }

    class FixedSize

    class FlexibleSize << singleton >>

    class Sizes {
        + fromIndices()
    }
}

int      <|-down-  FixedSize
SizeBase <|-up-  FixedSize

Enum     <|-down-  FlexibleSize
SizeBase <|.up.  FlexibleSize

SizeBase o-- "0..n" Sizes
tuple        <|-        Sizes
```

```python
"""
Size(s) for Metaclass
"""

from modelica_languae.types.size import (
    FixedSize, FlexibleSize,
    Sizes
)

# SomeScalar is a ModelicaScalarClass

SomeScalar[:] == SomeScalar[FlexibleSize.flexible]  # -> True
SomeScalar[42] == SomeScalar[FixedSize(42)]  # -> True
SomeScalar[4,2] == SomeScalar[Sizes.fromIndices((4, 2))]  # -> True
```

### `modelica_language.types.abc`

```plantuml
package modelica_language.types {
    package size {
        class Sizes
    }

    package abc {

        class ModelicaClass << metaClass >>
        class ModelicaScalarClass << metaClass >> {
            + {abstract} ModelicaArrayClass arrayClassFactory(Shape)
            + ModelicaArrayClass __getitem__(...)
        }
        class ModelicaArrayClass << metaClass >> {
            + ModelicaScalarClass scalar
            + Shape shape
        }

        together {
            abstract class AbstractModelicaObject
            abstract class AbstractModelicaScalarObject
            abstract class AbstractModelicaArrayObject
        }
    }
}

ModelicaClass <|-- ModelicaScalarClass
ModelicaClass <|-- ModelicaArrayClass

ModelicaClass       <- AbstractModelicaObject \
    : "isinstance"
ModelicaScalarClass <-- AbstractModelicaScalarObject \
    : "isinstance"
ModelicaArrayClass  <-- AbstractModelicaArrayObject \
    : "isinstance"

Sizes --> ModelicaScalarClass : "as index"

ModelicaScalarClass        o-- "1" ModelicaArrayClass
ModelicaScalarClass "1..n" --o     ModelicaArrayClass

AbstractModelicaObject <|- AbstractModelicaScalarObject
AbstractModelicaObject <|- AbstractModelicaArrayObject
```
