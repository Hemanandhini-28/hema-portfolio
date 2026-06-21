const menuToggle = document.getElementById('menu-toggle');
const mobileNav = document.getElementById('mobile-nav');
const header = document.getElementById('site-header');

menuToggle?.addEventListener('click', () => {
  mobileNav?.classList.toggle('hidden');
});

window.addEventListener('scroll', () => {
  if (window.scrollY > 30) {
    header?.classList.add('scrolled');
  } else {
    header?.classList.remove('scrolled');
  }
});

function scrollToSection(id) {
  const section = document.getElementById(id);
  if (!section) return;
  section.scrollIntoView({ behavior: 'smooth', block: 'start' });
  mobileNav?.classList.add('hidden');
}

window.scrollToSection = scrollToSection;

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-fade-up');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 },
);

document.querySelectorAll('[data-reveal]').forEach((el) => observer.observe(el));
