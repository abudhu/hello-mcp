# Hello MCP Server

A simple Python MCP (Model Context Protocol) server that provides a greeting tool.

## Features

- **greet tool**: Responds to greeting messages, especially "how are you" with "I am great"
- **Dual mode**: Runs in stdio mode for local development or HTTP mode for remote access
- **Docker ready**: Fully containerized with Docker and docker-compose support

## Installation

### Local Development

1. Make sure you have Python installed
2. Install the required dependencies:

```powershell
pip install mcp
```

Or using uv:

```powershell
uv add mcp
```

### Docker Deployment

Make sure you have Docker and Docker Compose installed.

## Running the Server

### Local Development (stdio mode)

**Using Python directly:**

```powershell
python server.py
```

**Using uv:**

```powershell
uv run server.py
```

### Local HTTP Mode

To run the server in HTTP mode locally:

```powershell
$env:TRANSPORT="http"
python server.py
```

The server will be available at `http://localhost:8000/mcp`

### Docker Deployment

#### Using Docker Compose (Recommended)

```powershell
# Build and start the container
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the container
docker-compose down
```

#### Using Docker directly

```powershell
# Build the image
docker build -t hello-mcp-server .

# Run the container
docker run -d -p 8000:8000 --name hello-mcp-server hello-mcp-server

# View logs
docker logs -f hello-mcp-server

# Stop the container
docker stop hello-mcp-server
docker rm hello-mcp-server
```

## Testing the Server

### Testing HTTP Endpoint

Once running in HTTP mode, the server exposes an MCP endpoint at:
- **Local**: `http://localhost:8000/mcp`
- **Container**: `http://localhost:8000/mcp`

You can connect to it using any MCP client that supports HTTP transport.

### With MCP Inspector

```powershell
npx @modelcontextprotocol/inspector python server.py
```

### With Claude Desktop (Local stdio mode)

Add this configuration to your Claude Desktop config file:

**Location**: `%AppData%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "hello-mcp": {
      "command": "python",
      "args": ["c:\\Users\\ambudhu\\Github\\hello-mcp\\server.py"]
    }
  }
}
```

Then restart Claude Desktop and you should see the tool available!

### With Claude.ai (HTTP mode)

If you're running the server in HTTP mode (locally or in Docker), you can connect to it from Claude.ai:

1. Go to Claude.ai settings
2. Add a custom connector
3. Enter the URL: `http://localhost:8000/mcp` (or your server's public URL)

### With VS Code (HTTP mode)

Update your `.vscode/mcp.json`:

```json
{
  "servers": {
    "hello-mcp-server": {
      "type": "http",
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

### With VS Code

The server is already configured in `.vscode/mcp.json` for use with VS Code's MCP support.

## Usage

Once connected to the server, you can use the `greet` tool:

```
Tool: greet
Arguments: {"message": "how are you"}
Response: "I am great"
```

## Deployment Options

### Running Locally
- Best for: Development and testing
- Transport: stdio or HTTP
- Access: Local machine only

### Running in Docker (Local)
- Best for: Testing containerization, isolated environment
- Transport: HTTP
- Access: `http://localhost:8000/mcp`

### Running in Production
For production deployment, you can:

1. **Deploy to cloud providers**: AWS ECS, Google Cloud Run, Azure Container Apps
2. **Use Kubernetes**: Deploy the container with proper ingress configuration
3. **Add reverse proxy**: Use nginx or Traefik for SSL/TLS termination
4. **Set up monitoring**: Add health checks and logging aggregation

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `TRANSPORT` | `stdio` | Transport mode: `stdio` or `http` |
| `HOST` | `0.0.0.0` | Host to bind to (use `0.0.0.0` for containers) |
| `PORT` | `8000` | Port to listen on |

## Project Structure

```
hello-mcp/
├── server.py                    # Main MCP server implementation
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker image definition
├── docker-compose.yml           # Docker Compose configuration
├── .dockerignore               # Docker build exclusions
├── README.md                   # This file
├── .vscode/
│   └── mcp.json                # VS Code MCP configuration
└── .github/
    └── copilot-instructions.md # Project instructions
```

## Security Considerations

When deploying in production:

1. **Use HTTPS**: Always use TLS/SSL in production
2. **Authentication**: Consider adding authentication (OAuth, API keys)
3. **Rate limiting**: Implement rate limiting to prevent abuse
4. **CORS**: Configure CORS appropriately for browser-based clients
5. **Monitoring**: Set up proper logging and monitoring
6. **Secrets**: Never commit secrets; use environment variables or secret management

## Learn More

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP Documentation](https://modelcontextprotocol.github.io/python-sdk/)
