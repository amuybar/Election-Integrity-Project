// Initialize the map
var map = L.map("map").setView([-1.286389, 36.817223], 7); // Set the initial view (latitude, longitude)

// Set the tile layer (OpenStreetMap in this case)
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
}).addTo(map);

// Retrieve incidents from the JSON script tag
var incidents = JSON.parse(
  document.getElementById("incidents-data").textContent
);

// Add markers for each incident
incidents.forEach(function (incident) {
  // Create a marker for each incident
  var marker = L.marker([incident.latitude, incident.longitude]).addTo(map);
  marker.bindPopup(
    "<strong>Incident ID:</strong> " +
      incident.id +
      "<br><strong>Description:</strong> " +
      incident.description
  );
});
