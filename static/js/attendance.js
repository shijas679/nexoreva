// Sliding Pill Navigation JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Get navigation elements
    const navLinks = document.getElementById('navLinks');
    const navItems = document.querySelectorAll('.nav-link');

    // Only proceed if navigation elements exist
    if (!navLinks || navItems.length === 0) return;

    // Handle navigation clicks
    navItems.forEach(link => {
        link.addEventListener('click', (e) => {
            // Don't prevent default for actual navigation - let Django handle routing
            const targetNav = link.getAttribute('data-nav');
            if (targetNav) {
                setActive(targetNav);
            }
        });
    });

    // Function to set active navigation
    function setActive(activeNav) {
        // Update data attribute for CSS targeting
        navLinks.setAttribute('data-active', activeNav);
        
        // Update active classes
        navItems.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('data-nav') === activeNav) {
                link.classList.add('active');
            }
        });
    }

    // Optional: Add hover effects for smoother interaction
    navItems.forEach(link => {
        link.addEventListener('mouseenter', () => {
            const hoverNav = link.getAttribute('data-nav');
            if (hoverNav) {
                // You can add hover-specific styling here if needed
                link.style.transform = 'translateY(-2px)';
            }
        });
        
        link.addEventListener('mouseleave', () => {
            // Reset hover transform
            link.style.transform = '';
        });
    });

    // Initialize pill position based on current page
    // This will run when the page loads to set the correct initial position
    const activeLink = document.querySelector('.nav-link.active');
    if (activeLink) {
        const activeNav = activeLink.getAttribute('data-nav');
        if (activeNav) {
            setActive(activeNav);
        }
    }
});