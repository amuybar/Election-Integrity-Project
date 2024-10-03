// Example for creating a bar chart for presidential results
const ctx = document.getElementById('presidential-results-chart').getContext('2d');
const presidentialResultsChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Candidate A', 'Candidate B', 'Candidate C'],
        datasets: [{
            label: '# of Votes',
            data: [12000, 15000, 8000],
            backgroundColor: ['#3498db', '#2ecc71', '#e74c3c']
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
