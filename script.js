// Theme Toggle Logic
const themeBtn = document.getElementById('theme-toggle');
themeBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const targetTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', targetTheme);
});

// Tab Switcher Logic
function switchCategory(catId) {
    const contents = document.querySelectorAll('.category-content');
    const tabs = document.querySelectorAll('.tab-link');

    // Toggle Content Visibility
    contents.forEach(content => {
        content.classList.remove('active');
        if(content.id === catId) {
            setTimeout(() => content.classList.add('active'), 50);
        }
    });

    // Toggle Tab Active State
    tabs.forEach(tab => {
        // Compare tab text to catId (e.g., 'experience' matches 'experience')
        const isActive = tab.getAttribute('onclick').includes(catId);
        tab.classList.toggle('active', isActive);
    });
}

// Accordion Logic
function toggleAccordion(header) {
    const item = header.parentElement;
    const wasOpen = item.classList.contains('open');

    // Optional: Close all other accordion items when opening a new one
    document.querySelectorAll('.accordion-item').forEach(el => el.classList.remove('open'));

    if (!wasOpen) {
        item.classList.add('open');
    }
}