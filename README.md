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

5. **Start Debugging**:
   - Select the FastAPI configuration from the dropdown in the debug view.
   - Click the green play button (▶️) to start debugging your FastAPI application.

Now, you should be able to debug your FastAPI application directly from Visual Studio Code!
