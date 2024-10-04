##  FastAPI Debug Configuration
To add a FastAPI option in the debug configuration of Visual Studio Code, follow these steps:

1. **Open the Debug View**: Click on the debug icon in the Activity Bar on the side of the window or press `Ctrl + Shift + D`.

2. **Create a New Configuration**:
   - Click on the gear icon (⚙️) to open the `launch.json` file.
   - If prompted, select the Python environment.

3. **Add FastAPI Configuration**:
   - In the `launch.json` file, add a new configuration for FastAPI. It should look something like this:

   ```json
   {
       "name": "FastAPI",
       "type": "python",
       "request": "launch",
       "module": "uvicorn",
       "args": [
           "main:app",  // Replace 'main' with your filename without .py
           "--host",
           "localhost",
           "--port",
           "8000",
           "--reload"
       ],
       "jinja": true
   }
   ```

   - Make sure to replace `"main:app"` with the appropriate module and app name if your FastAPI app is defined differently.

4. **Save the Configuration**: Save the `launch.json` file.

5. **Start Dev mode**
   - Run following commnand
      ```bash
      docker compose -f docker-compose.yml up --build
      ```

5. **Start Debugging**:

   `**Add FastAPI Configuration**:
      - In the `launch.json` file, add a new configuration for FastAPI. It should look something like this:

      ```json
       "configurations": [
        {
            "name": "Python Debugger: Remote Attach",
            "type": "debugpy",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 7999
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "."
                }
            ]
        },
        {
            "name": "Python Debugger: FastAPI",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "main:app",
                "--host",
                "localhost",
                "--port",
                "8000",
                "--reload"
            ],
            "jinja": true
        }
      ]
      ```
      - Make sure to replace `"main:app"` with the appropriate module and app name if your FastAPI app is defined differently.`

   - Run following commnand
      ```bash
      docker compose -f docker-compose-debug.yml up --build
      ```
   - Select the FastAPI configuration from the dropdown in the debug view.
   - Click the green play button (▶️) to start debugging your FastAPI application.

   - This approach will work with `.ssh` connections in VS Code as well. VS Code has built-in support for remote development, allowing you to use the **Remote - SSH** extension to seamlessly work and debug on remote machines via SSH.

Now, you should be able to debug your FastAPI application directly from Visual Studio Code!
