from dataclasses import dataclass
from happy_config import ConfigLoader
from happy_config.typechecking import show_type


@dataclass
class Bar:
    s: str


@dataclass
class Foo:
    x: float
    y: int
    bar: Bar


@dataclass
class Config:
    foo: Foo
    i: int = 0


if __name__ == '__main__':
    loader = ConfigLoader(model=Config, config='basic.json')
    print(show_type(loader.config_type))
    config = loader()
    print(config)
