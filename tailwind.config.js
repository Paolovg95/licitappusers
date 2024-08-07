/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/**/*.js',
    './licitaciones/forms.py',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {

    opacity: {
      '0': '0',
      '20': '0.2',
      '40': '0.4',
      '60': '0.6',
      '80': '0.8',
      '100': '1',
    },
    extend: {},
  },
  plugins: [require('flowbite/plugin')],
}
