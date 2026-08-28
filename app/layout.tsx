import type { Metadata } from 'next';
import { Cormorant_Garamond, Manrope } from 'next/font/google';
import './globals.css';

const manrope = Manrope({
  variable: '--font-body',
  subsets: ['latin'],
});

const cormorant = Cormorant_Garamond({
  variable: '--font-display',
  subsets: ['latin'],
});

export const metadata: Metadata = {
  metadataBase: new URL('https://laura-gonzalez-estudio-creativo.lgel.chatgpt.site'),
  title: 'Laura González — Estrategia digital & contenido',
  description:
    'Estrategia, contenido y experiencias digitales para marcas que quieren crecer con intención.',
  openGraph: {
    title: 'Laura González — Estrategia digital & contenido',
    description:
      'Estrategia, contenido y experiencias digitales para marcas que quieren crecer con intención.',
    url: 'https://laura-gonzalez-estudio-creativo.lgel.chatgpt.site',
    siteName: 'Laura González — Estudio Creativo',
    locale: 'es_AR',
    type: 'website',
    images: [
      {
        url: 'https://laura-gonzalez-estudio-creativo.lgel.chatgpt.site/og.png',
        width: 1200,
        height: 630,
        alt: 'Laura González — Estrategia digital & contenido',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Laura González — Estrategia digital & contenido',
    description:
      'Estrategia, contenido y experiencias digitales para marcas que quieren crecer con intención.',
    images: ['https://laura-gonzalez-estudio-creativo.lgel.chatgpt.site/og.png'],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es" suppressHydrationWarning>
      <body className={`${manrope.variable} ${cormorant.variable} antialiased`}>
        {children}
      </body>
    </html>
  );
}
