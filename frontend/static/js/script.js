document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('predictButton').addEventListener('click', async (event) => {
        event.preventDefault(); // Mencegah form dari pengiriman default
        const math = document.getElementById('math').value;
        const science = document.getElementById('science').value;
        const language = document.getElementById('language').value;
        const english = document.getElementById('english').value;
        const social = document.getElementById('social').value;
        const sports = document.getElementById('sports').value;
        const arts = document.getElementById('arts').value;
        const interest = document.getElementById('interest').value;

        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ math, science, language, english, social, sports, arts, interest })
        });

        if (!response.ok) {
            console.error('Error in response:', response.statusText);
            return;
        }

        const result = await response.json();
        const resultDiv = document.getElementById('result');

        if (result.major === "Jurusan Umum") {
            const majorsList = result.recommended_majors.map(major => `<li style="list-style: none;">${major}</li>`).join('');
            resultDiv.innerHTML = `
                <p>Jurusan yang disarankan berdasarkan minat Anda:</p>
                <ul><strong>${majorsList}</strong></ul>
            `;
        } else {
            resultDiv.innerHTML = `<p>Jurusan yang disarankan: <strong>${result.major}</strong></p>`;
        }
    });
});


let navbar = document.querySelector('.navbar');
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset + height){
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ' ]').classList.add('active')
            })
        }
    })
}

menuIcon.onclick = () => {
    navbar.classList.toggle('active');
}