// Wires up the Normal / Developer Mode buttons, persists the choice
// in localStorage, and keeps the buttons' active state in sync.
const root = document.documentElement;
const buttons = document.querySelectorAll('.mode-btn');

function setActiveButton(mode) {
  buttons.forEach((btn) => {
    btn.classList.toggle('active', btn.dataset.mode === mode);
  });
}

setActiveButton(root.getAttribute('data-theme') || 'normal');

buttons.forEach((btn) => {
  btn.addEventListener('click', () => {
    const mode = btn.dataset.mode;
    root.setAttribute('data-theme', mode);
    localStorage.setItem('site-theme', mode);
    setActiveButton(mode);
  });
});
