
// Переменные для хранения данных
let goalPages = 0;
let readPages = 0;

// Получаем данные из localStorage
const today = new Date().toISOString().slice(0, 10);
const savedDate = localStorage.getItem('lastDate');
const savedPages = localStorage.getItem('readPages');
const savedGoal = localStorage.getItem('goalPages');

// Если день изменился, сбрасываем прочитанные страницы
if (savedDate !== today) {
    localStorage.setItem('readPages', 0);
    localStorage.setItem('lastDate', today);
    localStorage.setItem('goalPages', 0);
} else {
    readPages = parseInt(savedPages) || 0;
    goalPages = parseInt(savedGoal) || 0;
}

// Функция обновления счетчика на странице
function updateCircle() {
    const percentage = (goalPages > 0) ? (readPages / goalPages) * 100 : 0;
    const progressElement = document.querySelector('.progress');
    progressElement.setAttribute('data-percentage', percentage);

    const statusElement = document.getElementById('status');
    statusElement.textContent = `${readPages}/${goalPages}`;

    // Проверяем выполнена ли цель
    const congratulationsMessage = document.getElementById('congratulationsMessage');
    if (readPages >= goalPages && goalPages > 0) {
        congratulationsMessage.style.display = 'block';
    } else {
        congratulationsMessage.style.display = 'none';
    }
}

// Функция для установки цели по страницам
function setGoal() {
    const goalInput = document.getElementById('goal');
    goalPages = parseInt(goalInput.value) || 0;
    localStorage.setItem('goalPages', goalPages);
    updateCircle();
}

// Функция для добавления прочитанных страниц
function addReadPages() {
    const readPagesInput = document.getElementById('readPagesInput');
    const pagesToAdd = parseInt(readPagesInput.value) || 0;
    readPages += pagesToAdd;
    localStorage.setItem('readPages', readPages);
    updateCircle();
}

// Обработать события
document.getElementById('goal').addEventListener('change', setGoal);
document.getElementById('addPages').addEventListener('click', addReadPages);

// Первоначальное обновление счетчика
updateCircle();


