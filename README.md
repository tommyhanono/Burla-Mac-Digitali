# 🚨 Mac Digitali — Hall of Shame

**El archivo oficial de vergüenzas de La Vaada Mac.**

🌐 **Website en vivo:** https://tommyhanono.github.io/Burla-Mac-Digitali/

---

## 🔴 APAGAR el website

Doble click en este archivo:

```
apagar_website.command
```

Se abre una ventana, hace todo solo y cierra. El site queda offline en ~1 minuto.

---

## 🟢 PRENDER el website

Doble click en este archivo:

```
prender_website.command
```

Se abre una ventana, restaura todo y cierra. El site vuelve en ~1 minuto.

---

## 📱 QR Code para imprimir / proyectar

Abre este archivo en el navegador:

```
qr.html
```

Se ve el QR grande con el branding de Mac Digitali. Para imprimir: Cmd+P → escala al 100%.  
Para proyectar: abre el archivo y pasa el navegador a pantalla completa (F11 / Ctrl+Cmd+F).

---

## 📸 Agregar fotos nuevas

1. Pon las fotos en la carpeta `photos/` con el nombre correcto:
   - Mugshot de miembro: `gabriel_1.jpg`, `benji_1.jpg`, etc.
   - Fotos de galería extra: `extra_1.jpg`, `extra_2.jpg`, etc.
2. Actualiza el campo `photo:` en el JS de `index.html`
3. Sube los cambios:
```bash
git add . && git commit -m "📸 Fotos" && git push
```
