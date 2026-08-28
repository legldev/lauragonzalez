# Laura González — Estudio Creativo

Sitio bilingüe de marca personal construido con React, TypeScript, Vite y Tailwind CSS.

## Desarrollo local

```bash
npm install
npm run dev
```

## Verificación

```bash
npm run typecheck
npm run lint
npm run build
```

## Despliegue en Netlify

Importar el repositorio `legldev/lauragonzalez` desde Netlify. El archivo `netlify.toml` ya configura:

- comando de compilación: `npm run build`;
- carpeta publicada: `dist`;
- versión de Node.js;
- fallback para navegación SPA;
- políticas de seguridad y caché;
- metadatos, sitemap y robots con la URL asignada por Netlify.

No requiere variables privadas ni funciones de servidor.
