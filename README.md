
# API Demo Project

This project provides a simple demo of three APIs that demonstrate various functionalities such as web scraping, fetching artist songs, and fetching singer details.

## Features

1. **Scrapper API**
   - Fetches search results for a given query using the `/api/scrapper` endpoint.

2. **Artist Songs API**
   - Fetches songs and singer details for a specific artist using the `/api/artist/songs` endpoint.

3. **Artist Name API**
   - Fetches a list of all singers' details using the `/api/artist/name` endpoint.


## How to Use

### Prerequisites
- Python 3.x installed.
- Required dependencies installed using `pip install -r requirements.txt`.

### Running the Flask App
1. Clone the repository.
2. Navigate to the project directory.
3. Run the Flask app using:
   ```bash
   python app.py
   ```
4. Access the application at `http://127.0.0.1:5000/`.

---

## API Endpoints

### 1. `/api/scrapper` (POST)
- **Description**: Fetches search results for the input query.
- **Request Body**:
  ```json
  {
    "data": "query string"
  }
  ```
- **Response**:
  ```json
  {
    "status": "success",
    "data": [/* array of search results */]
  }
  ```

### 2. `/api/artist/songs` (POST)
- **Description**: Fetches songs and singer details for the given artist.
- **Request Body**:
  ```json
  {
    "query": "artist name"
  }
  ```
- **Response**:
  ```json
  {
    "status": "success",
    "data": [/* list of songs */],
    "singer": [/* singer details */]
  }
  ```

### 3. `/api/artist/name` (POST)
- **Description**: Fetches details of all singers.
- **Response**:
  ```json
  {
    "status": "success",
    "data": [/* list of all singers */]
  }
  ```

---

## Frontend Example

The project includes an example frontend page to interact with the APIs.

### File Structure
- `index.html`: Demo page for interacting with APIs.
- `static/`: Contains JavaScript files for API calls and CSS for styling.

### Demo Instructions
1. Open `index.html` in a browser.
2. Use the provided fields and buttons to test the APIs:
   - Enter a query for the Scrapper API.
   - Enter an artist name for the Artist Songs API.
   - Fetch all singers using the Artist Name API.

---

## Technologies Used

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript
- **Database**: Supabase

---

## Example Code Snippets

### Scrapper API (JavaScript)
```javascript
async function ScrapperMG() {
    const input = document.getElementById("inputData").value;

    const inputData = { data: input };

    try {
        const response = await fetch("http://127.0.0.1:5000/api/scrapper", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(inputData),
        });

        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

        const data = await response.json();
        console.log("Scrapper data:", data);
    } catch (error) {
        console.error("Error:", error);
    }
}
```

### Artist Songs API (JavaScript)
```javascript
async function FetchSingerSongs() {
    const input = document.getElementById("artistInput").value;

    const inputData = { query: input };

    try {
        const response = await fetch("http://127.0.0.1:5000/api/artist/songs", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(inputData),
        });

        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

        const data = await response.json();
        console.log("Artist data:", data);
    } catch (error) {
        console.error("Error:", error);
    }
}
```

### Artist Name API (JavaScript)
```javascript
async function FetchSingerName() {
    try {
        const response = await fetch("http://127.0.0.1:5000/api/artist/name", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
        });

        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

        const data = await response.json();
        console.log("Singer data:", data);
    } catch (error) {
        console.error("Error:", error);
    }
}
```

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.
```
