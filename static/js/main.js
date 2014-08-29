/*global $, document */

function closeContainer(element, button) {
    "use strict";
    // Hides a section in the cv and reverses the icon (from minus to plus and vice versa)
    element.toggleClass("uk-hidden");
    button.toggleClass("uk-icon-plus-square-o uk-icon-minus-square-o");
}
