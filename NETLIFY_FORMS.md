# Configuración del formulario en Netlify

El formulario se registra con el nombre `contact` después del próximo despliegue.

1. En Netlify, abre el proyecto y entra en **Forms → Usage and configuration → Form detection**.
2. Confirma que **Form detection** esté activado y vuelve a desplegar el sitio si acabas de activarlo.
3. Después del despliegue, envía una consulta de prueba desde la web. Aparecerá en **Forms → contact**.
4. Para recibir cada consulta por correo, entra en **Project configuration → Notifications → Emails and webhooks → Form submission notifications**.
5. Elige **Add notification → Email notification**, selecciona el formulario `contact` e introduce el correo de Laura.

Netlify guardará nombre, email, marca/proyecto, mensaje e idioma. El campo `email` permite responder directamente a la persona desde la notificación. WhatsApp continúa disponible como contacto alternativo.
