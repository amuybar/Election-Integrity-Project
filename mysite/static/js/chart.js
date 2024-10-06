// Function to create charts
function createChart(canvasId, labels, data) {
  const ctx = document.getElementById(canvasId).getContext("2d");
  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Votes",
          data: data,
          backgroundColor: "rgba(75, 192, 192, 0.6)",
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}

// Create charts for each position
function initCharts(positionResults) {
  positionResults.forEach((position) => {
    const labels = position.results.map((result) => result.candidate);
    const data = position.results.map((result) => result.votes);
    createChart(`${position.slug}-results-chart`, labels, data);
  });
}

// Initialize Mapbox map
function initMap(incidents) {
  mapboxgl.accessToken = "YOUR_MAPBOX_ACCESS_TOKEN";
  const map = new mapboxgl.Map({
    container: "incident-map",
    style: "mapbox://styles/mapbox/streets-v11",
    center: [36.8219, 1.2921], // Nairobi coordinates
    zoom: 6,
  });

  // Add markers for incidents
  incidents.forEach((incident) => {
    new mapboxgl.Marker()
      .setLngLat([incident.longitude, incident.latitude])
      .setPopup(
        new mapboxgl.Popup().setHTML(
          `<h3>${incident.incident_type}</h3><p>${incident.description}</p>`
        )
      )
      .addTo(map);
  });
}

// AJAX for dynamic filtering
document.getElementById("filter-form").addEventListener("submit", function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  fetch(`/reporting/filter-results/?${new URLSearchParams(formData)}`)
    .then((response) => response.json())
    .then((data) => {
      // Update the results section with the new data
      console.log(data);
    });
});

// Call initialization functions on page load
document.addEventListener("DOMContentLoaded", function () {
  const positionResults = JSON.parse(
    document.getElementById("positionResultsData").textContent
  );
  const incidents = JSON.parse(
    document.getElementById("incidentsData").textContent
  );

  initCharts(positionResults);
  initMap(incidents);
});
