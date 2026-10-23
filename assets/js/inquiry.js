'use strict';
// Keep visitor-entered product names as text; never insert URL values as HTML.
(function () {
  var product = document.getElementById('product');
  var requested = new URLSearchParams(window.location.search).get('product');
  if (product && requested) product.value = requested.slice(0, 160);
}());

async function handleSubmit(event) {
  event.preventDefault();
  var form = document.getElementById('inquiry-form');
  var button = form.querySelector('.btn-submit');
  var error = document.getElementById('form-error');
  var success = document.getElementById('form-success');
  if (button.disabled || !form.reportValidity()) return false;
  button.disabled = true;
  button.textContent = 'Sending...';
  error.hidden = true;
  var controller = new AbortController();
  var timer = setTimeout(function () { controller.abort(); }, 20000);
  try {
    var response = await fetch(form.action, {
      method: 'POST', body: new FormData(form),
      headers: { Accept: 'application/json' }, signal: controller.signal
    });
    var result = await response.json();
    // HTTP 200 alone does not establish service acceptance or mailbox delivery.
    if (!response.ok || (result.success !== true && result.success !== 'true')) {
      throw new Error('Service did not confirm acceptance');
    }
    form.style.display = 'none';
    success.style.display = 'block';
    if (typeof window.clarity === 'function') window.clarity('event', 'inquiry_form_accepted');
  } catch (failure) {
    error.hidden = false;
    if (typeof window.clarity === 'function') window.clarity('event', 'inquiry_form_error');
  } finally {
    clearTimeout(timer);
    button.disabled = false;
    button.textContent = 'Send Inquiry →';
  }
  return false;
}
