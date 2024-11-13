document.getElementById('createBtn').addEventListener('click', function() {
    const collectionName = prompt("Введите название коллекции:");
    if (collectionName) {
        const collectionDiv = document.createElement('div');
        collectionDiv.className = 'collection';
        collectionDiv.textContent = collectionName;
        collectionDiv.addEventListener('click', function() {
            alert(`Вы перешли к коллекции: ${collectionName}`);
        });

        document.getElementById('collectionsList').appendChild(collectionDiv);
    }
});

document.getElementById('readFileButton').addEventListener('click', function() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0]; // Получаем первый файл из списка

    if (file && file.type === 'text/plain') {
        const reader = new FileReader();

        reader.onload = function(event) {
            // Получаем содержимое файла
            const content = event.target.result;
            // Отображаем содержимое в <pre> теге
            document.getElementById('fileContent').textContent = content;
        };

        reader.onerror = function(event) {
            console.error("Ошибка чтения файла", event);
        };

        // Читаем файл как текст
        reader.readAsText(file);
    } else {
        alert('Пожалуйста, выберите текстовый файл (.txt)');
    }
});
/*
// запоминаем ник из регистрации
document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const login = document.getElementById('login').value;
    localStorage.setItem('userLogin', login);
    // Перенаправление на другую страницу после регистрации
    location.href = 'MainPage.html';
});

const userLogin = localStorage.getItem('userLogin');
        if (userLogin) {
            document.getElementById('usrNm').textContent = `${userLogin}`;
        } else {
            document.getElementById('usrNm').textContent = ``;
        }
*/

window.onload = function() {
    var storedUsername = localStorage.getItem('username');
    if (storedUsername) {
        document.getElementById('displayUsername').textContent = storedUsername;
    } else {
        document.getElementById('displayUsername').textContent = 'Гость';
    }
};
