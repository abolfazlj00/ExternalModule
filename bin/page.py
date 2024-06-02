from dependency_injector.wiring import Provide, inject
from bclib.edge import RESTfulContext, HttpStatusCodes
from typing import Dict

@inject
def page_data_func(context: RESTfulContext, sample_json:Dict=Provide["sample_json"]):
    page_id = context.url_segments.pageid
    pages = sample_json["pages"]
    for page in pages:
        if str(page["id"]) == page_id:
            return page["data"]
    context.status_code = HttpStatusCodes.NOT_FOUND
    return {
        "error": f"page with id={page_id} not found"
    }