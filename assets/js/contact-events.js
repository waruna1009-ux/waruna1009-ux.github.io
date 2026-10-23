// Count contact intent, not confirmed leads. Never send form values to analytics.
document.addEventListener('click', function (event) {
  var link = event.target.closest && event.target.closest('a[href]');
  if (!link || typeof window.clarity !== 'function') return;
  var href = link.getAttribute('href');
  if (href.indexOf('https://wa.me/') === 0) window.clarity('event', 'whatsapp_click');
  if (href.indexOf('mailto:') === 0) window.clarity('event', 'email_click');
});
