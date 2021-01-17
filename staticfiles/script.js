// This file contains js used by multiple apps
function reload_with_filter(tags) {
	var params = "";
	for (var i = 0; i < tags.length; i++) {
		var tag_checkbox = document.getElementById(tags[i].name);
		if (tag_checkbox.checked) {
			params += tags[i].name + ",";
		}
	}
	if (params != "") {
		params = params.slice(0,-1);
		var url = window.location.href;
		url = url.split('?')[0];
		url = url + '?tags=' + params;
		window.location.href = url;
	} else {
		var warning = document.getElementById("empty-tags-warning");
		warning.removeAttribute("hidden");
	}
}
