// This file contains js used by multiple apps
function reload_with_filter(tags, small) {
    var tag_params = "";
    var suffix = "";
    if (small) {
        suffix = "-small";
    }

    for (var i = 0; i < tags.length; i++) {
        var tag_checkbox = document.getElementById(tags[i].name + suffix);
        if (tag_checkbox.checked) {
            tag_params += tags[i].name + ",";
        }
    }

    var for_checkbox = document.getElementById("for");
    var by_checkbox = document.getElementById("by");
    var by_or_for_params = "";
    if (for_checkbox.checked) {
        by_or_for_params += "for,";
    }
    if (by_checkbox.checked) {
        by_or_for_params += "by,";
    }

    if (tag_params != "" || by_or_for_params != "") {
        var url = window.location.href;
        // remove current arguments
        url = url.split('?')[0];
        if (tag_params != "") {
            // remove trailing comma
            tag_params = tag_params.slice(0,-1);
            url = url + '?tags=' + tag_params;
        }
        if (by_or_for_params != "") {
            // remove trailing comma
            by_or_for_params = by_or_for_params.slice(0,-1);
            url = url + '?by_or_for=' + by_or_for_params;
        }
        window.location.href = url;
    } else {
        var warning = document.getElementById("empty-tags-warning");
        warning.removeAttribute("hidden");
    }
}

function close_modal_and_reload(tags) {
    document.getElementById("modal").classList.remove("active");
    tags_json = JSON.parse(tags);
    reload_with_filter(tags_json, true);
}

function uncheck_all() {
    checkboxes = document.getElementsByName("tag");
    checkboxes.forEach(function(checkbox) {
        checkbox.checked = false;
    });
}
