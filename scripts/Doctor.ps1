Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "   VogueLivin AI Studio Doctor"
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

function Test-ItemExists($label, $path) {
    if (Test-Path $path) {
        Write-Host "[OK]  $label" -ForegroundColor Green
    } else {
        Write-Host "[FAIL] $label" -ForegroundColor Red
    }
}

Write-Host "Checking Project Structure..." -ForegroundColor Yellow

Test-ItemExists "Backend"      "apps\backend"
Test-ItemExists "Frontend"     "apps\frontend"
Test-ItemExists "Desktop"      "apps\desktop"
Test-ItemExists "Workflows"    "workflows"
Test-ItemExists "Models"       "models"

Write-Host ""
Write-Host "Checking ComfyUI..." -ForegroundColor Yellow

$comfy = "C:\AI\ComfyUI"

Test-ItemExists "ComfyUI Root" "$comfy"
Test-ItemExists "Models" "$comfy\models"
Test-ItemExists "Custom Nodes" "$comfy\custom_nodes"
Test-ItemExists "Output Folder" "$comfy\output"

Write-Host ""
Write-Host "Checking Tools..." -ForegroundColor Yellow

try {
    python --version
} catch {
    Write-Host "Python Missing" -ForegroundColor Red
}

try {
    node -v
} catch {
    Write-Host "Node Missing" -ForegroundColor Red
}

try {
    git --version
} catch {
    Write-Host "Git Missing" -ForegroundColor Red
}

Write-Host ""
Write-Host "Doctor Completed." -ForegroundColor Green
