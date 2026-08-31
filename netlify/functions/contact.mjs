const json = (body, status = 200) => Response.json(body, { status });

function textField(form, name, maxLength, required = false) {
  const value = form.get(name);
  if (typeof value !== 'string') return required ? null : '';
  const normalized = value.trim();
  if ((required && !normalized) || normalized.length > maxLength) return null;
  return normalized;
}

async function contact(request, context) {
  if (request.method !== 'POST') return json({ error: 'Method not allowed' }, 405);

  try {
    const form = await request.formData();

    // Silently accept honeypot submissions without storing them.
    if (textField(form, 'bot-field', 200)) return json({ ok: true });

    const name = textField(form, 'name', 100, true);
    const email = textField(form, 'email', 254, true);
    const brand = textField(form, 'brand', 120);
    const message = textField(form, 'message', 5000, true);
    const language = textField(form, 'language', 2) === 'en' ? 'en' : 'es';
    const token = textField(form, 'cf-turnstile-response', 2048, true);

    if (!name || !email || !message || !token || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return json({ error: 'Invalid form submission' }, 400);
    }

    const secret = process.env.TURNSTILE_SECRET_KEY;
    if (!secret) return json({ error: 'Security verification is not configured' }, 503);

    const verificationBody = new URLSearchParams({ secret, response: token });
    if (context?.ip) verificationBody.set('remoteip', context.ip);

    const verificationResponse = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: verificationBody,
      signal: AbortSignal.timeout(8000),
    });
    const verification = await verificationResponse.json();

    if (!verificationResponse.ok || !verification.success || verification.action !== 'contact') {
      return json({ error: 'Security verification failed' }, 422);
    }

    const submission = new URLSearchParams({
      'form-name': 'contact',
      name,
      email,
      brand: brand ?? '',
      message,
      language,
    });
    const formEndpoint = new URL('/', request.url);
    const submissionResponse = await fetch(formEndpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: submission,
      redirect: 'manual',
      signal: AbortSignal.timeout(8000),
    });

    if (!submissionResponse.ok && ![301, 302, 303].includes(submissionResponse.status)) {
      return json({ error: 'Form delivery failed' }, 502);
    }

    return json({ ok: true });
  } catch {
    return json({ error: 'Unable to process the form' }, 500);
  }
}

export default contact;

export const config = {
  path: '/api/contact',
};
