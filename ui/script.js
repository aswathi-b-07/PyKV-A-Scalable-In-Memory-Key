const SERVER_URL = "http://127.0.0.1:8000";

function showOutput(data) {
    document.getElementById("output").textContent =
        JSON.stringify(data, null, 2);
}

async function setKey() {
    const key = keyInput();
    const value = valueInput();

    const res = await fetch(`${SERVER_URL}/set`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({key, value})
    });

    showOutput(await res.json());
}

async function getKey() {
    const key = keyInput();

    const res = await fetch(`${SERVER_URL}/get/${key}`);
    showOutput(await res.json());
}

async function deleteKey() {
    const key = keyInput();

    if (!key) {
        alert("Please enter a key to delete");
        return;
    }

    const res = await fetch(`${SERVER_URL}/${key}`, {
        method: "DELETE"
    });

    showOutput(await res.json());
}


async function listKeys() {
    const res = await fetch(`${SERVER_URL}/keys`);
    showOutput(await res.json());
}

function keyInput() {
    return document.getElementById("key").value;
}

function valueInput() {
    return document.getElementById("value").value;
}
