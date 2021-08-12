# Happy Config
 Managing ML experiment configuration with joy.
 
 - Use `dataclass` to define the schema for experiment configurations.
 - Load configuration from multiple sources: JSON, YAML, NNI.
 - Annotate fields with search space, and generate NNI search space file using CLI tool.
 
## Basic Usage

**Define configuration schema with `dataclass`**

```python
from dataclasses import dataclass

@dataclass
class Bar:
    a: str
    b: str

@dataclass 
class Foo:
    x: int
    y: int
    bar: Bar
```

**Write configuration files**

```json
{
  "x": 1,
  "y": 1,
  "bar:a": "1",
  "bar:b": "1"
}
```

Note the namespace syntax `bar:a` we use in JSON. It is also possible to write:

```json
{
  "x": 1,
  "y": 1,
  "bar": {
    "a": "1"
  },
  "bar:b": "1"
}
```
 
**Create a `ConfigLoader` instacen from the schema, and load the configuration**

```python
from happy_config import ConfigLoader
loader = ConfigLoader(model=Foo, config="config.json")
config: Foo = loader()  # Foo(x=1, y=1, bar=Bar(a="1", b="1"))
```

If we save the code in `main.py`, we can use command line arguments to specify the configuration file path:
```shell
python main.py --config config.json
```

And we can overwrite the configurations directly using command line arguments:
```shell
python main.py --x 10 --bar:b 100
```
We have to use the namespace syntax here.

## Generating NNI Search Space File

We embed parameter search spaces in the definition of configuration schema.

```python
from dataclasses import dataclass
from happy_config import ConfigLoader
from happy_config.typechecking import show_type
from happy_config.param_tuning import with_search_space


@dataclass
class Bar:
    s: str


@dataclass
class Foo:
    y: int
    bar: Bar
    x: float = with_search_space(1.0, space_type='uniform', space_value=[0.0, 1.0])


@dataclass
class Config:
    foo: Foo
    i: int = with_search_space(0, space_type='choice', space_value=[1, 2, 3])
```

Save the file in `main.py`. And in CLI:
```
python -m happy_config genspace -m main.Config -o search_space.json
```

The outputed `search_space.json` file:
```json
{
    "foo:x": {
        "_type": "uniform",
        "_value": [
            0.0,
            1.0
        ]
    },
    "i": {
        "_type": "choice",
        "_value": [
            1,
            2,
            3
        ]
    }
}
```
