let links = document.querySelectorAll('a[data-active]');
for (let link of links) {
  let link_value = link.attributes['data-active'].value
  let exists = document.querySelector(`[id*="${link_value}-body-container"]`)
  if (exists !== null) {
    link.classList.replace("text-gray-500", "text-gray-900")
    link.classList.add("bg-blue-50")
  }
}
