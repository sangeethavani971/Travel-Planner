function $(sel, parent=document){ return parent.querySelector(sel); }

function changeDuration(delta){
    const el = $('#duration');
    const v = Math.max(1, Number(el.value || 1) + delta);
    el.value = v;
}

function scrollToForm(){
    document.getElementById('trip-planning-form').scrollIntoView({behavior: 'smooth'});
}

document.addEventListener('DOMContentLoaded', () => {
    const form = $('#travelForm');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const destination = $('#destination').value;
        const start_date = $('#startDate').value;
        const duration = Number($('#duration').value);
        const budget = document.querySelector('input[name="budget"]:checked').value;

        const preferred_transport = Array.from(document.querySelectorAll('input[name="transport"]:checked')).map(i=>i.value);
        const preferred_stay = Array.from(document.querySelectorAll('input[name="stay"]:checked')).map(i=>i.value);
        const interests = Array.from(document.querySelectorAll('input[name="interest"]:checked')).map(i=>i.value);

        const payload = { destination, start_date, duration, budget_level: budget, preferred_transport, preferred_stay, interests };

        const res = await fetch('/api/generate', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload) });
        const data = await res.json();
        if (!res.ok){ alert(data.error || 'Error generating itinerary'); return; }

        renderItinerary(data);
    });
});

function renderItinerary(data){
    document.getElementById('trip-planning-form').style.display = 'none';
    const disp = document.getElementById('itinerary-display');
    disp.style.display = 'block';
    document.getElementById('itineraryDestination').textContent = data.summary.destination;
    document.getElementById('summaryDates').textContent = data.summary.start_date;
    document.getElementById('summaryDuration').textContent = data.summary.duration;
    document.getElementById('summaryBudget').textContent = data.summary.budget_level;
    document.getElementById('summaryTotalCost').textContent = data.summary.total_estimated_cost;
    document.getElementById('summaryTransport').textContent = data.summary.preferred_transport;
    document.getElementById('summaryStay').textContent = data.summary.preferred_stay;
    document.getElementById('summaryInterests').textContent = data.summary.interests;

    const container = document.getElementById('day-by-day-itinerary');
    container.innerHTML = '';
    data.itinerary_details.forEach(day => {
        const card = document.createElement('div');
        card.className = 'day-card curve-box';
        card.innerHTML = `<h4>Day ${day.day} — ${day.date}</h4><p><strong>Location:</strong> ${day.location}</p>`;
        if (day.activities && day.activities.length){
            const list = document.createElement('ul');
            day.activities.forEach(a=>{ list.innerHTML += `<li>${a.name} — ${a.estimated_cost} (est.)</li>` });
            card.appendChild(list);
        }
        container.appendChild(card);
    });

    // Budget chart
    const ctx = document.getElementById('budgetChart').getContext('2d');
    new Chart(ctx, { type: 'doughnut', data: { labels: ['Accommodation','Transport','Activities'], datasets:[{ data:[1,1,1], backgroundColor:['#4e79a7','#f28e2b','#e15759'] }] }, options:{ responsive:true } });
}
