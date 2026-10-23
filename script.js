document.querySelectorAll('[data-layer]').forEach((button) => {
  button.addEventListener('click', () => {
    const isActive = button.getAttribute('aria-pressed') === 'true';
    button.setAttribute('aria-pressed', String(!isActive));
    document.querySelector('.anatomy-panel').classList.toggle(`hide-${button.dataset.layer}`, isActive);
  });
});
