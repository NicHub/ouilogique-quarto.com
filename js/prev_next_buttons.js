"use strict";

/**
 *
 */
function findIdOfCurrentURL(prev_next_links, url) {
    for (let id = 0; id < prev_next_links.length; id++) {
        if (url.includes(prev_next_links[id]["curr"])) {
            return id;
        }
    }
    return -1;
}
// prev_next_links is declared in `prev_next_links.js`.
const url = window.location.href;
const id = findIdOfCurrentURL(prev_next_links, url);
main();

/**
 *
 */
function main() {
    if (id === -1) {
        console.log("Unknown URL");
        return;
    }

    if (
        !(
            prev_next_links[id]["prev"].length > 0 ||
            prev_next_links[id]["next"].length > 0
        )
    ) {
        console.log("No prev nor next");
        return;
    }

    const template_home = `
    <div class="nav-page nav-page-home">
        <a href="/" class="pagination-link">
            ↑ <span class="nav-page-text">Retour à l’accueil</span>
        </a>
    </div>`;

    const template_prev =
        prev_next_links[id]["prev"].length === 0
            ? template_home
            : `
    <div class="nav-page nav-page-previous">
        <a href="${prev_next_links[id]["prev"]}" class="pagination-link">
            ← <span class="nav-page-text">Précédent</span>
        </a>
        </div>`;

        const template_next =
        prev_next_links[id]["next"].length === 0
        ? template_home
        : `
        <div class="nav-page nav-page-next">
        <a href="${prev_next_links[id]["next"]}" class="pagination-link">
            <span class="nav-page-text">Suivant</span> →
        </a>
    </div>`;

    const template_prev_next = `
<nav class="page-navigation">
    ${template_prev}
    ${template_next}
</nav>;`;

    console.log(template_prev_next);
    const quartoContent = document.getElementById("quarto-content");
    quartoContent.innerHTML += template_prev_next;

    document
        .getElementsByTagName("body")[0]
        .addEventListener("keyup", keyboardShortcutHandler);
}

/**
 *
 */
function keyboardShortcutHandler(event) {
    // console.log("");
    // console.log(event);
    // console.log(event.key);
    // console.log(!isNaN(parseInt(event.key)));
    // console.log(parseInt(event.key));
    // console.log(parseFloat(event.key));
    // console.log(parseFloat(event.keyCode));

    if (event.repeat) {
        return;
    }
    const keys_preventdefault = [
        "ArrowUp",
        "ArrowDown",
        "ArrowRight",
        "ArrowLeft",
    ];
    if (keys_preventdefault.includes(event.key)) {
        event.preventDefault();
    }
    if (["ArrowLeft"].includes(event.key)) {
        console.log("ArrowLeft");
        window.location.href = prev_next_links[id]["prev"];
    } else if (["ArrowRight"].includes(event.key)) {
        console.log("ArrowRight");
        window.location.href = prev_next_links[id]["next"];
    } else if (["ArrowUp"].includes(event.key)) {
        console.log("ArrowUp");
        if (event.shiftKey) window.location.href = "/";
    } else {
        return;
    }
}
