// A sleep function that takes in 'ms' as input and pauses for that amount of time
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// When page is loaded or reloaded run the slide to left animation and make image fade in
window.addEventListener("load", async () => {
    await sleep(1600);
    document.querySelector("#harmoniXfer-title").classList.add("animate");
    document.querySelector("#harmoniXfer-caption").classList.add("animate");
    document.querySelector("#transfer-song-button").classList.add("animate");
    document.querySelector("#title-caption-button").classList.add("animate");

    await sleep(900);
    document.querySelector("#image").classList.add("appear-fade-in");
});