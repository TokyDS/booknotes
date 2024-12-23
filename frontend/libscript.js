
let books = [];
let collections = [];

function addBook() {
    const bookInput = document.getElementById('bookInput');
    const bookFile = document.getElementById('bookFile');
    const bookName = bookInput.value.trim();

    if (bookName && bookFile.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const bookContent = e.target.result;
            books.push({ name: bookName, content: bookContent });
            saveBooksToLocalStorage();  // Сохраняем книги в localStorage
            bookInput.value = '';
            bookFile.value = '';
            renderBookList();
        };
        reader.readAsText(bookFile.files[0]);
    } else {
        alert("Пожалуйста, заполните все поля.");
    }
}

function renderBookList() {
    const bookList = document.getElementById('bookList');
    bookList.innerHTML = '';
    books.forEach((book, index) => {
        const li = document.createElement('li');
        li.innerHTML = `<a href="#" onclick="showBookContent(${index})">${book.name}</a> <button onclick="deleteBook(${index})">Удалить</button>`;
        bookList.appendChild(li);
    });
}

function showBookContent(index) {
    const book = books[index];
    localStorage.setItem('currentBook', JSON.stringify(book));
    window.location.href = 'book.html'; // Перенаправляем на новую HTML-страницу
}

function renderCollectionList() {
    const collectionList = document.getElementById('collectionList');
    collectionList.innerHTML = '';
    collections.forEach((collection, index) => {
        const li = document.createElement('li');
        li.innerHTML = `<a href="#" onclick="showCollection(${index})">${collection.name}</a> <button onclick="deleteCollection(${index})">Удалить</button>`;
        collectionList.appendChild(li);
    });
}

function addCollection() {
    const collectionInput = document.getElementById('collectionInput');
    const collectionName = collectionInput.value.trim();

    if (collectionName) {
        collections.push({ name: collectionName, books: [] });
        saveCollectionsToLocalStorage();  // Сохраняем коллекции в localStorage
        collectionInput.value = '';
        renderCollectionList();
    } else {
        alert("Пожалуйста, введите название коллекции.");
    }
}

function showCollection(index) {
    const collection = collections[index];
    localStorage.setItem('currentCollection', JSON.stringify(collection));
    window.location.href = 'collection.html'; // Перенаправляем на новую HTML-страницу
}

function saveBooksToLocalStorage() {
    localStorage.setItem('books', JSON.stringify(books));
}

function saveCollectionsToLocalStorage() {
    localStorage.setItem('collections', JSON.stringify(collections));
}

function loadBooksFromLocalStorage() {
    const loadedBooks = localStorage.getItem('books');
    if (loadedBooks) {
        books = JSON.parse(loadedBooks);
        renderBookList();
    }
}

function loadCollectionsFromLocalStorage() {
    const loadedCollections = localStorage.getItem('collections');
    if (loadedCollections) {
        collections = JSON.parse(loadedCollections);
        renderCollectionList();
    }
}

function deleteCollection(index) {
    collections.splice(index, 1);
    saveCollectionsToLocalStorage;
    renderCollectionList();
}

function deleteBook(index) {
    books.splice(index, 1);
    saveBooksToLocalStorage();
    renderBookList();
}
// Загружаем книги и коллекции из localStorage при загрузке страницы
window.onload = function() {
    loadBooksFromLocalStorage();
    loadCollectionsFromLocalStorage();
};


