from container import Container
from options import OptionsFileType, BaseOptions
from bclib.edge import RESTfulContext, WebContext, HttpStatusCodes

container = Container()
container.wire(packages=["app", "options"])
op:BaseOptions = container.app_options_factory(OptionsFileType.YAML, ".yaml")
options = op.initialize()
print(f"Running service '{options.service_name}'")
edge_options = options.as_edge_options
print(edge_options)
app = container.dispatcher_routing(edge_options)

@app.restful_action(
    app.url(f"{options.routing_folder}/:rkey/errormessages")
)
def process_restful_handler(context: RESTfulContext):
    return [
        {
            "errorCode": num,
            "errorMessage": f"error_{num}"
        }
        for num in range(10)
    ]

@app.restful_action(
    app.url(f"{options.routing_folder}/:*url")
)
def process_404_restful(context: RESTfulContext):
    context.status_code = HttpStatusCodes.NOT_FOUND
    return {
        "error": "404 error"
    }

@app.web_action()
def process_404(context: WebContext):
    context.status_code = HttpStatusCodes.NOT_FOUND
    return "404 error"

app.listening()
