const filterColorSelectEl = document.querySelector('#color-filter')

function filterListItems() {
    const selectedOption = filterColorSelectEl.value
    const groceryEntries = document.querySelectorAll('#groceries-list li')
    function hideIfNotColor(e) {
        e.hidden = !e.querySelector(`div[data-color=${selectedOption}]`)
    }
    function showItems(j) {
        j.hidden = false
    }
    if (selectedOption !== "No Filter") groceryEntries.forEach(
        (e) => e.hidden = !e.querySelector(`div[data-color=${selectedOption}]`)
    )
    else groceryEntries.forEach(showItems)
}

filterColorSelectEl.addEventListener('change', filterListItems)


