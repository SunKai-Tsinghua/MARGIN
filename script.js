document.querySelectorAll('[data-layer]').forEach((button) => {
  button.addEventListener('click', () => {
    const isActive = button.getAttribute('aria-pressed') === 'true';
    button.setAttribute('aria-pressed', String(!isActive));
    document.querySelector('.anatomy-panel').classList.toggle(`hide-${button.dataset.layer}`, isActive);
  });
});

const tabs = Array.from(document.querySelectorAll('[role="tab"]'));
function activateTab(selected, moveFocus = false) {
  tabs.forEach((tab) => {
    const active = tab === selected;
    tab.setAttribute('aria-selected', String(active));
    tab.tabIndex = active ? 0 : -1;
    document.getElementById(tab.getAttribute('aria-controls')).hidden = !active;
  });
  if (moveFocus) selected.focus();
}
tabs.forEach((tab, index) => {
  tab.addEventListener('click', () => activateTab(tab));
  tab.addEventListener('keydown', (event) => {
    let next;
    if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
    if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
    if (event.key === 'Home') next = 0;
    if (event.key === 'End') next = tabs.length - 1;
    if (next !== undefined) { event.preventDefault(); activateTab(tabs[next], true); }
  });
});

document.getElementById('copy-title').addEventListener('click', async () => {
  const title = document.querySelector('.paper-grid h2').textContent.trim();
  const status = document.getElementById('copy-status');
  try {
    await navigator.clipboard.writeText(title);
    status.textContent = 'Paper title copied.';
  } catch {
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(document.querySelector('.paper-grid h2'));
    selection.removeAllRanges();
    selection.addRange(range);
    status.textContent = 'Title selected. Press Ctrl+C or ⌘C to copy.';
  }
});
