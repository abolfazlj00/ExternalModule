from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory, FactoryAggregate, Singleton
from options import OptionsFileType, JsonBaseOptions, YamlBaseOptions
from bclib import edge

class Container(DeclarativeContainer):
    config = Configuration()

    app_options_factory = FactoryAggregate(
        {  
            OptionsFileType.JSON: Factory(
                JsonBaseOptions
            ),
            OptionsFileType.YAML: Factory(
                YamlBaseOptions
            )
        }
    )

    dispatcher_routing = Singleton(
        edge.from_options
    )