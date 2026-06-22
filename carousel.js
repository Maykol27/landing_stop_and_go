/* ==========================
   CAROUSEL + LIGHTBOX ENGINE
   ========================== */
(function () {
  const AUTOPLAY_MS = 4000;

  const images = [
    { src: './assets/sobrenosotros.jpeg',                               cap: 'Módulo Café Gourmet — Vista Exterior' },
    { src: './assets/1WhatsApp Image 2026-06-11 at 6.03.51 PM.jpeg',    cap: 'Módulo Standard — Vista Frontal' },
    { src: './assets/WhatsApp Image 2026-06-11 at 8.27.36 PM.jpeg',     cap: 'Módulo Premium — Vista Nocturna' },
    { src: './assets/21WhatsApp Image 2026-06-11 at 10.52.11 PM.jpeg',  cap: 'Módulo Compact — Vista Lateral' },
    { src: './assets/express.jpeg',                                     cap: 'Módulo Express — Detalle Arquitectónico' },
    { src: './assets/4WhatsApp Image 2026-06-11 at 10.52.11 PM.jpeg',   cap: 'Módulo Mobility — Perspectiva' },
    { src: './assets/1WhatsApp Image 2026-06-11 at 6.02.25 PM.jpeg',    cap: 'Hub Comercial — Ambiente' },
    { src: './assets/WhatsApp Image 2026-06-11 at 5.58.38 PM.jpeg',     cap: 'Módulo Food — Vista Interior' },
  ];

  let current = 0;
  let autoTimer = null;
  let progressTimer = null;
  let progressStart = null;
  let lbIndex = 0;
  let isDragging = false, startX = 0, dragDist = 0;

  /* ---------- INIT ---------- */
  document.addEventListener('DOMContentLoaded', () => {
    buildDots();
    buildThumbs();
    attachArrows();
    attachDrag();
    goTo(0, false);
    startAutoplay();
  });

  /* ---------- BUILD DOTS ---------- */
  function buildDots() {
    const container = document.getElementById('galleryDots');
    if (!container) return;
    images.forEach((_, i) => {
      const btn = document.createElement('button');
      btn.className = 'sg-dot' + (i === 0 ? ' active' : '');
      btn.setAttribute('aria-label', `Ir a imagen ${i + 1}`);
      btn.addEventListener('click', () => { goTo(i); resetAutoplay(); });
      container.appendChild(btn);
    });
  }

  /* ---------- BUILD THUMBNAILS ---------- */
  function buildThumbs() {
    const container = document.getElementById('galleryThumbs');
    if (!container) return;
    images.forEach((img, i) => {
      const div = document.createElement('div');
      div.className = 'sg-thumb' + (i === 0 ? ' active' : '');
      const picture = document.createElement('img');
      picture.src = img.src;
      picture.alt = img.cap;
      picture.loading = 'lazy';
      div.appendChild(picture);
      div.addEventListener('click', () => { goTo(i); resetAutoplay(); });
      container.appendChild(div);
    });
  }

  /* ---------- ATTACH ARROWS ---------- */
  function attachArrows() {
    document.getElementById('galleryPrev')?.addEventListener('click', () => { move(-1); resetAutoplay(); });
    document.getElementById('galleryNext')?.addEventListener('click', () => { move(1); resetAutoplay(); });

    // Keyboard
    document.addEventListener('keydown', e => {
      if (document.getElementById('galleryLightbox')?.classList.contains('open')) return;
      if (e.key === 'ArrowLeft') { move(-1); resetAutoplay(); }
      if (e.key === 'ArrowRight') { move(1); resetAutoplay(); }
    });
  }

  /* ---------- DRAG / SWIPE ---------- */
  function attachDrag() {
    const carousel = document.querySelector('.sg-carousel');
    if (!carousel) return;

    const onStart = e => {
      isDragging = true;
      startX = e.type === 'touchstart' ? e.touches[0].clientX : e.clientX;
      dragDist = 0;
      stopAutoplay();
    };
    const onMove = e => {
      if (!isDragging) return;
      const x = e.type === 'touchmove' ? e.touches[0].clientX : e.clientX;
      dragDist = x - startX;
    };
    const onEnd = () => {
      if (!isDragging) return;
      isDragging = false;
      if (Math.abs(dragDist) > 60) move(dragDist < 0 ? 1 : -1);
      dragDist = 0;
      startAutoplay();
    };

    carousel.addEventListener('mousedown', onStart);
    carousel.addEventListener('touchstart', onStart, { passive: true });
    window.addEventListener('mousemove', onMove);
    // passive:true so touchmove never blocks vertical page scroll
    window.addEventListener('touchmove', e => {
      if (!isDragging) return;
      const x = e.touches[0].clientX;
      dragDist = x - startX;
    }, { passive: true });
    window.addEventListener('mouseup', onEnd);
    window.addEventListener('touchend', onEnd);
  }

  /* ---------- NAVIGATION ---------- */
  function move(dir) {
    goTo((current + dir + images.length) % images.length);
  }

  function goTo(index, animate = true) {
    const track = document.getElementById('galleryTrack');
    if (!track) return;

    // Update slides
    const slides = track.querySelectorAll('.sg-slide');
    slides.forEach((s, i) => s.classList.toggle('active', i === index));

    // Translate track
    track.style.transition = animate ? 'transform 0.7s cubic-bezier(0.25, 0.8, 0.25, 1)' : 'none';
    track.style.transform = `translateX(-${index * 100}%)`;

    // Update dots
    document.querySelectorAll('.sg-dot').forEach((d, i) => d.classList.toggle('active', i === index));

    // Update thumbs — scroll only the THUMB STRIP, never the page
    const thumbsContainer = document.getElementById('galleryThumbs');
    const thumbs = document.querySelectorAll('.sg-thumb');
    thumbs.forEach((t, i) => t.classList.toggle('active', i === index));
    if (thumbsContainer && thumbs[index]) {
      const thumb = thumbs[index];
      const containerLeft = thumbsContainer.scrollLeft;
      const containerWidth = thumbsContainer.clientWidth;
      const thumbLeft = thumb.offsetLeft;
      const thumbWidth = thumb.offsetWidth;
      // Only scroll the thumb strip container, not the page
      thumbsContainer.scrollTo({
        left: thumbLeft - containerWidth / 2 + thumbWidth / 2,
        behavior: 'smooth'
      });
    }

    current = index;
    resetProgress();
  }

  /* ---------- AUTOPLAY ---------- */
  function startAutoplay() {
    stopAutoplay();
    autoTimer = setInterval(() => move(1), AUTOPLAY_MS);
    startProgress();
  }

  function stopAutoplay() {
    clearInterval(autoTimer);
    clearAnimationFrame();
  }

  function resetAutoplay() {
    stopAutoplay();
    startAutoplay();
  }

  /* ---------- PROGRESS BAR ---------- */
  let rafId = null;
  function startProgress() {
    progressStart = performance.now();
    animateProgress();
  }

  function resetProgress() {
    clearAnimationFrame();
    const bar = document.getElementById('galleryProgress');
    if (bar) bar.style.width = '0%';
    progressStart = performance.now();
    animateProgress();
  }

  function animateProgress() {
    const bar = document.getElementById('galleryProgress');
    if (!bar) return;
    const elapsed = performance.now() - progressStart;
    const pct = Math.min((elapsed / AUTOPLAY_MS) * 100, 100);
    bar.style.width = pct + '%';
    if (pct < 100) rafId = requestAnimationFrame(animateProgress);
  }

  function clearAnimationFrame() {
    if (rafId) { cancelAnimationFrame(rafId); rafId = null; }
  }

  /* ---------- LIGHTBOX ---------- */
  window.openLightbox = function (index) {
    lbIndex = index;
    showLbImage(lbIndex);
    document.getElementById('galleryLightbox').classList.add('open');
    document.body.style.overflow = 'hidden';
    stopAutoplay();
  };

  function showLbImage(i) {
    const img = document.getElementById('galleryLbImg');
    const cap = document.getElementById('galleryLbCaption');
    if (img) { img.src = images[i].src; img.alt = images[i].cap; }
    if (cap) cap.textContent = images[i].cap;
    lbIndex = i;
  }

  function closeLightbox() {
    document.getElementById('galleryLightbox').classList.remove('open');
    document.body.style.overflow = '';
    startAutoplay();
  }

  document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('galleryLbBackdrop')?.addEventListener('click', closeLightbox);
    document.getElementById('galleryLbClose')?.addEventListener('click', closeLightbox);
    document.getElementById('galleryLbPrev')?.addEventListener('click', e => { e.stopPropagation(); showLbImage((lbIndex - 1 + images.length) % images.length); });
    document.getElementById('galleryLbNext')?.addEventListener('click', e => { e.stopPropagation(); showLbImage((lbIndex + 1) % images.length); });

    document.addEventListener('keydown', e => {
      const lb = document.getElementById('galleryLightbox');
      if (!lb?.classList.contains('open')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowLeft') showLbImage((lbIndex - 1 + images.length) % images.length);
      if (e.key === 'ArrowRight') showLbImage((lbIndex + 1) % images.length);
    });
  });

})();
