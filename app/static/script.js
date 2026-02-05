const output = document.getElementById("output");

function loadAll() {
    fetch("/parking-spaces")
        .then(res => res.json())
        .then(data => render(data));
}

function loadEmpty() {
    fetch("/parking-spaces/empty")
        .then(res => res.json())
        .then(data => render(data));
}

function checkFull() {
    fetch("/parking-spaces/full-capacity")
        .then(res => res.json())
        .then(data => {
            alert(data.is_full ? "Parking is FULL" : "Parking has empty spaces");
        });
}

function updateExit() {
    const level = document.getElementById("level").value;
    const spot = document.getElementById("spot").value;

    fetch("/parking-spaces/update", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            level: Number(level),
            spot_number: Number(spot)
        })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}

function render(data) {
    output.innerHTML = "";
    data.forEach(space => {
        const div = document.createElement("div");
        div.innerText = `Level ${space.level} - Spot ${space.spot_number} | ${space.is_available ? "Empty" : "Occupied"}`;
        output.appendChild(div);
    });
}
