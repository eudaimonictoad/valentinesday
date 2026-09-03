// Renders every HTML file in ./html to a Letter-size PDF in ./pdf
// Usage: node render.js [name ...]   (no args = all)
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const dir = path.join(__dirname, 'html');
  let files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));
  const only = process.argv.slice(2);
  if (only.length) files = files.filter(f => only.some(o => f.startsWith(o)));
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage();
  for (const f of files) {
    await page.goto('file://' + path.join(dir, f), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const out = path.join(__dirname, 'pdf', f.replace(/\.html$/, '.pdf'));
    await page.pdf({ path: out, format: 'Letter', printBackground: true, preferCSSPageSize: true, margin: {top:0,right:0,bottom:0,left:0} });
    console.log('rendered', out);
  }
  await browser.close();
})();
