from dependency_injector.wiring import Provide, inject
from bclib.edge import RESTfulContext
from typing import Dict

@inject
def menu_func(_: RESTfulContext, sample_json:Dict=Provide["sample_json"]):
    return sample_json["menu"]