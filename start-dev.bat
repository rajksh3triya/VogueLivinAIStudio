@echo off
title VogueLivin AI Studio

echo =====================================
echo   Starting VogueLivin AI Studio
echo =====================================
echo.

REM ---------- Frontend ----------
start "Frontend" cmd /k "cd /d C:\AI\VogueLivinAIStudio\apps\frontend && npm run dev"

timeout /t 3 /nobreak >nul

REM ---------- Backend ----------
start "Backend" cmd /k "cd /d C:\AI\VogueLivinAIStudio\apps\backend && .venv\Scripts\activate && uvicorn main:app --reload --port 8000"

timeout /t 3 /nobreak >nul

REM ---------- Electron ----------
start "Desktop" cmd /k "cd /d C:\AI\VogueLivinAIStudio\apps\desktop && npm start"

exit