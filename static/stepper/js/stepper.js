document.addEventListener('alpine:init', () => {
    Alpine.data('steps', () => ({
      step1: false,
      step2: false,
      step3: false,
    }))
})
var submitForm = (data) => {
  console.log("data = ", data);
};
