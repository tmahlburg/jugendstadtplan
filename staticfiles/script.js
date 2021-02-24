// This	file contains js used by multiple apps
function reload_with_filter(tags, small) {
	var	params = "";
	var	suffix = "";
	if (small) {
		suffix = "-small";
	}
	for	(var i = 0;	i <	tags.length; i++) {
		var	tag_checkbox = document.getElementById(tags[i].name	+ suffix);
		if (tag_checkbox.checked) {
			params += tags[i].name + ",";
		}
	}
	if (params != "") {
		params = params.slice(0,-1);
		var	url	= window.location.href;
		url	= url.split('?')[0];
		url	= url +	'?tags=' + params;
		window.location.href = url;
	} else {
		var	warning	= document.getElementById("empty-tags-warning");
		warning.removeAttribute("hidden");
	}
}

function close_modal_and_reload() {
	document.getElementById("modal").classList.remove("active");
	tags_json =	JSON.parse("{{ tags_json|escapejs }}");
	reload_with_filter(tags_json, true);
}

function uncheck_all() {
	checkboxes = document.getElementsByName("tag");
	checkboxes.forEach(function(checkbox) {
		checkbox.checked = false;
	});
}
