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
      "cupcake",
      {
        custom: {
          "primary": "#25476A",      // A deep navy blue for primary elements
          "secondary": "#6C757D",    // A muted gray for secondary elements
          "accent": "#6610F2",       // A deep purple accent color for highlights
          "neutral": "#212529",      // A very dark gray for text and neutral elements
          "base-100": "#F8F9FA",     // A very light gray for the background base
          "info": "#0DCAF0",         // A cyan for informational elements
          "success": "#198754",      // A green for success messages
          "warning": "#FFC107",      // A vibrant yellow for warnings
          "error": "#DC3545"         // A red for errors
        }
      }
    ],
  },
}

