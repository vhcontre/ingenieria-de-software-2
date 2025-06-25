# Activar entorno virtual y ejecutar pytest con PYTHONPATH configurado

Write-Host "🟢 Activando entorno virtual..."
. .\venv\Scripts\Activate.ps1

Write-Host "🧪 Ejecutando tests con pytest..."
$env:PYTHONPATH="."
pytest -v tests
