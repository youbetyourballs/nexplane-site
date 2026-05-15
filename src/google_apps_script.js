/**
 * Nexplane.ai — Interest Form Handler
 *
 * SETUP INSTRUCTIONS (one-time, 10 minutes):
 *
 * 1. Go to https://sheets.google.com → create a new spreadsheet
 *    Name it "Nexplane Interest Form Responses"
 *    Add these headers in row 1:
 *    Timestamp | First Name | Last Name | Email | Company | Role | Fleet Size | Pain Point | Source
 *
 * 2. Go to Extensions → Apps Script
 *    Paste this entire file into the editor, replacing any existing code
 *    Save it (Ctrl+S)
 *
 * 3. Click Deploy → New deployment
 *    Type: Web app
 *    Execute as: Me (your Google account)
 *    Who has access: Anyone
 *    Click Deploy → Authorize → Copy the web app URL
 *
 * 4. In your website's index.html, add before </body>:
 *    <script>window.NEXPLANE_FORM_ENDPOINT = 'PASTE_YOUR_URL_HERE';</script>
 *
 * 5. Test by submitting the form — check the spreadsheet for a new row.
 *
 * Optional: set up email notifications in the spreadsheet via
 * Extensions → Apps Script → Triggers → Add trigger on form submit.
 */

const SHEET_NAME = 'Responses'; // tab name in your spreadsheet

function doPost(e) {
  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = ss.getSheetByName(SHEET_NAME);

    // Create sheet with headers if it doesn't exist
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow([
        'Timestamp',
        'First Name',
        'Last Name',
        'Email',
        'Company',
        'Role',
        'Fleet Size',
        'Pain Point',
        'Source',
        'Submitted At',
      ]);
      // Freeze header row and bold it
      sheet.setFrozenRows(1);
      sheet.getRange(1, 1, 1, 10).setFontWeight('bold');
      sheet.setColumnWidth(8, 400); // Pain point column wider
    }

    const data = JSON.parse(e.postData.contents);

    sheet.appendRow([
      new Date(),                            // Timestamp (server time)
      data.first_name   || '',
      data.last_name    || '',
      data.email        || '',
      data.company      || '',
      data.role         || '',
      data.fleet_size   || '',
      data.pain_point   || '',
      data.source       || 'direct',
      data.submitted_at || '',
    ]);

    // Optional: send yourself a notification email
    _sendNotificationEmail(data);

    return ContentService
      .createTextOutput(JSON.stringify({ success: true }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    console.error('Form handler error:', err);
    return ContentService
      .createTextOutput(JSON.stringify({ success: false, error: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function _sendNotificationEmail(data) {
  // Replace with your email address — or remove this block to skip notifications
  const NOTIFY_EMAIL = 'john.o.terrill@gmail.com';

  try {
    MailApp.sendEmail({
      to: NOTIFY_EMAIL,
      subject: `New Nexplane interest: ${data.first_name} ${data.last_name} @ ${data.company}`,
      htmlBody: `
        <h2>New Early Access Request</h2>
        <table style="border-collapse:collapse;font-family:sans-serif;font-size:14px;">
          <tr><td style="padding:6px 12px;color:#666">Name</td><td style="padding:6px 12px"><b>${data.first_name} ${data.last_name}</b></td></tr>
          <tr><td style="padding:6px 12px;color:#666">Email</td><td style="padding:6px 12px"><a href="mailto:${data.email}">${data.email}</a></td></tr>
          <tr><td style="padding:6px 12px;color:#666">Company</td><td style="padding:6px 12px">${data.company}</td></tr>
          <tr><td style="padding:6px 12px;color:#666">Role</td><td style="padding:6px 12px">${data.role}</td></tr>
          <tr><td style="padding:6px 12px;color:#666">Fleet size</td><td style="padding:6px 12px">${data.fleet_size}</td></tr>
          <tr><td style="padding:6px 12px;color:#666">Pain point</td><td style="padding:6px 12px;max-width:400px">${data.pain_point}</td></tr>
        </table>
      `,
    });
  } catch (e) {
    // Non-fatal — log but don't fail the submission
    console.warn('Email notification failed:', e.message);
  }
}

// GET handler for health check
function doGet() {
  return ContentService
    .createTextOutput(JSON.stringify({ status: 'ok', service: 'nexplane-interest-form' }))
    .setMimeType(ContentService.MimeType.JSON);
}
