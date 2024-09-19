document.addEventListener("alpine:init", () => {
  Alpine.data("layout", () => ({
    profileOpen: false,
    asideOpen: true,
  }));
});

let links = document.querySelectorAll('a[data-active]');
for (let link of links) {
  let link_value = link.attributes['data-active'].value
  let exists = document.querySelector(`[id*="${link_value}-body-container"]`)
  if (exists !== null) {
    link.classList.replace("hover:bg-gray-100","bg-emerald-50")
    link.firstElementChild.classList.add("text-emerald-400")
    link.setAttribute('aria-selected', 'true')
    link.classList.add('selected')
  }
}

function manageTab(event) {
  let currentTab = document.querySelector('[aria-selected=true]');
  currentTab.setAttribute('aria-selected', 'false')
  currentTab.classList.remove('selected')
  currentTab.classList.replace('bg-emerald-50', 'hover:bg-gray-100')
  currentTab.firstElementChild.classList.remove('text-emerald-400')
  let newTab = event.target
  newTab.setAttribute('aria-selected', 'true')
  newTab.classList.add('selected')
  newTab.classList.replace('hover:bg-gray-100','bg-emerald-50')
  newTab.firstElementChild.classList.add('text-emerald-400')
}
