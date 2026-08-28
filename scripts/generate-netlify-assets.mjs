import { writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';

const fallbackUrl = 'https://laura-gonzalez-estudio-creativo.lgel.chatgpt.site';
const siteUrl = (process.env.URL || fallbackUrl).replace(/\/$/, '');
const output = resolve(process.cwd(), 'dist');

await Promise.all([
  writeFile(
    resolve(output, 'robots.txt'),
    `User-agent: *\nAllow: /\n\nSitemap: ${siteUrl}/sitemap.xml\n`,
  ),
  writeFile(
    resolve(output, 'sitemap.xml'),
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url>\n    <loc>${siteUrl}/</loc>\n    <changefreq>monthly</changefreq>\n    <priority>1.0</priority>\n  </url>\n</urlset>\n`,
  ),
]);

console.log(`Netlify assets generated for ${siteUrl}`);
