from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles


def swagger_initialize(app, api_title, api_prefix):
    app.mount("/static", StaticFiles(directory="static"), name="static")



    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=f"{api_prefix}{app.openapi_url}",
            title=api_title,
            swagger_js_url=f"{api_prefix}/static/swagger-ui-bundle.js",
            swagger_css_url=f"{api_prefix}/static/swagger-ui.css",
            swagger_favicon_url=f"{api_prefix}/static/favicon.png",
            #swagger_ui_parameters={"supportedSubmitMethods": [] } # remove "Try it out" button
        )
    @app.get("/openapi.json", include_in_schema=False)
    async def get_open_api():
        return get_openapi(title="My API", version="1.0.0", routes=app.routes)
    