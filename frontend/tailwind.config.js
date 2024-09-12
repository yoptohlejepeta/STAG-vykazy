/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{vue,html,js,ts}"],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: [
      "bumblebee",
    ],
  },
}

