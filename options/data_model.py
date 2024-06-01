from dataclasses import dataclass

@dataclass
class Options:
    service_name: str
    routing_folder: str
    host: str
    port: int
    settings: dict
    cache: dict

    @property
    def as_edge_options(self):
        return {
            "server": f"{self.host}: {self.port}",
            "router": {
                "restful": [self.routing_folder],
                "web": ["*"],
            },
            "log_error": True,
            "settings": self.settings,
            "cache": self.cache
        }