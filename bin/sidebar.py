from dependency_injector.wiring import Provide, inject
from bclib.edge import RESTfulContext, HttpStatusCodes
from typing import Dict

@inject
def sidebar_data_func(context: RESTfulContext, sample_json:Dict=Provide["sample_json"]):
    item_id = context.url_segments.itemid
    sidebars = sample_json["sidebars"]
    for item in sidebars:
        if str(item["id"]) == item_id:
            return item["data"]
    context.status_code = HttpStatusCodes.NOT_FOUND
    return {
        "error": f"sidebar with id={item_id} not found"
    }
