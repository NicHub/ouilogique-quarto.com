"use strict";

/**
 * Automatically add `target=_blank` to all links pointing to an external page.
 */
function addTargetBlankToExternalLinks() {
    // Remove subdomain of current site’s url and setup regex.
    let internal = location.host.replace("www.", "");
    internal = new RegExp(internal, "i");
    // Then, grab every link on the page.
    const links = document.getElementsByTagName("a");
    for (let id = 0; id < links.length; id++) {
        // Set the host of each link.
        let href = links[id].host;
        // Make sure the href doesn’t contain current site’s host.
        if (!internal.test(href)) {
            // If it doesn’t, set attributes.
            links[id].setAttribute("target", "_blank");
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    addTargetBlankToExternalLinks();
});
