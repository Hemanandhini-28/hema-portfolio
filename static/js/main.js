const navToggle = document.querySelector('.nav-toggle');
const siteNav = document.querySelector('.site-nav');
const form = document.querySelector('#contactForm');
const formResponse = document.querySelector('#formResponse');

navToggle?.addEventListener('click', () => {
    siteNav?.classList.toggle('active');
});

form?.addEventListener('submit', event => {
    event.preventDefault();
    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const message = form.message.value.trim();

    if (!name || !email || !message) {
        formResponse.textContent = 'Please fill in all fields.';
        return;
    }

    formResponse.textContent = `Thanks, ${name}! Your message is ready.`;
    form.reset();
});
