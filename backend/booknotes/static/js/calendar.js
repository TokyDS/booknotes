
const daysContainer = document.querySelector('.days');
const monthYear = document.getElementById('monthYear');
const bookModal = document.getElementById('bookModal');
const bookTitleInput = document.getElementById('bookTitle');
const saveBookButton = document.getElementById('saveBook');
const cancelBookButton = document.getElementById('cancelBook');
const today = new Date();
const bookSelect = document.getElementById('bookSelector')

let currentDate = new Date(today.getFullYear(), today.getMonth(), 1);
let selectedDate = null;
const books = {}; // Объект для хранения книг по датам

function renderCalendar() {
    daysContainer.innerHTML = '';
    monthYear.textContent = currentDate.toLocaleString('default', { month: 'long', year: 'numeric' });

    const firstDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1).getDay();
    const lastDate = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0).getDate();

    for (let i = 0; i < firstDay; i++) {
        const emptyDay = document.createElement('div');
        emptyDay.classList.add('day');
        daysContainer.appendChild(emptyDay);
    }

    for (let date = 1; date <= lastDate; date++) {
        const dayElement = document.createElement('div');
        dayElement.classList.add('day');
        dayElement.textContent = date;
        
        const currentDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), date);
        if (currentDay.toDateString() === today.toDateString()) {
            dayElement.classList.add('today');
        }
        
        const dateKey = `${currentDate.getFullYear()}-${currentDate.getMonth() + 1}-${date}`;
        if (books[dateKey]) {
            dayElement.classList.add('has-book');
            dayElement.textContent += `: ${books[dateKey]}`;
        }

        dayElement.onclick = () => {
            selectedDate = date;
            bookSelect.value = books[dateKey] || '';
            bookModal.style.display = 'block';
        };
        
        daysContainer.appendChild(dayElement);
    }
}

document.getElementById('prevMonth').onclick = () => {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar();
};

document.getElementById('nextMonth').onclick = () => {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar();
};

saveBookButton.onclick = () => {
    const bookTitle = bookSelect.value;
    const dateKey = `${currentDate.getFullYear()}-${currentDate.getMonth() + 1}-${selectedDate}`;
    if (bookTitle) {
        books[dateKey] = bookTitle;
    }
    bookModal.style.display = 'none';
    renderCalendar();
};

cancelBookButton.onclick = () => {
    bookModal.style.display = 'none';
};

renderCalendar();


