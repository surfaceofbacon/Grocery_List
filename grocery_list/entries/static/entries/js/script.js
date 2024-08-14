const filterColorSelectEl = document.querySelector('#color-filter')

function filterListItems() {
    const selectedOption = filterColorSelectEl.value
    const groceryEntries = document.querySelectorAll('#groceries-list li')
    if (selectedOption !== "No Filter") groceryEntries.forEach(
        (e) => e.hidden = !e.querySelector(`div[data-color=${selectedOption}]`)
    )
    else groceryEntries.forEach(
        (j) => j.hidden = false
    )
}

filterColorSelectEl.addEventListener('change', filterListItems)


