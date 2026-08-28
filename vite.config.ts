import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/postcss';
import { fileURLToPath, URL } from 'node:url';
import { defineConfig, type Plugin } from 'vite';

function netlifyMetadata(): Plugin {
  return {
    name: 'netlify-metadata',
    transformIndexHtml(html) {
      const fallbackUrl = 'https://laura-gonzalez-estudio-creativo.lgel.chatgpt.site';
      const siteUrl = (process.env.URL || fallbackUrl).replace(/\/$/, '');
      return html.replaceAll('__SITE_URL__', siteUrl);
    },
  };
}

export default defineConfig({
  plugins: [react(), netlifyMetadata()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('.', import.meta.url)),
    },
  },
  css: {
    postcss: {
      plugins: [tailwindcss()],
    },
  },
  build: {
    target: 'es2021',
    sourcemap: false,
    cssCodeSplit: true,
    reportCompressedSize: true,
  },
  server: {
    port: 3000,
    host: true,
  },
  preview: {
    port: 3000,
    host: true,
  },
});
