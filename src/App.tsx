import {
  ArrowDownRight,
  ArrowRight,
  ArrowUpRight,
  Check,
  ChevronRight,
  Globe2,
  Heart,
  Menu,
  MessageCircle,
  Moon,
  Palette,
  PenTool,
  Send,
  Sparkles,
  Sun,
  Target,
  X,
} from 'lucide-react';
import { type SyntheticEvent, useEffect, useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';

type Language = 'es' | 'en';

const copy = {
  es: {
    nav: ['Servicios', 'Sobre mí', 'Experiencia', 'Contacto'],
    available: 'Disponible para nuevos proyectos',
    location: 'Córdoba, Argentina · Para todo el mundo',
    hero: <>Tu marca merece<br />ser <em>inolvidable.</em></>,
    intro: 'Estrategia, contenido y experiencias digitales que conectan con tu audiencia y hacen crecer tu negocio con intención.',
    talk: 'Hablemos de tu marca',
    discover: 'Descubrir servicios',
    thoughtful: 'Estrategia con sensibilidad',
    converts: 'Creatividad que también convierte.',
    hello: 'Hola, soy Laura',
    role: <>Estratega digital &<br />creadora de contenido</>,
    strip: ['ESTRATEGIA DIGITAL', 'CONTENIDO QUE CONECTA', 'MARCAS CON PROPÓSITO', 'DISEÑO WEB'],
    servicesEyebrow: 'SERVICIOS A MEDIDA',
    servicesTitle: <>Todo lo que tu marca necesita<br />para <em>crecer con intención.</em></>,
    servicesIntro: 'Una mirada estratégica, creativa y humana para construir una presencia digital coherente, atractiva y lista para convertir.',
    services: [
      ['Estrategia de redes sociales', 'Auditoría, objetivos, pilares de contenido, calendario editorial y hoja de ruta para comunicar con claridad.'],
      ['Gestión de comunidades', 'Planificación, publicación, atención de mensajes y conversaciones que fortalecen la relación con tu audiencia.'],
      ['Creación de contenido', 'Reels, piezas gráficas, carruseles, historias y edición de video alineados con la esencia de tu marca.'],
      ['Copywriting & campañas', 'Textos con personalidad, llamados a la acción y campañas promocionales pensadas para conectar y vender.'],
      ['Diseño web & presencia digital', 'Landing pages y sitios de marca elegantes, responsivos y enfocados en transformar visitas en consultas.'],
      ['Consultoría & soporte virtual', 'Sesiones estratégicas, organización comercial, WhatsApp Business, seguimiento de clientes y procesos digitales.'],
    ],
    learn: 'Ver alcance',
    manifesto: 'No se trata de publicar por publicar.',
    manifesto2: <>Se trata de crear una marca que se <em>sienta</em>, se recuerde y se elija.</>,
    aboutEyebrow: 'LA PERSONA DETRÁS DE LA ESTRATEGIA',
    aboutTitle: <>Creatividad, empatía<br />y una mirada <em>muy humana.</em></>,
    aboutP1: 'Soy Laura González, estratega digital y creadora de contenido. Ayudo a marcas, emprendedoras y negocios a ordenar sus ideas, encontrar su voz y mostrarse con confianza.',
    aboutP2: 'Mi recorrido en salud me enseñó a escuchar, cuidar los detalles y acompañar con empatía. Hoy transformo esa sensibilidad en comunicación clara, contenido con propósito y experiencias digitales que acercan personas.',
    aboutQuote: '“Creo en las marcas que no necesitan gritar para dejar huella.”',
    based: 'Radicada en Córdoba · trabajando globalmente',
    journeyEyebrow: 'MI RECORRIDO',
    journeyTitle: <>Experiencia que une<br /><em>organización y creatividad.</em></>,
    current: 'Actualidad',
    expTitle: 'Comunicación digital & redes sociales',
    expCompany: 'Las Liebres Distribuciones · Córdoba, Argentina',
    expText: 'Planificación y publicación de contenido, gestión de Instagram, Facebook y WhatsApp Business, diseño en Canva, edición de video y comunicación comercial.',
    skillsTitle: 'Herramientas que mueven ideas',
    skillList: ['Canva & edición de video', 'Meta Business Suite', 'WhatsApp Business', 'Copywriting & CTA', 'Office & Power BI', 'Herramientas de IA'],
    bgTitle: 'Una base diferente',
    bgText: 'TSU en Tecnología Cardiopulmonar por la Universidad Central de Venezuela. Una formación que aporta precisión, escucha y templanza a cada proyecto.',
    approachEyebrow: 'CÓMO TRABAJAMOS',
    approachTitle: <>Un proceso claro.<br /><em>Una experiencia cercana.</em></>,
    approach: [
      ['01', 'Escuchamos', 'Entiendo tu historia, tus objetivos y lo que hace única a tu marca.'],
      ['02', 'Trazamos la ruta', 'Definimos una estrategia simple, accionable y alineada a tu momento.'],
      ['03', 'Creamos', 'Damos vida a cada pieza con intención, coherencia y sensibilidad.'],
      ['04', 'Medimos & afinamos', 'Observamos, aprendemos y mejoramos para sostener el crecimiento.'],
    ],
    contactEyebrow: 'HAGAMOS ALGO INCREÍBLE',
    contactTitle: <>Tu próxima gran idea<br />puede empezar <em>hoy.</em></>,
    contactIntro: 'Contame sobre tu marca, tu proyecto o esa idea que todavía vive en tus notas. Te respondo con una propuesta clara y sin vueltas.',
    name: 'Nombre',
    email: 'Email',
    brand: 'Marca / Proyecto',
    message: 'Contame qué necesitás',
    namePh: 'Tu nombre',
    emailPh: 'hola@tumarca.com',
    brandPh: 'Nombre de tu marca',
    messagePh: '¿En qué etapa estás y cómo puedo ayudarte?',
    send: 'Enviar consulta',
    sent: '¡Listo! Se abrirá WhatsApp para enviar tu consulta.',
    direct: '¿Preferís hablar directo?',
    response: 'Respondo habitualmente dentro de 24–48 h hábiles.',
    footer: 'Estrategia digital · Contenido · Diseño web',
    rights: 'Todos los derechos reservados.',
  },
  en: {
    nav: ['Services', 'About', 'Experience', 'Contact'],
    available: 'Available for new projects',
    location: 'Córdoba, Argentina · Working worldwide',
    hero: <>Your brand deserves<br />to be <em>unforgettable.</em></>,
    intro: 'Strategy, content and digital experiences that connect with your audience and help your business grow with intention.',
    talk: 'Let’s talk about your brand',
    discover: 'Discover services',
    thoughtful: 'Strategy with sensitivity',
    converts: 'Creativity that also converts.',
    hello: 'Hi, I’m Laura',
    role: <>Digital strategist &<br />content creator</>,
    strip: ['DIGITAL STRATEGY', 'CONTENT THAT CONNECTS', 'PURPOSEFUL BRANDS', 'WEB DESIGN'],
    servicesEyebrow: 'TAILORED SERVICES',
    servicesTitle: <>Everything your brand needs<br />to <em>grow with intention.</em></>,
    servicesIntro: 'A strategic, creative and human perspective to build a cohesive, attractive digital presence designed to convert.',
    services: [
      ['Social media strategy', 'Audit, goals, content pillars, editorial calendar and a clear roadmap for your communication.'],
      ['Community management', 'Planning, publishing, inbox care and meaningful conversations that strengthen your audience relationship.'],
      ['Content creation', 'Reels, graphics, carousels, stories and video editing aligned with your brand essence.'],
      ['Copywriting & campaigns', 'Distinctive copy, clear calls to action and promotional campaigns designed to connect and sell.'],
      ['Web design & digital presence', 'Elegant, responsive landing pages and brand sites focused on turning visits into enquiries.'],
      ['Consulting & virtual support', 'Strategy sessions, commercial organization, WhatsApp Business, customer follow-up and digital processes.'],
    ],
    learn: 'Explore service',
    manifesto: 'It’s not about posting just to post.',
    manifesto2: <>It’s about building a brand people can <em>feel</em>, remember and choose.</>,
    aboutEyebrow: 'THE PERSON BEHIND THE STRATEGY',
    aboutTitle: <>Creativity, empathy<br />and a <em>deeply human</em> eye.</>,
    aboutP1: 'I’m Laura González, a digital strategist and content creator. I help brands, founders and businesses organize their ideas, find their voice and show up with confidence.',
    aboutP2: 'My healthcare background taught me to listen, care about the details and support people with empathy. Today, I turn that sensitivity into clear communication, purposeful content and digital experiences that bring people closer.',
    aboutQuote: '“I believe in brands that don’t need to shout to leave a mark.”',
    based: 'Based in Córdoba · working globally',
    journeyEyebrow: 'MY JOURNEY',
    journeyTitle: <>Experience that brings together<br /><em>organization and creativity.</em></>,
    current: 'Present',
    expTitle: 'Digital communication & social media',
    expCompany: 'Las Liebres Distribuciones · Córdoba, Argentina',
    expText: 'Content planning and publishing, Instagram, Facebook and WhatsApp Business management, Canva design, video editing and commercial communication.',
    skillsTitle: 'Tools that move ideas',
    skillList: ['Canva & video editing', 'Meta Business Suite', 'WhatsApp Business', 'Copywriting & CTA', 'Office & Power BI', 'AI tools'],
    bgTitle: 'A different foundation',
    bgText: 'Higher Technical Degree in Cardiopulmonary Technology from Universidad Central de Venezuela. A background that brings precision, listening and composure to every project.',
    approachEyebrow: 'HOW WE WORK',
    approachTitle: <>A clear process.<br /><em>A close partnership.</em></>,
    approach: [
      ['01', 'We listen', 'I learn your story, your goals and what makes your brand one of a kind.'],
      ['02', 'We map the route', 'We define a simple, actionable strategy aligned with your current stage.'],
      ['03', 'We create', 'We bring each piece to life with intention, consistency and sensitivity.'],
      ['04', 'We measure & refine', 'We observe, learn and improve to support sustainable growth.'],
    ],
    contactEyebrow: 'LET’S MAKE SOMETHING WONDERFUL',
    contactTitle: <>Your next big idea<br />can start <em>today.</em></>,
    contactIntro: 'Tell me about your brand, your project or that idea still living in your notes. I’ll reply with a clear, straightforward proposal.',
    name: 'Name',
    email: 'Email',
    brand: 'Brand / Project',
    message: 'Tell me what you need',
    namePh: 'Your name',
    emailPh: 'hello@yourbrand.com',
    brandPh: 'Your brand name',
    messagePh: 'Where are you now, and how can I help?',
    send: 'Send enquiry',
    sent: 'All set! WhatsApp will open so you can send your enquiry.',
    direct: 'Prefer to talk directly?',
    response: 'I usually reply within 24–48 business hours.',
    footer: 'Digital strategy · Content · Web design',
    rights: 'All rights reserved.',
  },
} as const;

const serviceIcons = [Target, MessageCircle, Sparkles, PenTool, Palette, Globe2];

export default function Home() {
  const [language, setLanguage] = useState<Language>('es');
  const [dark, setDark] = useState(() => {
    const saved = localStorage.getItem('laura-theme');
    return saved === 'dark' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches);
  });
  const [menuOpen, setMenuOpen] = useState(false);
  const [sent, setSent] = useState(false);
  const t = copy[language];

  useEffect(() => {
    document.documentElement.classList.toggle('dark', dark);
    localStorage.setItem('laura-theme', dark ? 'dark' : 'light');
  }, [dark]);

  useEffect(() => {
    document.documentElement.lang = language;
  }, [language]);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => entries.forEach((entry) => entry.isIntersecting && entry.target.classList.add('is-visible')),
      { threshold: 0.12 },
    );
    const elements = document.querySelectorAll('.reveal');
    elements.forEach((element) => observer.observe(element));
    return () => observer.disconnect();
  }, [language]);

  function submitContact(event: SyntheticEvent<HTMLFormElement, SubmitEvent>) {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const field = (name: string) => {
      const value = data.get(name);
      return typeof value === 'string' ? value.trim() : '';
    };
    const name = field('name');
    const brand = field('brand');
    const messageText = field('message');
    const email = field('email');
    const message = [
      `Hola Laura, soy ${name}.`,
      brand ? `Mi marca/proyecto es ${brand}.` : '',
      messageText,
      `Mi email es ${email}.`,
    ].filter(Boolean).join('\n');
    setSent(true);
    window.open(`https://wa.me/5493516215635?text=${encodeURIComponent(message)}`, '_blank', 'noopener,noreferrer');
  }

  const anchors = ['servicios', 'sobre-mi', 'experiencia', 'contacto'];

  return (
    <main className="site-shell">
      <header className="site-header">
        <a href="#inicio" className="brand" aria-label="Laura González, inicio">
          <span>LG</span>
          <small>ESTUDIO CREATIVO</small>
        </a>
        <nav className="desktop-nav" aria-label="Navegación principal">
          {t.nav.map((item, index) => <a key={item} href={`#${anchors[index]}`}>{item}</a>)}
        </nav>
        <div className="header-actions">
          <button className="lang-switch" onClick={() => setLanguage(language === 'es' ? 'en' : 'es')} aria-label="Cambiar idioma / Change language">
            {language.toUpperCase()} <span>/ {language === 'es' ? 'EN' : 'ES'}</span>
          </button>
          <button className="icon-button" onClick={() => setDark((value) => !value)} aria-label={dark ? 'Activar modo claro' : 'Activar modo oscuro'}>
            {dark ? <Sun /> : <Moon />}
          </button>
          <button className="icon-button mobile-menu-button" onClick={() => setMenuOpen(!menuOpen)} aria-label="Abrir menú" aria-expanded={menuOpen}>
            {menuOpen ? <X /> : <Menu />}
          </button>
        </div>
        {menuOpen && (
          <nav className="mobile-nav" aria-label="Navegación móvil">
            {t.nav.map((item, index) => <a key={item} onClick={() => setMenuOpen(false)} href={`#${anchors[index]}`}>{item}<ChevronRight /></a>)}
          </nav>
        )}
      </header>

      <section className="hero" id="inicio">
        <div className="hero-copy">
          <p className="eyebrow"><span /> {t.location}</p>
          <h1>{t.hero}</h1>
          <p className="hero-intro">{t.intro}</p>
          <div className="hero-actions">
            <a className="primary-cta" href="#contacto">{t.talk} <ArrowUpRight /></a>
            <a className="text-link" href="#servicios">{t.discover} <ArrowDownRight /></a>
          </div>
          <div className="trust-row">
            <div className="avatars" aria-hidden="true"><span>✦</span><span>♡</span><span>↑</span></div>
            <p><strong>{t.thoughtful}</strong><br />{t.converts}</p>
          </div>
        </div>

        <div className="hero-visual" aria-label="Retrato de Laura González">
          <div className="portrait-wrap">
            <img src="/images/laura-05.webp" alt="Laura González, estratega digital y creadora de contenido" width="768" height="1024" fetchPriority="high" decoding="async" />
            <span className="sparkle sparkle-one">✦</span><span className="sparkle sparkle-two">✦</span>
          </div>
          <div className="floating-card card-top"><span className="status-dot" /> {t.available}</div>
          <div className="floating-card card-bottom"><span className="script">{t.hello}</span><strong>{t.role}</strong></div>
          <span className="vertical-note">CREATIVIDAD · ESTRATEGIA · CONEXIÓN</span>
        </div>
      </section>

      <div className="marquee" aria-hidden="true">
        <div>{[...t.strip, ...t.strip].map((item, i) => <span key={`${item}-${i}`}>{item}<b>✦</b></span>)}</div>
      </div>

      <section className="services-section section-pad" id="servicios">
        <div className="section-heading reveal">
          <div><p className="section-eyebrow">{t.servicesEyebrow}</p><h2>{t.servicesTitle}</h2></div>
          <p>{t.servicesIntro}</p>
        </div>
        <div className="services-grid">
          {t.services.map(([title, description], index) => {
            const Icon = serviceIcons[index];
            return (
              <article className="service-card reveal" style={{ '--delay': `${index * 70}ms` } as React.CSSProperties} key={title}>
                <div className="service-card-top"><span>0{index + 1}</span><Icon /></div>
                <h3>{title}</h3><p>{description}</p>
                <a href="#contacto">{t.learn} <ArrowRight /></a>
              </article>
            );
          })}
        </div>
      </section>

      <section className="manifesto reveal">
        <span className="manifesto-star">✦</span>
        <p>{t.manifesto}</p><h2>{t.manifesto2}</h2>
        <div className="signature">Laura González</div>
      </section>

      <section className="about-section section-pad" id="sobre-mi">
        <div className="about-collage reveal">
          <div className="about-main-img"><img src="/images/laura-02.webp" alt="Laura González en un espacio creativo" width="768" height="1024" loading="lazy" decoding="async" /></div>
          <div className="about-small-img"><img src="/images/laura-01.webp" alt="Laura González al aire libre en Córdoba" width="768" height="1024" loading="lazy" decoding="async" /></div>
          <div className="roundel" aria-hidden="true"><span>CREAR · CONECTAR · CRECER ·</span><b>LG</b></div>
        </div>
        <div className="about-copy reveal">
          <p className="section-eyebrow">{t.aboutEyebrow}</p><h2>{t.aboutTitle}</h2>
          <p>{t.aboutP1}</p><p>{t.aboutP2}</p>
          <blockquote>{t.aboutQuote}</blockquote>
          <div className="based"><Globe2 /><span>{t.based}</span></div>
        </div>
      </section>

      <section className="journey-section section-pad" id="experiencia">
        <div className="journey-title reveal"><p className="section-eyebrow">{t.journeyEyebrow}</p><h2>{t.journeyTitle}</h2></div>
        <div className="journey-layout">
          <div className="experience-stack reveal">
            <article className="experience-card featured">
              <div className="experience-date">FEB. 2026 — {t.current.toUpperCase()}</div>
              <h3>{t.expTitle}</h3><strong>{t.expCompany}</strong><p>{t.expText}</p>
              <div className="experience-tags"><span>Canva</span><span>Reels</span><span>Social media</span><span>Copywriting</span></div>
            </article>
            <article className="experience-card compact">
              <div><span className="mini-star">✦</span><h3>{t.bgTitle}</h3></div><p>{t.bgText}</p>
            </article>
          </div>
          <div className="skills-panel reveal">
            <img src="/images/laura-03.webp" alt="Laura González observando la ciudad de Córdoba" width="768" height="1024" loading="lazy" decoding="async" />
            <div className="skills-card"><p>{t.skillsTitle}</p>{t.skillList.map((skill) => <span key={skill}><Check />{skill}</span>)}</div>
          </div>
        </div>
      </section>

      <section className="approach-section section-pad">
        <div className="approach-heading reveal"><p className="section-eyebrow">{t.approachEyebrow}</p><h2>{t.approachTitle}</h2></div>
        <div className="steps">
          {t.approach.map(([number, title, description], index) => (
            <article className="step reveal" style={{ '--delay': `${index * 80}ms` } as React.CSSProperties} key={number}>
              <span>{number}</span><div className="step-icon">{index === 0 ? <Heart /> : index === 1 ? <Target /> : index === 2 ? <Sparkles /> : <ArrowUpRight />}</div><h3>{title}</h3><p>{description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="contact-section section-pad" id="contacto">
        <div className="contact-copy reveal">
          <p className="section-eyebrow">{t.contactEyebrow}</p><h2>{t.contactTitle}</h2><p>{t.contactIntro}</p>
          <div className="direct-contact"><p>{t.direct}</p><a href="https://wa.me/5493516215635" target="_blank" rel="noreferrer"><MessageCircle />+54 9 351 621-5635</a><a href="mailto:lgabryelah@gmail.com"><Send />lgabryelah@gmail.com</a></div>
          <small>{t.response}</small>
        </div>
        <div className="contact-card reveal">
          <form onSubmit={submitContact}>
            <div className="form-row"><label>{t.name}<Input required name="name" placeholder={t.namePh} /></label><label>{t.email}<Input required type="email" name="email" placeholder={t.emailPh} /></label></div>
            <label>{t.brand}<Input name="brand" placeholder={t.brandPh} /></label>
            <label>{t.message}<Textarea required name="message" placeholder={t.messagePh} /></label>
            <Button type="submit" size="lg" className="form-submit">{t.send}<ArrowUpRight /></Button>
            {sent && <output className="form-success"><Check />{t.sent}</output>}
          </form>
          <div className="contact-photo"><img src="/images/laura-04.webp" alt="Laura González" width="768" height="1024" loading="lazy" decoding="async" /></div>
        </div>
      </section>

      <footer>
        <div className="footer-brand"><span>LG</span><div><strong>Laura González</strong><small>{t.footer}</small></div></div>
        <div className="footer-socials"><a className="linkedin-mark" href="https://www.linkedin.com/in/laura-gonz%C3%A1lez-09bb7a380/" target="_blank" rel="noreferrer" aria-label="LinkedIn">in</a><a href="https://wa.me/5493516215635" target="_blank" rel="noreferrer" aria-label="WhatsApp"><MessageCircle /></a><a href="#inicio" aria-label="Volver arriba"><ArrowUpRight /></a></div>
        <p>© {new Date().getFullYear()} Laura González. {t.rights}</p>
      </footer>
    </main>
  );
}
