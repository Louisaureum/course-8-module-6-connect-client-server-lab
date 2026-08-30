document.addEventListener('DOMContentLoaded', () => {
    // --- Fetch and display existing events ---
    fetch('http://localhost:5000/events')
        .then(response => response.json())
        .then(events => {
            events.forEach(renderEvent);
        })
        .catch(error => console.error('Error fetching events:', error));

    // --- Handle form submission ---
    const form = document.querySelector('form');
    const titleInput = document.querySelector('#title');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const title = titleInput.value.trim();
        if (!title) {
            alert('Please enter an event title.');
            return;
        }

        fetch('http://localhost:5000/events', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title })
        })
        .then(response => {
            if (!response.ok) {
                // Parse error message from server
                return response.json().then(err => { throw new Error(err.error || 'Server error'); });
            }
            return response.json();
        })
        .then(newEvent => {
            renderEvent(newEvent);
            form.reset();   // clear the input field
        })
        .catch(error => console.error('Error adding event:', error));
    });

    // --- Helper function to add an event to the list ---
    function renderEvent(event) {
        const li = document.createElement('li');
        li.textContent = event.title;
        li.dataset.id = event.id;   // store id for future use (optional)
        document.querySelector('#event-list').appendChild(li);
    }
});