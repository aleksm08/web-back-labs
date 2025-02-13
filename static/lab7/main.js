function fillFilmList() {
    fetch('/lab7/rest-api/films/')
        .then(response => response.json())
        .then(data => {
            const filmList = document.getElementById('film-list');
            filmList.innerHTML = '';
            data.forEach(film => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${film.title_ru}</td>
                    <td><i>(${film.title})</i></td>
                    <td>${film.film_year}</td>
                    <td>
                        <button class="edit" onclick="editFilm(${film.id})">Редактировать</button>
                        <button class="delete" onclick="deleteFilm(${film.id})">Удалить</button>
                    </td>
                `;
                filmList.appendChild(row);
            });
        });
}

function addFilm() {
    document.getElementById('id').value = '';
    document.getElementById('title-ru').value = '';
    document.getElementById('title').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    document.querySelector('.modal').style.display = 'block';
}

function sendFilm() {
    const id = document.getElementById('id').value;
    const titleRu = document.getElementById('title-ru').value;
    const title = document.getElementById('title').value;
    const year = document.getElementById('year').value;
    const description = document.getElementById('description').value;

    const filmData = {
        title_ru: titleRu,
        title: title,
        film_year: year,
        description: description
    };

    const method = id ? 'PUT' : 'POST';
    const url = id ? `/lab7/rest-api/films/${id}` : '/lab7/rest-api/films/';

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(filmData)
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw err; });
        }
        return response.json();
    })
    .then(data => {
        document.querySelector('.modal').style.display = 'none';
        fillFilmList();
    })
    .catch(error => {
        let errorMessage = 'Ошибка:\n';
        for (const [field, message] of Object.entries(error)) {
            errorMessage += `${field}: ${message}\n`;
        }
        alert(errorMessage);
    });
}

function editFilm(id) {
    fetch(`/lab7/rest-api/films/${id}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('id').value = data.id;
            document.getElementById('title-ru').value = data.title_ru;
            document.getElementById('title').value = data.title;
            document.getElementById('year').value = data.film_year;
            document.getElementById('description').value = data.description;
            document.querySelector('.modal').style.display = 'block';
        });
}


function deleteFilm(id) {
    if (confirm('Вы уверены, что хотите удалить этот фильм?')) {
        fetch(`/lab7/rest-api/films/${id}`, {
            method: 'DELETE'
        })
        .then(() => fillFilmList());
    }
}



function cancel() {
    document.querySelector('.modal').style.display = 'none';
}


document.addEventListener('DOMContentLoaded', fillFilmList);