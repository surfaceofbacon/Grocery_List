const filterButtonEl = document.querySelector('#Submit-Priority')

function filterListItems() {
    const filterColorSelectEl = document.querySelector('#color-filter')
    const selectedOption = filterColorSelectEl.value
    const groceryEntries = document.querySelectorAll('#groceries-list li')
    function hideIfNotColor(e) {
        const importanceBlock = e.querySelector('span.importance-color')
        const elementColorValue = importanceBlock.dataset.value
        if (elementColorValue !== selectedOption) e.hidden = true
        else e.hidden = false
    }
    groceryEntries.forEach(hideIfNotColor)
}

filterButtonEl.addEventListener('click', filterListItems)


