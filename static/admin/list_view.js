document.addEventListener('DOMContentLoaded', function() {
    // Search Functionality
    const searchInput = document.getElementById('searchInput');
    const listItems = document.querySelectorAll('.list-item');

    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            
            listItems.forEach(item => {
                const name = item.dataset.name;
                if (name.includes(searchTerm)) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    }

    // Modal Handling
    const editModal = document.getElementById('editModal');
    const deleteModal = document.getElementById('deleteModal');
    const editButtons = document.querySelectorAll('.edit-btn');
    const deleteButtons = document.querySelectorAll('.delete-btn');
    const closeButtons = document.querySelectorAll('.close-modal');
    const cancelButtons = document.querySelectorAll('.cancel-btn');
    let currentItemId = null;

    // Edit Modal Functions
    function openEditModal(id) {
        currentItemId = id;
        // Fetch student data
        fetch(`/get-student/${id}/`)
            .then(response => response.json())
            .then(data => {
                const form = editModal.querySelector('form');
                form.querySelector('[name="name"]').value = data.name;
                form.querySelector('[name="address"]').value = data.address;
                form.querySelector('[name="age"]').value = data.age;
                form.querySelector('[name="phone_number"]').value = data.phone_number;
            });
        editModal.classList.add('active');
    }

    // Delete Modal Functions
    function openDeleteModal(id) {
        currentItemId = id;
        deleteModal.classList.add('active');
    }

    function closeModals() {
        editModal.classList.remove('active');
        deleteModal.classList.remove('active');
        currentItemId = null;
    }

    // Event Listeners
    editButtons.forEach(btn => {
        btn.addEventListener('click', () => openEditModal(btn.dataset.id));
    });

    deleteButtons.forEach(btn => {
        btn.addEventListener('click', () => openDeleteModal(btn.dataset.id));
    });

    closeButtons.forEach(btn => {
        btn.addEventListener('click', closeModals);
    });

    cancelButtons.forEach(btn => {
        btn.addEventListener('click', closeModals);
    });

    // Handle edit form submission
    const editForm = document.getElementById('editForm');
    if (editForm) {
        editForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);

            fetch(`/edit-student/${currentItemId}/`, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Update the UI
                    const item = document.querySelector(`.list-item[data-id="${currentItemId}"]`);
                    item.querySelector('.item-details h3').textContent = formData.get('name');
                    item.querySelector('.item-details p').textContent = formData.get('address');
                    item.querySelector('.item-secondary span:last-child').textContent = `Age: ${formData.get('age')}`;
                    item.querySelector('.item-secondary span:first-child').textContent = formData.get('phone_number');
                    
                    // Show success message
                    showMessage('Student updated successfully', 'success');
                    closeModals();
                } else {
                    showMessage('Error updating student', 'error');
                }
            });
        });
    }

    // Handle delete confirmation
    const deleteConfirmBtn = document.querySelector('.delete-confirm-btn');
    if (deleteConfirmBtn) {
        deleteConfirmBtn.addEventListener('click', function() {
            fetch(`/delete-student/${currentItemId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Remove the item from UI
                    const item = document.querySelector(`.list-item[data-id="${currentItemId}"]`);
                    item.remove();
                    showMessage('Student deleted successfully', 'success');
                    closeModals();
                } else {
                    showMessage('Error deleting student', 'error');
                }
            });
        });
    }

    // Message System
    function showMessage(message, type) {
        const container = document.querySelector('.message-container');
        const messageHTML = `
            <div class="message-item ${type}">
                <i class='bx ${type === 'success' ? 'bx-check-circle' : 'bx-error-circle'}'></i>
                <span>${message}</span>
                <button class="close-btn" aria-label="Close">
                    <i class='bx bx-x'></i>
                </button>
            </div>
        `;
        container.insertAdjacentHTML('beforeend', messageHTML);
        
        const newMessage = container.lastElementChild;
        setTimeout(() => {
            newMessage.classList.add('removing');
            setTimeout(() => newMessage.remove(), 300);
        }, 3000);

        // Add close button functionality
        newMessage.querySelector('.close-btn').addEventListener('click', () => {
            newMessage.classList.add('removing');
            setTimeout(() => newMessage.remove(), 300);
        });
    }
}); 