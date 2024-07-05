let links = document.querySelectorAll('a[data-active]');
for (let link of links) {
  let link_value = link.attributes['data-active'].value
  let exists = document.querySelector(`[id*="${link_value}-body-container"]`)
  if (exists !== null) {
    link.classList.replace("hover:bg-gray-100","bg-emerald-50")
    link.firstElementChild.classList.add("text-emerald-400")
  }
}
