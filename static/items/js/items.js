var itemForm = document.querySelectorAll(".item-form")
var items = document.querySelector("#items")
var addButton = document.querySelector("#add-item")
var totalForms = document.querySelector("#id_licitacionitem_set-TOTAL_FORMS")

var formNum = itemForm.length - 1 // Get the number of the last form on the page with zero-based indexing
addButton.addEventListener('click', addForm)

function addForm(e) {
  e.preventDefault()
  let formLength = itemForm.length
  let newForm = itemForm[formLength - 1].cloneNode(true)
  let formRegex = RegExp(`licitacionitem_set-(\\d){1}-`, 'g')

  formNum++ //Increment the form number
  newForm.innerHTML = newForm.innerHTML.replace(formRegex, `licitacionitem_set-${formNum}-`) //Update the new form to have the correct form number
  items.insertAdjacentElement("beforeend", newForm) // Insert the new form at the end of the list of forms

  totalForms.setAttribute('value', `${formNum + 1}`) //Increment the number of total forms in the management form
}
