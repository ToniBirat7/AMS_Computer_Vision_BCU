document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registrationForm');
    const formSteps = document.querySelectorAll('.form-step');
    const progressSteps = document.querySelectorAll('.progress-step');
    let currentStep = 1;

    // Guidelines Carousel
    const carousel = {
        container: document.querySelector('.guidelines-carousel'),
        cards: document.querySelectorAll('.guideline-card'),
        dots: document.querySelector('.carousel-dots'),
        prevBtn: document.querySelector('.prev-btn'),
        nextBtn: document.querySelector('.next-btn'),
        currentIndex: 0,
        autoPlayInterval: null,

        init() {
            // Create dots
            this.cards.forEach((_, index) => {
                const dot = document.createElement('div');
                dot.className = `dot ${index === 0 ? 'active' : ''}`;
                dot.addEventListener('click', () => this.goToCard(index));
                this.dots.appendChild(dot);
            });

            // Add button listeners
            this.prevBtn.addEventListener('click', () => this.prev());
            this.nextBtn.addEventListener('click', () => this.next());

            // Start autoplay
            this.startAutoPlay();

            // Pause autoplay on hover
            this.container.addEventListener('mouseenter', () => this.stopAutoPlay());
            this.container.addEventListener('mouseleave', () => this.startAutoPlay());
        },

        goToCard(index) {
            this.cards[this.currentIndex].classList.remove('active');
            this.dots.children[this.currentIndex].classList.remove('active');
            
            this.currentIndex = index;
            
            this.cards[this.currentIndex].classList.add('active');
            this.dots.children[this.currentIndex].classList.add('active');
        },

        next() {
            this.goToCard((this.currentIndex + 1) % this.cards.length);
        },

        prev() {
            this.goToCard((this.currentIndex - 1 + this.cards.length) % this.cards.length);
        },

        startAutoPlay() {
            this.autoPlayInterval = setInterval(() => this.next(), 5000);
        },

        stopAutoPlay() {
            clearInterval(this.autoPlayInterval);
        }
    };

    // Message System
    const messageSystem = {
        container: document.querySelector('.floating-messages-container'),
        maxMessages: 3,
        
        init() {
            if (!this.container) {
                this.container = document.createElement('div');
                this.container.className = 'floating-messages-container';
                document.body.appendChild(this.container);
            }
        },

        show(type, title, message, duration = 5000) {
            this.init();
            
            const messages = this.container.children;
            if (messages.length >= this.maxMessages) {
                messages[messages.length - 1].remove();
            }

            const messageEl = document.createElement('div');
            messageEl.className = `floating-message ${type}`;
            
            let icon = type === 'error' ? 'bx-x-circle' : 
                      type === 'success' ? 'bx-check-circle' : 'bx-error';

            messageEl.innerHTML = `
                <i class='bx ${icon}'></i>
                <div class="message-content">
                    <div class="message-title">${title}</div>
                    <div class="message-text">${message}</div>
                </div>
                <button class="close-btn">
                    <i class='bx bx-x'></i>
                </button>
                <div class="progress"></div>
            `;

            this.container.insertBefore(messageEl, this.container.firstChild);
            
            requestAnimationFrame(() => {
                messageEl.classList.add('show');
                messageEl.style.transform = 'translateX(0)';
                messageEl.style.opacity = '1';
            });

            const closeBtn = messageEl.querySelector('.close-btn');
            closeBtn.addEventListener('click', () => this.remove(messageEl));

            if (duration > 0) {
                setTimeout(() => this.remove(messageEl), duration);
            }
        },

        remove(messageEl) {
            messageEl.style.transform = 'translateX(120%)';
            messageEl.style.opacity = '0';
            setTimeout(() => messageEl.remove(), 500);
        },

        error(title, message) {
            this.show('error', title, message);
        },

        success(title, message) {
            this.show('success', title, message);
        },

        warning(title, message) {
            this.show('warning', title, message);
        }
    };

    // Form Navigation
    function goToStep(step) {
        formSteps.forEach(s => s.classList.remove('active'));
        progressSteps.forEach(s => s.classList.remove('active'));

        formSteps[step - 1].classList.add('active');
        for (let i = 0; i < step; i++) {
            progressSteps[i].classList.add('active');
        }
        currentStep = step;
    }

    // Form Validation
    function validateStep(step) {
        const currentStepEl = document.querySelector(`.form-step[data-step="${step}"]`);
        const inputs = currentStepEl.querySelectorAll('input[required]');
        let isValid = true;

        inputs.forEach(input => {
            if (!input.value) {
                const label = input.closest('.input-group').querySelector('label').textContent;
                messageSystem.error('Required Field', `${label} is required`);
                input.classList.add('error');
                isValid = false;
            } else {
                input.classList.remove('error');
            }
        });

        return isValid;
    }

    // Event Listeners
    document.querySelectorAll('.next-step-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            if (validateStep(currentStep)) {
                goToStep(currentStep + 1);
            }
        });
    });

    document.querySelectorAll('.prev-step-btn').forEach(btn => {
        btn.addEventListener('click', () => goToStep(currentStep - 1));
    });

    // Password Toggle
    document.querySelectorAll('.password-toggle').forEach(toggle => {
        toggle.addEventListener('click', function() {
            const input = this.previousElementSibling;
            const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
            input.setAttribute('type', type);
            this.classList.toggle('bx-hide');
            this.classList.toggle('bx-show');
        });
    });

    // Form Submit
    if (form) {
        form.addEventListener('submit', function(e) {
            const passwords = form.querySelectorAll('input[type="password"]');
            if (passwords[0].value !== passwords[1].value) {
                e.preventDefault();
                messageSystem.error('Password Error', 'Passwords do not match');
            }
        });
    }

    // Make messageSystem globally accessible
    window.messageSystem = messageSystem;

    // Initialize
    messageSystem.init();
    carousel.init();
}); 