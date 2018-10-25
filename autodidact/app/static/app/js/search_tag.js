let suggested_tags = [];
let applied_tags = [];

function search_tags(value, url, csrf_token) {

    const suggestion_div = document.getElementById('tag_suggestions');
    if (value.length === 0) {
        clear_node(suggestion_div);
        return;
    }

    $.ajax({
        type: "POST",
        url: url,
        dataType: 'json',
        data: {
            'csrfmiddlewaretoken': csrf_token,
            'query': value,
            'limit': 6
        },

        success: function (res) {
            console.log('Search Successful for ' + value);

            const curr_val = document.getElementById('tags').value;
            if (value !== curr_val)
                return;

            clear_node(suggestion_div);

            suggested_tags = res.response;

            console.log('Showing results for ' + value);
            console.log('Current val is ' + curr_val + ' ' + suggested_tags.length);

            if (suggested_tags.length > 0)
                suggestion_div.style.display = 'block';

            for (let i in suggested_tags) {

                let tag = suggested_tags[i];

                if (has_tag(applied_tags, tag) > -1)
                    continue;

                let sTagDiv = document.createElement('div');
                sTagDiv.className = 'tag_suggestion_div';
                sTagDiv.onclick = function () {

                    if (has_tag(applied_tags, tag) === -1) {
                        applied_tags.push(tag);

                        let applied_div = document.getElementById('tag_applied');
                        applied_div.style.display = 'block';

                        let aTagDiv = document.createElement('div');
                        aTagDiv.className = 'tag_applied_div';
                        aTagDiv.onclick = function () {
                            remove_tag(applied_div, aTagDiv, applied_tags, tag);
                        };

                        let aTagP = document.createElement('p');
                        aTagP.className = 'tag_applied_p';

                        aTagP.appendChild(document.createTextNode(tag['fields']['name']));
                        aTagDiv.appendChild(aTagP);
                        applied_div.appendChild(aTagDiv);
                    }
                    remove_tag(suggestion_div, sTagDiv, suggested_tags, tag);
                };

                let sTagP = document.createElement('p');
                sTagP.className = 'tag_suggestion_p';

                sTagP.appendChild(document.createTextNode(tag['fields']['name']));
                sTagDiv.appendChild(sTagP);
                suggestion_div.appendChild(sTagDiv);
            }
        },
        error: function (res) {
            console.log('Search Failed.');
        },
    });
}

function has_tag(arr, tag) {

    let idx = -1;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i]['fields']['name'] === tag['fields']['name']) {
            idx = i;
            break;
        }
    }
    return idx;
}

function remove_tag(div, childDiv, arr, tag) {

    childDiv.remove();
    let idx = has_tag(arr, tag);
    if (idx !== -1)
        arr.splice(idx, 1);

    if (arr.length === 0)
        div.style.display = 'none';
}

function clear_node(node) {
    while (node.hasChildNodes()) {
        node.removeChild(node.lastChild);
    }
    node.style.display = 'none';
}