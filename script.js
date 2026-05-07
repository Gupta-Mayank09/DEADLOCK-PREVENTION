function call(route) {
    fetch(route)
    .then(res => res.text())
    .then(data => {
        updateStatus(data);
    });
}

function apply(route, text) {
    fetch(route)
    .then(res => res.text())
    .then(data => {
        updateStatus(data);
        showExplanation(text);
    });
}

function updateStatus(data) {
    const status = document.getElementById("status");

    // Reset classes
    status.classList.remove("deadlock", "success");

    if (data.includes("DEADLOCK")) {
        status.classList.add("deadlock");
    } else {
        status.classList.add("success");
    }

    status.innerText = data;
}

function showExplanation(text) {
    const exp = document.getElementById("explanation");

    const explanations = {
        "Mutual Exclusion Broken": "Resources are shared → no exclusive lock.",
        "Hold & Wait Broken": "Processes must request all resources together.",
        "No Preemption Broken": "Resources can be taken back forcibly.",
        "Circular Wait Broken": "Ordering removes cycle → no deadlock."
    };

    exp.innerText = explanations[text];
}