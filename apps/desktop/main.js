const { app, BrowserWindow } = require("electron");

function createWindow() {
  const win = new BrowserWindow({
    width: 1600,
    height: 900,
    minWidth: 1280,
    minHeight: 720,
    autoHideMenuBar: true,
    backgroundColor: "#0F1117",
    title: "VogueLivin AI Studio",
    webPreferences: {
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  // Open DevTools while developing
  win.webContents.openDevTools();

  // Load the Vite development server
  win.loadURL("http://localhost:5173");

  win.webContents.on("did-finish-load", () => {
    console.log("Frontend Loaded");
  });

  win.webContents.on("did-fail-load", (_, code, description) => {
    console.error("Load Failed:", code, description);
  });
}

app.whenReady().then(createWindow);

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});