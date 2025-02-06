document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('studentSearchForm');
    const studentDetails = document.getElementById('studentDetails');
    const noResults = document.getElementById('noResults');
    let chart = null;

    // Handle search form submission
    searchForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const studentId = this.querySelector('input[name="student_id"]').value;
        
        try {
            const response = await fetch(`/get-student-report/${studentId}/`);
            const data = await response.json();

            if (response.ok) {
                displayStudentDetails(data);
                studentDetails.classList.remove('hidden');
                noResults.classList.add('hidden');
            } else {
                studentDetails.classList.add('hidden');
                noResults.classList.remove('hidden');
            }
        } catch (error) {
            console.error('Error:', error);
            studentDetails.classList.add('hidden');
            noResults.classList.remove('hidden');
        }
    });

    // Display student details
    function displayStudentDetails(data) {
        // Update profile info
        document.querySelector('.student-name').textContent = data.name;
        document.querySelector('.student-id').textContent = `ID: ${data.id}`;

        // Update course cards
        const progressGrid = document.querySelector('.progress-grid');
        progressGrid.innerHTML = data.courses.map(course => `
            <div class="course-card">
                <h3>${course.title}</h3>
                <div class="course-stats">
                    <p>Present: ${course.present_days}</p>
                    <p>Absent: ${course.absent_days}</p>
                    <p>Attendance: ${course.attendance_rate}%</p>
                </div>
            </div>
        `).join('');

        // Update attendance stats
        document.querySelector('.stat-item.present .stat-value').textContent = data.total_present;
        document.querySelector('.stat-item.absent .stat-value').textContent = data.total_absent;
        document.querySelector('.stat-item.percentage .stat-value').textContent = `${data.attendance_rate}%`;

        // Update chart
        updateAttendanceChart(data.monthly_attendance);
    }

    // Create/Update attendance chart
    function updateAttendanceChart(monthlyData) {
        const ctx = document.getElementById('monthlyAttendanceChart').getContext('2d');
        
        if (chart) {
            chart.destroy();
        }

        chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: monthlyData.map(d => d.month),
                datasets: [{
                    label: 'Attendance Rate',
                    data: monthlyData.map(d => d.rate),
                    borderColor: getComputedStyle(document.documentElement)
                        .getPropertyValue('--secondary').trim(),
                    tension: 0.4,
                    fill: true,
                    backgroundColor: 'rgba(0, 164, 189, 0.1)'
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100,
                        ticks: {
                            callback: value => `${value}%`
                        }
                    }
                }
            }
        });
    }

    // Add animation when student details become visible
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    observer.observe(studentDetails);
}); 