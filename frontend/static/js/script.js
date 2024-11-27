const API_BASE_URL = "https://your-api-url.amazonaws.com";

async function fetchConcerts() {
    try {
        const response = await fetch(`${API_BASE_URL}/concerts`);
        const concerts = await response.json();
        renderConcerts(concerts);
    } catch (error) {
        console.error("Error fetching concerts:", error);
    }
}

function renderConcerts(concerts) {
    const concertContainer = document.getElementById("concert-list");
    concerts.forEach(concert => {
        const concertItem = document.createElement("div");
        concertItem.innerHTML = `
            <h3>${concert.name}</h3>
            <p>${concert.date}</p>
            <p>${concert.location}</p>
            <button onclick="bookSeat('${concert.id}')">Reserve Seat</button>
        `;
        concertContainer.appendChild(concertItem);
    });
}

async function bookSeat(concertId) {
    const userId = localStorage.getItem("userId");
    if (!userId) {
        alert("Please log in first!");
        return;
    }
    try {
        const response = await fetch(`${API_BASE_URL}/reservations`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ concertId, userId })
        });
        if (response.ok) {
            alert("Seat booked successfully!");
        } else {
            alert("Error booking seat.");
        }
    } catch (error) {
        console.error("Error booking seat:", error);
    }
}
