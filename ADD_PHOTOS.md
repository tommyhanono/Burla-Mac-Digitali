# 📸 Cómo agregar fotos a Burla Mac Digitali

## Paso 1 — Nombrar las fotos

| Persona | Nombre de archivo |
|---|---|
| Gabriel | `gabriel_1.jpg`, `gabriel_2.jpg`, … |
| Benji | `benji_1.jpg`, `benji_2.jpg`, … |
| Beny | `beny_1.jpg`, `beny_2.jpg`, … |
| Elias | `elias_1.jpg`, `elias_2.jpg`, … |
| Alesandra | `alesandra_1.jpg`, `alesandra_2.jpg`, … |
| Helena | `helena_1.jpg`, `helena_2.jpg`, … |
| Mike | `mike_1.jpg`, `mike_2.jpg`, … |
| Sarah | `sarah_1.jpg`, `sarah_2.jpg`, … |
| Camila | `camila_1.jpg`, `camila_2.jpg`, … |
| Isaac Hamui | `isaac_hamui_1.jpg`, `isaac_hamui_2.jpg`, … |
| Galería general | `gallery_1.jpg`, `gallery_2.jpg`, … |

**Formatos soportados:** `.jpg` `.jpeg` `.png` `.webp`

---

## Paso 2 — Copiar fotos a la carpeta /photos

Arrastra y suelta tus fotos en:
```
burla-mac-digitali/
└── photos/
    ├── gabriel_1.jpg
    ├── elias_1.jpg
    ├── gallery_1.jpg
    └── ...
```

---

## Paso 3 — Correr el script

```bash
cd burla-mac-digitali
python3 inject_photos.py
```

El script:
- Pone la **primera foto** de cada persona como su mugshot en la tarjeta
- Agrega fotos adicionales a la galería con caption "Evidencia adicional: [nombre]"
- Llena los slots restantes de la galería con fotos `gallery_*.jpg`
- Reescribe `index.html` automáticamente
- Imprime un resumen de cuántas fotos se inyectaron

---

## Paso 4 — Subir a GitHub Pages

```bash
git add .
git commit -m "📸 Fotos agregadas"
git push
```

GitHub Pages se actualiza solo en ~1-2 minutos.

---

## Notas

- Puedes correr `inject_photos.py` múltiples veces sin problema — sobreescribe lo anterior
- Si no hay foto para alguien, el placeholder gris se mantiene
- Las fotos se referencian con ruta relativa `photos/nombre.jpg` — no las muevas después
