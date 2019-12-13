
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

### `modelica_language.types.array`

```plantuml
package modelica_language.types {
    package abc {
        class ModelicaScalarClass << metaClass >>
        class ModelicaArrayClass << metaClass >>
    }
    package array {
        together {
            class PrimitiveReal
            'class PrimitiveInteger
            'class PrimitiveBoolean
            'class PrimitiveString
        }

        together {
            class PrimitiveRealArray
            'class PrimitiveIntegerArray
            'class PrimitiveBooleanArray
            'class PrimitiveStringArray
        }
    }
}

ModelicaScalarClass <--- PrimitiveReal         : "isinstance"
'ModelicaScalarClass <--- PrimitiveInteger      : "isinstance"
'ModelicaScalarClass <--- PrimitiveBoolean      : "isinstance"
'ModelicaScalarClass <--- PrimitiveString       : "isinstance"

ModelicaArrayClass  <-- PrimitiveRealArray    : "isinstance"
'ModelicaArrayClass  <-- PrimitiveIntegerArray : "isinstance"
'ModelicaArrayClass  <-- PrimitiveBooleanArray : "isinstance"
'ModelicaArrayClass  <-- PrimitiveStringArray  : "isinstance"

PrimitiveReal    o-- "1..n" PrimitiveRealArray
'PrimitiveInteger o-- "1..n" PrimitiveIntegerArray
'PrimitiveBoolean o-- "1..n" PrimitiveBooleanArray
'PrimitiveString  o-- "1..n" PrimitiveStringArray
```

<!--

```plantuml
package modelica_language.types.array {
    class InheritableNDArray
    class StrAsObjectNDArray
    class CurlyBracesNDArray
    class NDArrayWrapper
}

numpy.ndarray <|-- InheritableNDArray

InheritableNDArray <|-- StrAsObjectNDArray
InheritableNDArray <|-- CurlyBracesNDArray

StrAsObjectNDArray <|-- NDArrayWrapper
CurlyBracesNDArray <|-- NDArrayWrapper
```

#### `NDArrayWrapper`

`NDArrayWrapper` is a _thin_ wrapper of numpy.ndarray for representing Modelica arrays.

- Change string representation to use curly braces `{` `}` instead of square brackets `[` `]`
- Suppress using `np.str_`. `str` array always be `dtype=object` array

#### `defaultArrayClassFactory(...)`

`defaultArrayClassFactory(...)` create new Modelica array class.
Modelica array class returned by `defaultArrayClassFactory(...)` will inherit `NDArrayWrapper` and their metaclass will be subclass of `modelica_language.types.meta.ModelicaArrayClassMeta`.

```python
from typing import Optional
from modelica_language.types import meta

def defaultArrayClassFactory(
    scalarClass: meta.ModelicaScalarClassMeta,
    sizes: meta.Sizes,
    name: Optional[str] = None,
) -> meta.ModelicaArrayClassMeta:
    ...
```

-->