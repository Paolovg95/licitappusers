document.addEventListener('alpine:init', () => {
    Alpine.data('steps', () => ({
      step1: false,
      completed1: false,
      step2: false,
      completed2: false,
      step3: false,
      completed3: false
    }))
})
var submitForm = (data) => {
  console.log("data = ", data);
};
