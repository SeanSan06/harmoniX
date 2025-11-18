function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

window.addEventListener("load", () => {
    document.querySelector("#harmoniXfer-title").classList.add("animate");
    document.querySelector("#harmoniXfer-caption").classList.add("animate");

    sleep(2000);
});