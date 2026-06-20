// ===== AOS INIT =====
document.addEventListener('DOMContentLoaded', () => {
  AOS.init({
    duration: 900,
    easing: 'ease-out-cubic',
    once: true,
    offset: 60,
  });

  // Vanilla Tilt on cards
  VanillaTilt.init(document.querySelectorAll('.card[data-tilt], [data-tilt]'), {
    max: 8,
    speed: 500,
    glare: true,
    'max-glare': 0.15,
  });
});

// ===== STICKY NAVBAR =====
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 60);
}, { passive: true });

// ===== SMOOTH SCROLL =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', e => {
    e.preventDefault();
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      window.scrollTo({ top: target.offsetTop - 80, behavior: 'smooth' });
    }
  });
});

// ===== ANIMATED COUNTERS =====
function animateCounter(el, target, suffix = '', duration = 2000) {
  let start = 0;
  const step = target / (duration / 16);
  const timer = setInterval(() => {
    start += step;
    if (start >= target) {
      start = target;
      clearInterval(timer);
    }
    el.textContent = Math.floor(start) + suffix;
  }, 16);
}

// Trigger counters when hero stats come into view
const heroSection = document.getElementById('hero');
if (heroSection) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(document.getElementById('stat-proyectos'), 3000, '+');
        animateCounter(document.getElementById('stat-roi'), 35, '%');
        animateCounter(document.getElementById('stat-dias'), 30, '');
        observer.disconnect();
      }
    });
  }, { threshold: 0.3 });
  observer.observe(heroSection);
}

// ===== FORM SUBMIT =====
function handleSubmit(e) {
  e.preventDefault();
  const btn = e.target.querySelector('.form-submit');
  btn.textContent = '✓ Mensaje Enviado';
  btn.style.background = '#22c55e';
  btn.style.boxShadow = '0 0 30px rgba(34,197,94,0.4)';
  btn.disabled = true;
  e.target.reset();
  setTimeout(() => {
    btn.innerHTML = 'Enviar Mensaje <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12h14M12 5l7 7-7 7"/></svg>';
    btn.style.background = '';
    btn.style.boxShadow = '';
    btn.disabled = false;
  }, 4000);
}

// ===== THEME TOGGLE (DARK/LIGHT MODE) =====
document.addEventListener('DOMContentLoaded', () => {
  const themeToggleBtn = document.getElementById('theme-toggle');
  const root = document.documentElement;

  // Check saved theme or system preference
  const savedTheme = localStorage.getItem('theme');
  const prefersLight = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches;

  if (savedTheme === 'light' || (!savedTheme && prefersLight)) {
    root.classList.add('light-mode');
    if (themeToggleBtn) themeToggleBtn.textContent = '☀️';
  }

  // Toggle theme on click
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      root.classList.toggle('light-mode');
      const isLight = root.classList.contains('light-mode');
      
      themeToggleBtn.textContent = isLight ? '☀️' : '🌙';
      localStorage.setItem('theme', isLight ? 'light' : 'dark');
    });
  }

  // ===== HAMBURGER MENU =====
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('nav-links');

  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('open');
      hamburger.classList.toggle('active', isOpen);
      hamburger.setAttribute('aria-expanded', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close menu when clicking a nav link
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        hamburger.classList.remove('active');
        hamburger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });

    // Close on Escape key
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && navLinks.classList.contains('open')) {
        navLinks.classList.remove('open');
        hamburger.classList.remove('active');
        hamburger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
  }
});
