
let currentCollection;

function goBack() {
    window.location.href = 'Library.html'; // Вернуться обратно
}

window.onload = function() {
    const loadedCollection = localStorage.getItem('currentCollection');
    if (loadedCollection) {
        currentCollection = JSON.parse(loadedCollection);
        renderBooksInCollection();
        loadBooksForSelection();
    }
};

function renderBooksInCollection() {
    const bookInCollectionList = document.getElementById('bookInCollection');
    bookInCollectionList.innerHTML = '';
    
    currentCollection.books.forEach((book, index) => {
        const li = document.createElement('li');
        
        // Создаем элемент для названия книги, который будет кликабельным
        const bookLink = document.createElement('span');
        bookLink.textContent = book.name;
        bookLink.style.cursor = 'pointer'; // Меняем курсор на указатель
        bookLink.onclick = () => showBookContent(index); // Устанавливаем обработчик клика
        
        // Добавляем кнопку для удаления книги
        const removeButton = document.createElement('button');
        removeButton.textContent = "Удалить";
        removeButton.onclick = () => removeBookFromCollection(index);
        
        li.appendChild(bookLink);
        li.appendChild(removeButton);
        bookInCollectionList.appendChild(li);
    });
}

function loadBooksForSelection() {
    const bookSelect = document.getElementById('bookSelect');
    const allBooks = JSON.parse(localStorage.getItem('books'));

    bookSelect.innerHTML = ''; // Очищаем текущий список
    allBooks.forEach((book, index) => {
        const option = document.createElement('option');
        option.value = index; // сохраняем индекс книги
        option.textContent = book.name;
        bookSelect.appendChild(option);
    });
}

function addBookToCollection() {
    const bookSelect = document.getElementById('bookSelect');
    const selectedBookIndex = bookSelect.value;
    
    if (selectedBookIndex !== '') {
        const allBooks = JSON.parse(localStorage.getItem('books'));
        const bookToAdd = allBooks[selectedBookIndex];
        currentCollection.books.push(bookToAdd);
        
        localStorage.setItem('currentCollection', JSON.stringify(currentCollection));
        renderBooksInCollection();
    } else {
        alert("Пожалуйста, выберите книгу для добавления.");
    }
}

function removeBookFromCollection(index) {
    currentCollection.books.splice(index, 1);
    localStorage.setItem('currentCollection', JSON.stringify(currentCollection));
    renderBooksInCollection();
}

function showBookContent(index) {
    const book = currentCollection.books[index]; // Получаем книгу из текущей коллекции
    localStorage.setItem('currentBook', JSON.stringify(book));
    window.location.href = 'book.html'; // Перенаправляем на новую HTML-страницу
}

