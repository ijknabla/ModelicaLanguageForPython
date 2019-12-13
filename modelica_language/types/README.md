
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

SizeBase "1" o-- "0..n" Sizes
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
