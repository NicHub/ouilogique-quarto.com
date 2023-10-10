"use strict";
const prefix = "../.."
let next_link = "";
let prev_link = "";
const texts = ["Retour à l’accueil", "Suivant", "Précédent"];

// file_list is declared in `file_list.js`.
const url = new URL(window.location.href);
let found = false;
let id = 0;
for (id = 0; id < file_list.length; id++) {
    console.log(`file_list[id] = ${file_list[id]}`);

    if (url.pathname.indexOf(file_list[id]) > -1) {
        found = true;
        break;
    }
}

const home_url = `/`

console.log(`url.pathname = ${url.pathname}`);
console.log(`home_url = ${home_url}`);

main();

/**
 *
 */
function main() {
    console.log("prev_next_buttons.js START");

    console.log(`id = ${id}`);
    if (!found) {
        console.log("Unknown URL");
        return;
    }

    const prev_id = (id + 1) % file_list.length;
    const next_id = (id - 1) % file_list.length;
    let prev_link_desc;
    let next_link_desc;

    // Prepare link to previous post.
    if (id === file_list.length - 1) {
        prev_link = home_url;
        prev_link_desc = texts[0];
    } else {
        prev_link = file_list[prev_id];
        prev_link_desc = texts[2];
    }
    prev_link = `${prefix}${prev_link}`
    const template_prev = `
    <div class="nav-page nav-page-home">
        <a href="${prev_link}" class="pagination-link">
            ← <span class="nav-page-text">${prev_link_desc}</span>
        </a>
    </div>`;

    // Prepare link to next post.
    if (id === 0) {
        next_link = home_url;
        next_link_desc = texts[0];
    } else {
        next_link = file_list[next_id];
        next_link_desc = texts[1];
    }
    next_link = `${prefix}${next_link}`
    let template_next = `
    <div class="nav-page nav-page-next">
        <a href="${next_link}" class="pagination-link">
            <span class="nav-page-text">${next_link_desc}</span> →
        </a>
    </div>`;

    // Bundle next and prev links.
    let template_prev_next = `
<nav class="page-navigation">
    ${template_prev}
    ${template_next}
</nav>`;

    // Display links.
    const quartoContent = document.getElementById("quarto-content");
    quartoContent.innerHTML += template_prev_next;
    console.log(template_prev_next);

    // Prepare keyboard shortcuts.
    document
        .getElementsByTagName("body")[0]
        .addEventListener("keyup", keyboardShortcutHandler);
}

/**
 *
 */
function keyboardShortcutHandler(event) {
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
        window.location.href = prev_link;
    } else if (["ArrowRight"].includes(event.key)) {
        window.location.href = next_link;
    } else if (["ArrowUp"].includes(event.key)) {
        if (event.shiftKey) window.location.href =`${prefix}${home_url}`;
    } else {
        return;
    }
}
