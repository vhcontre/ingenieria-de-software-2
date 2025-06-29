# 🚨 ATENCIÓN: Este script sobreescribe el historial de la rama `main`
# Úsalo solo cuando ya hayas eliminado todo el código fuente del repositorio
# y quieras eliminar también los diffs visibles desde antiguos Pull Requests.

# 👉 Asegurate de estar en la carpeta local del repositorio
# 👉 También asegurate de tener respaldo si querés conservar el historial anterior

# PASO 1: Crear una nueva rama sin historial previo
git checkout --orphan nuevo-main

# PASO 2: Eliminar todos los archivos actuales del directorio de trabajo
git rm -rf .

# PASO 3: Crear un README para dejar algo visible y mantener estructura
echo "# Repositorio limpio para trabajo estudiantil" > README.md

# PASO 4: Agregar y hacer commit del nuevo estado limpio
git add .
git commit -m "Reset completo del historial - sin código fuente"

# PASO 5 (opcional): Guardar el historial anterior bajo una nueva rama
git branch backup-historial
git push origin backup-historial

# PASO 6: Forzar reemplazo de la rama `main` en GitHub
git push origin +nuevo-main:main

Write-Host "`n✅ El historial fue limpiado correctamente. Los Pull Requests antiguos ya no podrán mostrar código."
