from dependency_injector.wiring import Provide, inject
from bclib.edge import RESTfulContext, HttpStatusCodes
from typing import Dict

@inject
def widget_data_func(context: RESTfulContext, sample_json:Dict=Provide["sample_json"]):
    widget_id = context.url_segments.widgetid
    widgets = sample_json["widgets"]
    for widget in widgets:
        if str(widget["id"]) == widget_id:
            return widget["data"]
    context.status_code = HttpStatusCodes.NOT_FOUND
    return  f"widget with id={widget_id} not found"