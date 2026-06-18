#!/bin/bash
cd "$(dirname "$0")"

if [ -f index.html.off ]; then
  echo "⚠️  El website ya está apagado."
  read -p "Presiona Enter para cerrar..."
  exit 0
fi

echo "🔴 Apagando el website..."
mv index.html index.html.off
cat > index.html << 'OFFLINE'
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mac Digitali</title>
  <style>
    body { background: #0a0a0a; color: #fff; font-family: Arial, sans-serif;
           display: flex; align-items: center; justify-content: center;
           min-height: 100vh; margin: 0; text-align: center; }
    h1 { font-size: 52px; color: #cc0000; letter-spacing: 4px; margin-bottom: 10px; }
    p  { color: rgba(255,255,255,0.35); font-size: 14px; letter-spacing: 3px; text-transform: uppercase; }
  </style>
</head>
<body>
  <div>
    <h1>🚨</h1>
    <h1>MAC DIGITALI</h1>
    <p>Sitio temporalmente fuera de línea</p>
  </div>
</body>
</html>
OFFLINE

git add index.html index.html.off
git commit -m "🔴 Website APAGADO"
git push

echo ""
echo "✅ Website apagado! GitHub Pages se actualiza en ~1 minuto."
read -p "Presiona Enter para cerrar..."
