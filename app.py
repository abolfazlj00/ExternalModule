from container import Container
from options import OptionsFileType, BaseOptions
from bclib.edge import RESTfulContext, WebContext, HttpStatusCodes
import json
from bin import menu_func, page_data_func, sidebar_data_func, widget_data_func, error_messages_func

with open("sample.json") as f: 
    sample_json = json.load(f)

container = Container()
container.config.set("sample_json", sample_json)
container.wire(packages=["options", "bin"])
op:BaseOptions = container.app_options_factory(OptionsFileType.YAML, ".yaml")
options = op.initialize()
service_name = options.service_name
routing_folder = options.routing_folder
edge_options = options.as_edge_options
# print(f"Running service '{service_name}'")

app = container.dispatcher_routing(edge_options)

# RESTFUL HANDLERS

@app.restful_action(
    app.url(f"{routing_folder}/:rkey/:culture/:device/menu")
)
def process_menu(context: RESTfulContext):
    return menu_func(context)

@app.restful_action(
    app.url(f"{routing_folder}/:rkey/:culture/:device/page/:pageid")
)
def process_page_data(context: RESTfulContext):
    return page_data_func(context)

@app.restful_action(
    app.url(f"{routing_folder}/:rkey/:culture/:device/sidebarMenu/:itemid")
)
def process_sidebar_data(context: RESTfulContext):
    return sidebar_data_func(context)

@app.restful_action(
    app.url(f"{routing_folder}/:rkey/errormessages")
)
def process_restful_handler(context: RESTfulContext):
    return error_messages_func(context)

# WEB HANDLERS

@app.web_action(
    app.url(f"{routing_folder}/:rkey/:culture/:device/widget/:widgetid")
)
def process_widget_data(context: RESTfulContext):
    return widget_data_func(context)



# NOT FOUND HANDLERS

@app.restful_action()
def process_404_restful(context: RESTfulContext):
    context.status_code = HttpStatusCodes.NOT_FOUND
    return {
        "ServiceName": f"{service_name}"
    }

@app.web_action()
def process_404(context: WebContext):
    context.status_code = HttpStatusCodes.NOT_FOUND
    return f"This is '{service_name}' service"

app.listening()
