function listFiles() {
    const req = new XMLHttpRequest();
    req.addEventListener("load", reqListener);
    req.open("GET", "");
    req.send();
}