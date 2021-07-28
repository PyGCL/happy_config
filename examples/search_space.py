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


if __name__ == '__main__':
    loader = ConfigLoader(model=Config, default_param_path='basic.json')
    print(show_type(loader.config_type))
    config = loader()
    print(config)
