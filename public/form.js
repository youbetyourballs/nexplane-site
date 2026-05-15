// Google Apps Script web app URL — replace with your deployed script URL
// See README.md for setup instructions
const APPS_SCRIPT_URL = window.NEXPLANE_FORM_ENDPOINT || 'https://script.google.com/macros/s/AKfycbwp191RM2gkcV6Y1lPeJaurbdFRLhY9u81UY3zUk_bBflov32b60PwhTNQcBI-67VKYig/exec';

document.getElementById('interest-form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const btn = document.getElementById('submit-btn');
  const btnText = document.getElementById('btn-text');
  const btnSpinner = document.getElementById('btn-spinner');
  const success = document.getElementById('form-success');
  const error = document.getElementById('form-error');

  // Reset state
  success.style.display = 'none';
  error.style.display = 'none';
  btn.disabled = true;
  btnText.style.display = 'none';
  btnSpinner.style.display = 'inline';

  const data = {
    first_name:  this.first_name.value.trim(),
    last_name:   this.last_name.value.trim(),
    email:       this.email.value.trim(),
    company:     this.company.value.trim(),
    role:        this.role.value,
    fleet_size:  this.fleet_size.value,
    pain_point:  this.pain_point.value.trim(),
    submitted_at: new Date().toISOString(),
    source:      document.referrer || 'direct',
  };

  try {
    if (!APPS_SCRIPT_URL) {
      // Dev fallback — log to console
      console.log('Form data (no endpoint configured):', data);
      throw new Error('NEXPLANE_FORM_ENDPOINT not set');
    }

    const resp = await fetch(APPS_SCRIPT_URL, {
      method: 'POST',
      // Apps Script requires no-cors for cross-origin POSTs without CORS headers
      mode: 'no-cors',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });

    // no-cors response is opaque — we assume success if no network error
    success.style.display = 'block';
    this.reset();
  } catch (err) {
    console.error('Form submit error:', err);
    error.style.display = 'block';
  } finally {
    btn.disabled = false;
    btnText.style.display = 'inline';
    btnSpinner.style.display = 'none';
  }
});
