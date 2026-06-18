#!/bin/bash
cd "$(dirname "$0")"

if [ ! -f index.html.off ]; then
  echo "⚠️  El website ya está prendido."
  read -p "Presiona Enter para cerrar..."
  exit 0
fi

echo "🟢 Prendiendo el website..."
rm index.html
mv index.html.off index.html

git add index.html
git rm --cached index.html.off 2>/dev/null || true
git add -u
git commit -m "🟢 Website PRENDIDO"
git push

echo ""
echo "✅ Website prendido! GitHub Pages se actualiza en ~1 minuto."
read -p "Presiona Enter para cerrar..."
