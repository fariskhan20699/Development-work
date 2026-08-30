// Realistic-ish drifting starfield with parallax, twinkle and occasional shooting stars.
(function () {
  const canvas = document.createElement('canvas');
  canvas.id = 'starfield';
  document.body.prepend(canvas);
  const ctx = canvas.getContext('2d');

  let w, h, dpr;
  let stars = [];
  let shootingStars = [];

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = window.innerWidth;
    h = window.innerHeight;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.width = w + 'px';
    canvas.style.height = h + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    buildStars();
  }

  function buildStars() {
    const count = Math.floor((w * h) / 3200);
    stars = [];
    for (let i = 0; i < count; i++) {
      const layer = Math.random();
      stars.push({
        x: Math.random() * w,
        y: Math.random() * h,
        r: layer < 0.7 ? Math.random() * 0.9 + 0.3 : Math.random() * 1.6 + 0.8,
        baseAlpha: Math.random() * 0.6 + 0.3,
        twinkleSpeed: Math.random() * 0.02 + 0.005,
        twinklePhase: Math.random() * Math.PI * 2,
        driftSpeed: (layer < 0.7 ? 0.006 : 0.018) * (Math.random() * 0.6 + 0.7),
        hue: Math.random() < 0.15 ? (Math.random() < 0.5 ? 200 : 30) : null
      });
    }
  }

  function maybeSpawnShootingStar() {
    if (Math.random() < 0.004 && shootingStars.length < 2) {
      const startX = Math.random() * w * 0.6 + w * 0.2;
      shootingStars.push({
        x: startX,
        y: -10,
        vx: -3 - Math.random() * 2,
        vy: 4 + Math.random() * 2,
        life: 0,
        maxLife: 60 + Math.random() * 20
      });
    }
  }

  let t = 0;
  function draw() {
    t += 1;
    ctx.clearRect(0, 0, w, h);

    // subtle nebula glow blobs
    const isLight = document.documentElement.dataset.theme === 'light';
    if (!isLight) {
      const g1 = ctx.createRadialGradient(w * 0.75, h * 0.15, 0, w * 0.75, h * 0.15, w * 0.5);
      g1.addColorStop(0, 'rgba(125,211,252,0.06)');
      g1.addColorStop(1, 'rgba(125,211,252,0)');
      ctx.fillStyle = g1;
      ctx.fillRect(0, 0, w, h);

      const g2 = ctx.createRadialGradient(w * 0.15, h * 0.8, 0, w * 0.15, h * 0.8, w * 0.4);
      g2.addColorStop(0, 'rgba(167,139,250,0.05)');
      g2.addColorStop(1, 'rgba(167,139,250,0)');
      ctx.fillStyle = g2;
      ctx.fillRect(0, 0, w, h);
    }

    for (const s of stars) {
      s.y += s.driftSpeed;
      if (s.y > h + 2) s.y = -2;
      const twinkle = Math.sin(t * s.twinkleSpeed + s.twinklePhase) * 0.35 + 0.65;
      const alpha = isLight ? s.baseAlpha * twinkle * 0.35 : s.baseAlpha * twinkle;
      ctx.beginPath();
      ctx.fillStyle = s.hue
        ? `hsla(${s.hue}, 80%, 80%, ${alpha})`
        : `rgba(255,255,255,${alpha})`;
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fill();
    }

    maybeSpawnShootingStar();
    shootingStars.forEach((s) => {
      s.x += s.vx;
      s.y += s.vy;
      s.life += 1;
      const progress = s.life / s.maxLife;
      const alpha = Math.max(0, 1 - progress) * 0.8;
      const grad = ctx.createLinearGradient(s.x, s.y, s.x - s.vx * 8, s.y - s.vy * 8);
      grad.addColorStop(0, `rgba(255,255,255,${alpha})`);
      grad.addColorStop(1, 'rgba(255,255,255,0)');
      ctx.strokeStyle = grad;
      ctx.lineWidth = 1.6;
      ctx.beginPath();
      ctx.moveTo(s.x, s.y);
      ctx.lineTo(s.x - s.vx * 8, s.y - s.vy * 8);
      ctx.stroke();
    });
    shootingStars = shootingStars.filter((s) => s.life < s.maxLife && s.y < h + 20);

    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', resize);
  resize();

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!prefersReducedMotion) {
    requestAnimationFrame(draw);
  } else {
    draw();
  }
})();
