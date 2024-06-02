from dataclasses import dataclass

@dataclass
class Options:
    service_name: str
    routing_type: str
    routing_folder: str
    host: str
    port: int
    settings: dict
    cache: dict

    @property
    def as_edge_options(self):
        return {
            f"{self.routing_type}": f"{self.host}: {self.port}",
            "router": {
                "web": ["/widget"],
                "restful": ["*"],
            },
            "log_error": True,
            "settings": self.settings,
            "cache": self.cache
        }