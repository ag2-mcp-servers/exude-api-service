# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T19:03:55+00:00



import argparse
import json
import os
from typing import *

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity
from fastapi import UploadFile

from models import ExudeResponseBean

app = MCPProxy(
    description='Exude API is an Open Source project, It is used for the primary ways for filtering the stopping, stemming words from the text data. This API is in a very basic level of development need to work on for later changes.',
    termsOfService='http://uttesh.com/apis/terms/',
    title='Exude API Service',
    version='1.0.0',
    servers=[
        {
            'description': 'Use Heruko deployment for testing/development',
            'url': 'https://exude-api.herokuapp.com',
        },
        {
            'description': 'Use docker container and deploy on the production environment or locally developmenet',
            'url': 'http://localhost:8080',
        },
    ],
)


@app.post('/exude/{type}/data', tags=['stopping_word_filtering'])
def filter_stoppings(type: str, file: UploadFile = ...):
    """
    Filter the stopping words from the provided input data or links
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post('/exude/{type}/file', tags=['stopping_word_filtering'])
def filter_file_data_stoppings(type: str, file: UploadFile = ...):
    """
    Filter the stopping words from the provided input file
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
