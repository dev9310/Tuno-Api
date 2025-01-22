function AddData(data) {
    console.log(data);

    // Set singer name
    document.getElementById('singer').innerText = data['singer'][0]['name'] + ' Total songs ' + data['singer'][0]['song_count'];

    // Target the songs container
    const songs_cont = document.querySelector(".songs");

    // Clear existing data (optional, if needed for reuse)
    songs_cont.innerHTML = '';

    // Add each song as a new paragraph
    for (let i in data['data']) {
        console.log(data['data'][i]['title']);
        const NewChild = document.createElement('p');

        NewChild.innerText = data['data'][i]['id'] + " " + data['data'][i]['title'];
        songs_cont.appendChild(NewChild);
    }
}