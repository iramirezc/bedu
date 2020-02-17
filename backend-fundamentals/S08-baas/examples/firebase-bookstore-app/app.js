/* globals firebase */

/**
 * This is an example of an UI client
 * written in vanilla JavaScript
 * to connect to a Firebase project.
 * NOTE: This app is NOT ready for production!
 */

// Firebase Configuration
// ==================================================

// project configuration
// NOTE: DO NOT commit your keys or secrets to your repository!
const firebaseConfig = {
  apiKey: 'yourApiKey', // update with your own
  projectId: 'yourProjectId' // update with your own
}

// firebase project initialization
firebase.initializeApp(firebaseConfig)

// database connection
const db = firebase.firestore()

// Firebase Helper Functions
// ==================================================

/**
 * Fetches all data from a given firebase collection.
 * @param {string} collectionName
 */
async function fetchCollection (collectionName) {
  return db
    .collection(collectionName)
    .get()
    .then(function (querySnapshot) {
      const data = []

      querySnapshot.forEach(function (obj) {
        data.push({
          id: obj.id,
          ...obj.data()
        })
      })

      return data
    })
}

async function insertIntoCollection (collectionName, data) {
  return db
    .collection(collectionName)
    .add(data)
    .then(function (doc) {
      return doc
    })
}

// Book Collection Functions
// ==================================================

// form to add a book DOM element
const addBookForm = document.getElementById('addBookForm')
// books table DOM element
const booksTable = document.getElementById('booksTable')

/**
 * Formats a date to MM/DD/YYYY
 * @param {string|null|object|Date} date
 */
function formatDate (date) {
  let formattedDate = null

  if (date && typeof date.toDate === 'function') {
    formattedDate = date.toDate().toLocaleDateString()
  } else if (date instanceof Date) {
    formattedDate = date.toLocaleDateString()
  }

  return formattedDate || 'Invalid Date'
}

/**
 * Creates a DOM element 'tr' with the data of a book.
 * @param {object} book
 */
function createBookRow (book) {
  const bookRow = document.createElement('tr')

  bookRow.innerHTML = `
  <td>${book.id}</td>
  <td>${book.title}</td>
  <td>${formatDate(book.publishingDate)}</td>
  <td>${book.author.name}</td>`

  return bookRow
}

/**
 * Fetches the books collection from firestore db.
 */
async function fetchBooks () {
  return fetchCollection('books')
}

/**
 * Appends all the books into the books table.
 */
async function appendBooksToTable () {
  try {
    const books = await fetchBooks()

    books.forEach(function (book) {
      booksTable.appendChild(createBookRow(book))
    })
  } catch (err) {
    console.log(err)
  }
}

/**
 * Inserts a book to the books firestore collection.
 * @param {object} bookData
 */
async function insertBookToCollection (bookData) {
  const savedBookObj = await insertIntoCollection('books', bookData)

  return {
    id: savedBookObj.id,
    ...bookData
  }
}

function cleanBookForm () {
  ['book-title', 'book-publishingDate', 'book-author'].forEach(function (id) {
    document.getElementById(id).value = ''
  })
}

// Application Start
// ==================================================

// load existing books to the table
appendBooksToTable()

// Event listener when a new book is added through the form.
addBookForm.addEventListener('submit', async function (evt) {
  evt.preventDefault()

  try {
    const bookData = {
      title: document.getElementById('book-title').value,
      publishingDate: new Date(document.getElementById('book-publishingDate').value),
      author: {
        name: document.getElementById('book-author').value
      }
    }

    const newBook = await insertBookToCollection(bookData)

    booksTable.appendChild(createBookRow(newBook)) // append new book to books table

    cleanBookForm()
  } catch (err) {
    console.error(err)
  }
})
